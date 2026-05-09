from app.core.schemas import DraftResult, ValidationResult, PriorityResult, RoutingResult

_ESCALATION_MESSAGE = (
    "Thank you for contacting us. Your request has been flagged as high priority "
    "and is being escalated to our specialist support team. A representative will "
    "reach out to you shortly. We apologize for any inconvenience."
)


def run(
    draft: DraftResult,
    validation: ValidationResult,
    priority: PriorityResult,
) -> RoutingResult:
    if validation.should_escalate or priority.level == "high":
        return RoutingResult(
            action="escalate",
            final_response=_ESCALATION_MESSAGE,
            reason=f"Escalated: priority={priority.level}, issues={validation.issues}",
        )

    if draft.missing_info and not validation.is_valid:
        missing_str = ", ".join(draft.missing_info)
        return RoutingResult(
            action="ask_more",
            final_response=(
                f"{draft.draft_reply}\n\nTo help resolve your request completely, "
                f"could you please provide: {missing_str}?"
            ),
            reason=f"Missing information required: {missing_str}",
        )

    return RoutingResult(
        action="reply",
        final_response=draft.draft_reply,
        reason="Valid response generated with sufficient confidence.",
    )
