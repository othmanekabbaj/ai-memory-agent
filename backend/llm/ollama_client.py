from ollama import chat
from config import OLLAMA_MODEL

class OllamaClient:
    def chat(self, prompt: str) -> str:
        response = chat(
            model=OLLAMA_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response.message.content