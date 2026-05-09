import httpx
from app.clients.base import BaseLLMClient
from app.core.settings import get_settings


class OllamaClient(BaseLLMClient):
    def __init__(self) -> None:
        settings = get_settings()
        self._base_url = settings.ollama_url.rstrip("/")
        self._model = settings.ollama_model

    async def generate(self, prompt: str) -> str:
        payload = {"model": self._model, "prompt": prompt, "stream": False}
        async with httpx.AsyncClient(timeout=60.0) as client:
            response = await client.post(
                f"{self._base_url}/api/generate", json=payload
            )
            response.raise_for_status()
            return response.json()["response"]
