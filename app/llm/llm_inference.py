import re
import json
import logging
from pydantic import ValidationError
from app.llm.knowledge_base import retrieve_knowledge
from app.llm.providers.groq_provider import GroqProvider
from app.llm.providers.hf_provider import HuggingFaceProvider
from app.llm.provider import LLMProviderError
from app.prompts.repair_prompt import repair_prompt
from app.schemas.taxonomy_data import TaxonomyOutput

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

groq = GroqProvider()
hugging_face = HuggingFaceProvider()

def infer(system_prompt: str, user_prompt: str):
    logger.info("Starting inference process...")
    logger.info(f"User prompt length: {len(user_prompt)} characters")
    
    logger.info("Retrieving knowledge base...")
    knowledge_base = retrieve_knowledge(user_prompt)
    logger.info(f"Knowledge base retrieved: {len(knowledge_base)} characters")
    
    full_prompt = f"{user_prompt}\n\nRelevant Information:\n{knowledge_base}"
    logger.info(f"Final prompt length: {len(full_prompt)} characters")
    
    # Try providers with fallback
    try:
        raw, usage = groq.infer(system_prompt, full_prompt)
        provider = "groq"
        logger.info("Groq response received, processing...")
    except LLMProviderError as e:
        logger.warning(f"Groq failed, falling back to Together: {e}")
        raw, usage = hugging_face.infer(system_prompt, full_prompt)
        provider = "together"
        logger.info("Together response received, processing...")
    
    logger.info(f"Raw {provider} output: {raw}")
    
    # Process response with validation and repair
    try:
        if not raw:
            raise ValueError(f"Empty response from {provider}")
        
        logger.info("Parsing JSON response...")
        extracted_json = extract_json(raw)
        logger.info("JSON extraction successful")
        logger.info("Validating output structure...")
        result = validate_output(extracted_json)
        logger.info(f"Inference completed successfully using {provider}")
        return result, usage
        
    except Exception as e:
        logger.error(f"{provider} inference failed: {e}")
        logger.error("Falling back to repair prompt")
        fallback_content = raw if raw else str(e)
        content = repair_output_prompt(fallback_content, provider)
        
    logger.info("Final validation attempt...")
    extracted_json = extract_json(content)
    logger.info("JSON extraction successful")
    logger.info("Validating output structure...")
    result = validate_output(extracted_json)
    logger.info("Inference completed successfully after repair")
    
    return result, usage

def extract_json(raw: str) -> dict:
    match = re.search(r"\{[\s\S]*?\}", raw)
    if not match:
        raise ValueError("No JSON object found")
    return json.loads(match.group())

def repair_output_prompt(raw: str, provider: str) -> str:
    logger.info(f"Starting repair prompt process using {provider}...")
    repair_system_prompt = repair_prompt + f"\n\n {raw}\n\nCorrected JSON:"
    logger.info(f"Sending repair prompt to {provider}...")
    
    # Use the same provider for repair
    try:
        if provider == "groq":
            repair_content, _ = groq.infer(repair_system_prompt, "")
        else:
            repair_content, _ = hugging_face.infer(repair_system_prompt, "")
    except LLMProviderError:
        # If repair fails, try the other provider
        logger.warning(f"Repair failed on {provider}, trying alternate provider")
        if provider == "groq":
            repair_content, _ = hugging_face.infer(repair_system_prompt, "")
        else:
            repair_content, _ = groq.infer(repair_system_prompt, "")
    
    logger.info(f"Raw repair output: {repair_content}")
    return repair_content or "{}"

def validate_output(output: dict):
    logger.info("Starting output validation...")
    logger.info(f"Output keys: {list(output.keys())}")
    
    try:
        validated = TaxonomyOutput.model_validate(output)
        logger.info("Output validation successful")
        return validated
    except ValidationError as e:
        logger.error(f"Output validation failed: {e}")
        raise ValueError(f"Invalid taxonomy output: {e}")