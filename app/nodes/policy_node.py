from app.core.schemas import PolicyResult
from app.data.policies import POLICIES


def run(intent: str) -> PolicyResult:
    entry = POLICIES.get(intent) or POLICIES["_default"]
    return PolicyResult(
        intent=intent,
        policy_text=entry["policy_text"],
        guidelines=entry["guidelines"],
    )
