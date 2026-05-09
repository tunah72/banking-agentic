import json
from app.clients.ollama_client import OllamaClient
from app.core.schemas import HistoryMessage, IntentResult, PriorityResult, PolicyResult, DraftResult

_PROMPT_TEMPLATE = """\
You are a professional banking customer support assistant.
{history_section}
Customer message: {message}
Detected intent: {intent} (confidence: {confidence:.0%})
Priority level: {priority_level}

Relevant policy:
{policy_text}

Support guidelines:
{guidelines}

Write a professional, empathetic response to the customer addressing their concern.
Identify any missing information needed to fully resolve the issue.
Suggest the appropriate next action for the support team.

Respond ONLY with valid JSON in this exact format:
{{"draft_reply": "...", "missing_info": [...], "next_action": "..."}}"""


def _build_prompt(
    message: str,
    history: list[HistoryMessage],
    intent: IntentResult,
    priority: PriorityResult,
    policy: PolicyResult,
) -> str:
    if history:
        lines = "\n".join(
            f"{'Customer' if m.role == 'user' else 'Agent'}: {m.content}"
            for m in history
        )
        history_section = f"\nPrevious conversation:\n{lines}\n"
    else:
        history_section = ""

    guidelines_text = "\n".join(f"- {g}" for g in policy.guidelines)
    return _PROMPT_TEMPLATE.format(
        history_section=history_section,
        message=message,
        intent=intent.intent,
        confidence=intent.confidence,
        priority_level=priority.level,
        policy_text=policy.policy_text,
        guidelines=guidelines_text,
    )


def _parse_raw(raw: str) -> DraftResult:
    try:
        raw_clean = raw.strip()
        if "```" in raw_clean:
            raw_clean = raw_clean.split("```")[1]
            if raw_clean.startswith("json"):
                raw_clean = raw_clean[4:]
        data = json.loads(raw_clean.strip())
        return DraftResult(
            draft_reply=str(data.get("draft_reply", raw)),
            missing_info=list(data.get("missing_info", [])),
            next_action=str(data.get("next_action", "review")),
        )
    except (json.JSONDecodeError, KeyError):
        return DraftResult(draft_reply=raw, missing_info=[], next_action="review")


async def run(
    message: str,
    history: list[HistoryMessage],
    intent: IntentResult,
    priority: PriorityResult,
    policy: PolicyResult,
) -> DraftResult:
    prompt = _build_prompt(message, history, intent, priority, policy)
    client = OllamaClient()
    collected = ""
    async for chunk in client.generate_stream(prompt):
        collected += chunk
    return _parse_raw(collected)
