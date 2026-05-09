import json
from typing import AsyncGenerator

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
        async with httpx.AsyncClient(timeout=90.0) as client:
            response = await client.post(
                f"{self._base_url}/api/generate", json=payload
            )
            response.raise_for_status()
            return response.json()["response"]

    async def generate_stream(self, prompt: str) -> AsyncGenerator[str, None]:
        payload = {"model": self._model, "prompt": prompt, "stream": True}
        async with httpx.AsyncClient(timeout=90.0) as client:
            async with client.stream(
                "POST", f"{self._base_url}/api/generate", json=payload
            ) as response:
                response.raise_for_status()
                async for line in response.aiter_lines():
                    if line:
                        data = json.loads(line)
                        if not data.get("done"):
                            yield data.get("response", "")
