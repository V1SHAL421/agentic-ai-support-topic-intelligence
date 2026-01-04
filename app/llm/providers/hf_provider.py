import json
from huggingface_hub import InferenceClient
from app.constants import HF_API_KEY, HF_MODEL
from app.llm.provider import LLMProviderError


class HuggingFaceProvider:
    def __init__(self):
        if not HF_API_KEY:
            raise LLMProviderError("HF_API_KEY not set")

        self.client = InferenceClient(
            model=HF_MODEL,
            token=HF_API_KEY
        )

    def infer(self, system_prompt: str, user_prompt: str):
        try:
            response = self.client.chat.completions.create(
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                temperature=0.1,
                max_tokens=100,
            )

            content = response.choices[0].message.content
            if not content:
                raise LLMProviderError("Empty response from Hugging Face")

            usage = {
                "prompt_tokens": getattr(response.usage, "prompt_tokens", 0),
                "completion_tokens": getattr(response.usage, "completion_tokens", 0),
                "total_tokens": getattr(response.usage, "total_tokens", 0),
            }

            return content, usage

        except Exception as e:
            raise LLMProviderError(f"Hugging Face API error: {e}")