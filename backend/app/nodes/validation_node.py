from app.core.schemas import IntentResult, PriorityResult, DraftResult, ValidationResult

_MIN_REPLY_LENGTH = 50
_LOW_CONFIDENCE_THRESHOLD = 0.4


def run(
    draft: DraftResult,
    intent: IntentResult,
    priority: PriorityResult,
) -> ValidationResult:
    issues: list[str] = []
    should_escalate = False

    if not draft.draft_reply or not draft.draft_reply.strip():
        issues.append("draft_generation_failed")
        should_escalate = True
    elif len(draft.draft_reply.strip()) < _MIN_REPLY_LENGTH:
        issues.append("response_too_short")

    if intent.confidence < _LOW_CONFIDENCE_THRESHOLD:
        issues.append("low_intent_confidence")
        should_escalate = True

    if priority.level == "high" and draft.missing_info:
        issues.append("high_priority_missing_info")
        should_escalate = True

    return ValidationResult(
        is_valid=len(issues) == 0,
        issues=issues,
        should_escalate=should_escalate,
    )
