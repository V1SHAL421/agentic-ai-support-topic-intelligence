import requests
from app.constants import GEMINI_API_KEY, GEMINI_MODEL
from app.llm.provider import LLMProviderError


class GeminiProvider:
    def __init__(self):
        if not GEMINI_API_KEY:
            raise LLMProviderError("GEMINI_API_KEY not set")

        self.api_key = GEMINI_API_KEY
        self.base_url = (
            f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent"
        )

    def infer(self, system_prompt: str, user_prompt: str):
        payload = {
            "system_instruction": {"parts": [{"text": system_prompt}]},
            "contents": [{"role": "user", "parts": [{"text": user_prompt}]}],
            "generation_config": {"temperature": 0.1, "max_output_tokens": 100},
        }

        try:
            response = requests.post(
                f"{self.base_url}?key={self.api_key}",
                headers={"Content-Type": "application/json"},
                json=payload,
                timeout=30,
            )

            if response.status_code != 200:
                try:
                    error_detail = response.json()
                except Exception:
                    error_detail = response.text
                raise LLMProviderError(
                    f"Gemini API error: {response.status_code} {error_detail}"
                )

            data = response.json()
            candidates = data.get("candidates", [])
            if not candidates:
                raise LLMProviderError("Gemini API returned no candidates")

            parts = candidates[0].get("content", {}).get("parts", [])
            if not parts or "text" not in parts[0]:
                raise LLMProviderError("Gemini API response missing text content")

            content = parts[0]["text"]
            usage_metadata = data.get("usageMetadata", {})
            usage = {
                "prompt_tokens": usage_metadata.get("promptTokenCount", 0),
                "completion_tokens": usage_metadata.get("candidatesTokenCount", 0),
                "total_tokens": usage_metadata.get("totalTokenCount", 0),
            }

            return content, usage

        except LLMProviderError:
            raise
        except Exception as e:
            raise LLMProviderError(f"Gemini API error: {e}")
