import asyncio
import json
from typing import AsyncGenerator

from app.core.schemas import CustomerRequest, AgentResponse, WorkflowTrace
from app.nodes import intent_node, priority_node, policy_node, draft_node, validation_node, router_node


async def run_workflow(request: CustomerRequest) -> AgentResponse:
    intent = await intent_node.run(request.message)
    priority = priority_node.run(request.message, intent)
    policy = policy_node.run(intent.intent)
    draft = await draft_node.run(request.message, request.history, intent, priority, policy)
    validation = validation_node.run(draft, intent, priority)
    routing = router_node.run(draft, validation, priority)

    trace = WorkflowTrace(
        intent=intent,
        priority=priority,
        policy=policy,
        draft=draft,
        validation=validation,
        routing=routing,
    )
    return AgentResponse(
        message=routing.final_response,
        action=routing.action,
        trace=trace,
    )


async def run_workflow_stream(request: CustomerRequest) -> AsyncGenerator[str, None]:
    intent = await intent_node.run(request.message)
    priority = priority_node.run(request.message, intent)
    policy = policy_node.run(intent.intent)
    draft = await draft_node.run(request.message, request.history, intent, priority, policy)
    validation = validation_node.run(draft, intent, priority)
    routing = router_node.run(draft, validation, priority)

    trace = WorkflowTrace(
        intent=intent,
        priority=priority,
        policy=policy,
        draft=draft,
        validation=validation,
        routing=routing,
    )

    words = routing.final_response.split()
    for i, word in enumerate(words):
        text = word if i == 0 else " " + word
        yield json.dumps({"type": "chunk", "text": text}, ensure_ascii=False)
        await asyncio.sleep(0.04)

    yield json.dumps({
        "type": "done",
        "action": routing.action,
        "trace": trace.model_dump(),
    }, ensure_ascii=False)
