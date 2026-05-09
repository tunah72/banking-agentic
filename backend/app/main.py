from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from app.core.schemas import CustomerRequest, AgentResponse
from app.agent.orchestrator import run_workflow, run_workflow_stream
from app.core.settings import get_settings

app = FastAPI(title="Banking AI Agent", version="1.0.0")


@app.post("/chat", response_model=AgentResponse)
async def chat(request: CustomerRequest) -> AgentResponse:
    try:
        return await run_workflow(request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/chat/stream")
async def chat_stream(request: CustomerRequest) -> StreamingResponse:
    async def event_generator():
        async for payload in run_workflow_stream(request):
            yield f"data: {payload}\n\n"

    return StreamingResponse(event_generator(), media_type="text/event-stream")


@app.get("/health")
async def health() -> dict:
    settings = get_settings()
    return {
        "status": "ok",
        "ollama_url": settings.ollama_url,
        "intent_api_url": settings.intent_api_url,
    }
