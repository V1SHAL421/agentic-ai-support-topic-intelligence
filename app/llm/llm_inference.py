import httpx
import os

from app.schemas.taxonomy_data import TaxonomyOutput

def infer(model: str, system_prompt: str, user_prompt: str, max_tokens: int = 512, temp: float = 0.1):
    base_url = os.environ.get("VLLM_URL", "http://localhost:8000")

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "max_tokens": max_tokens,
        "temperature": temp,
    }

    with httpx.Client(base_url=base_url) as client:
        response = client.post("/v1/chat/completions", json=payload)
        data = response.json()
        return data['choices'][0]['message']['content']

def validate_output(output: dict):
    taxonomy_output = TaxonomyOutput.model_validate(output)
    return taxonomy_output
    