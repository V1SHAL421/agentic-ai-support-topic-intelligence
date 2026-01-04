import requests
import os
from app.llm.provider import LLMProviderError

class TogetherProvider:
    def __init__(self):
        self.api_key = os.getenv("TOGETHER_API_KEY")
        self.base_url = "https://api.together.xyz/v1/chat/completions"
    
    def infer(self, system_prompt: str, user_prompt: str):
        try:
            response = requests.post(
                self.base_url,
                headers={"Authorization": f"Bearer {self.api_key}"},
                json={
                    "model": "meta-llama/Llama-3.2-3B-Instruct-Turbo",
                    "messages": [
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt}
                    ],
                    "temperature": 0.1,
                    "max_tokens": 100
                }
            )
            
            if response.status_code != 200:
                raise LLMProviderError(f"Together API error: {response.status_code}")
                
            data = response.json()
            content = data["choices"][0]["message"]["content"]
            usage = data.get("usage", {})
            
            return content, usage
            
        except Exception as e:
            raise LLMProviderError(f"Together API error: {e}")