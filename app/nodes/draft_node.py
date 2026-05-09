import json
from app.clients.ollama_client import OllamaClient
from app.core.schemas import IntentResult, PriorityResult, PolicyResult, DraftResult

_PROMPT_TEMPLATE = """\
You are a professional banking customer support assistant.

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


async def run(
    message: str,
    intent: IntentResult,
    priority: PriorityResult,
    policy: PolicyResult,
) -> DraftResult:
    guidelines_text = "\n".join(f"- {g}" for g in policy.guidelines)
    prompt = _PROMPT_TEMPLATE.format(
        message=message,
        intent=intent.intent,
        confidence=intent.confidence,
        priority_level=priority.level,
        policy_text=policy.policy_text,
        guidelines=guidelines_text,
    )

    raw = await OllamaClient().generate(prompt)

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
