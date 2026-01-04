import json
from groq import Groq
from app.constants import GROQ_API_KEY, GROQ_MODEL
from app.llm.provider import LLMProviderError

class GroqProvider:
    def __init__(self):
        self.client = Groq(api_key=GROQ_API_KEY)
    
    def infer(self, system_prompt: str, user_prompt: str):
        try:
            response = self.client.chat.completions.create(
                model=GROQ_MODEL,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.1,
                max_tokens=100,
                response_format={"type": "json_object"}
            )
            
            content = response.choices[0].message.content
            if not content:
                raise LLMProviderError("Empty response from Groq")
                
            usage = {
                'prompt_tokens': response.usage.prompt_tokens,
                'completion_tokens': response.usage.completion_tokens,
                'total_tokens': response.usage.total_tokens
            }
            
            return content, usage
            
        except Exception as e:
            raise LLMProviderError(f"Groq API error: {e}")