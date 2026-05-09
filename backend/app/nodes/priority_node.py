from app.core.schemas import IntentResult, PriorityResult

_HIGH_INTENTS = {
    "compromised_card",
    "lost_or_stolen_card",
    "lost_or_stolen_phone",
    "pin_blocked",
    "unable_to_verify_identity",
    "transaction_charged_twice",
    "card_swallowed",
    "failed_transfer",
    "declined_transfer",
    "cash_withdrawal_not_recognised",
    "card_payment_not_recognised",
}

_MEDIUM_INTENTS = {
    "declined_card_payment",
    "declined_cash_withdrawal",
    "card_not_working",
    "top_up_failed",
    "balance_not_updated_after_bank_transfer",
    "balance_not_updated_after_cheque_or_cash_deposit",
    "pending_transfer",
    "request_refund",
    "Refund_not_showing_up",
    "extra_charge_on_statement",
    "beneficiary_not_allowed",
    "cancel_transfer",
    "transfer_not_received_by_recipient",
    "virtual_card_not_working",
    "contactless_not_working",
    "top_up_reverted",
    "card_payment_wrong_exchange_rate",
    "wrong_exchange_rate_for_cash_withdrawal",
    "wrong_amount_of_cash_received",
}

_HIGH_KEYWORDS = [
    "stolen", "lost", "fraud", "suspicious", "unauthorized",
    "blocked", "compromised", "hacked", "scam",
    "double charge", "charged twice", "wrong charge", "missing money",
]

_MEDIUM_KEYWORDS = [
    "not working", "declined", "failed", "error", "rejected",
    "refund", "pending", "not received", "not showing",
]

_LOW_CONFIDENCE_THRESHOLD = 0.5


def run(message: str, intent_result: IntentResult) -> PriorityResult:
    if intent_result.confidence < _LOW_CONFIDENCE_THRESHOLD:
        return PriorityResult(
            level="high",
            reason="Intent confidence below threshold — escalation recommended.",
            matched_keywords=["low_confidence"],
        )

    message_lower = message.lower()
    matched: list[str] = []

    for kw in _HIGH_KEYWORDS:
        if kw in message_lower:
            matched.append(kw)

    if intent_result.intent in _HIGH_INTENTS or matched:
        return PriorityResult(
            level="high",
            reason=f"High-risk intent '{intent_result.intent}' or critical keywords detected.",
            matched_keywords=matched,
        )

    for kw in _MEDIUM_KEYWORDS:
        if kw in message_lower:
            matched.append(kw)

    if intent_result.intent in _MEDIUM_INTENTS or matched:
        return PriorityResult(
            level="medium",
            reason=f"Issue-related intent '{intent_result.intent}' requires prompt attention.",
            matched_keywords=matched,
        )

    return PriorityResult(
        level="low",
        reason="Informational or routine inquiry.",
        matched_keywords=[],
    )
