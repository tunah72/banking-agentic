import httpx
from app.core.schemas import IntentResult
from app.core.settings import get_settings


class IntentClient:
    def __init__(self) -> None:
        settings = get_settings()
        self._base_url = settings.intent_api_url.rstrip("/")

    async def predict(self, text: str) -> IntentResult:
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(
                f"{self._base_url}/predict", json={"text": text}
            )
            response.raise_for_status()
            return IntentResult(**response.json())
