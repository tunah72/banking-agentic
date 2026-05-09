# PLAN.md — Banking AI-Agent

> Kế hoạch triển khai chi tiết. Dựa trên `docs/requirements.md` và phân tích Lab 2 model.

---

## 1. Kiến trúc hệ thống

### 1.1 Tổng quan runtime

```
[Client / curl / Demo UI]
         │ POST /chat
         ▼
[banking-agentic — FastAPI local]
         │
         ├── intent_node ──── HTTP POST ──→ [Colab Notebook 2: Intent Server]
         │                                   (Llama-3.1-8B QLoRA, port 8001, Pinggy)
         │
         ├── draft_node ───── HTTP POST ──→ [Colab Notebook 1: Ollama]
         │                                   (gpt-oss-20b, port 11434, Pinggy)
         │
         ├── priority_node   (local, rules-based)
         ├── policy_node     (local, lookup policies.py)
         ├── validation_node (local, heuristic checks)
         └── router_node     (local, decision logic)
```

### 1.2 Workflow thực thi (thứ tự cố định)

```
CustomerMessage
    → [1] Intent Detection     → IntentResult(intent, confidence, top_k)
    → [2] Priority Detection   → PriorityResult(level, reason, matched_keywords)
    → [3] Policy Retrieval     → PolicyResult(policy_text, guidelines, intent)
    → [4] Response Drafting    → DraftResult(draft_reply, missing_info, next_action)
    → [5] Validation           → ValidationResult(is_valid, issues, should_escalate)
    → [6] Router               → RoutingResult(action, final_response, reason)
         │
         ├── action=reply      → trả phản hồi trực tiếp
         ├── action=ask_more   → yêu cầu khách cung cấp thêm info
         └── action=escalate   → chuyển sang nhân viên
```

---

## 2. Cấu trúc file

```
banking-agentic/
├── .env                         # OLLAMA_URL, INTENT_API_URL (không commit)
├── .env.example                 # Template .env để tham khảo
├── .gitignore
├── README.md
├── requirements.txt
├── run.py                       # Entry point duy nhất
├── PLAN.md                      # File này
├── app/
│   ├── __init__.py
│   ├── main.py                  # FastAPI app + routes
│   ├── core/
│   │   ├── __init__.py
│   │   ├── settings.py          # Pydantic Settings, đọc từ .env
│   │   └── schemas.py           # Tất cả Pydantic models
│   ├── data/
│   │   ├── __init__.py
│   │   └── policies.py          # Dummy policy/FAQ cho 77 intents
│   ├── clients/
│   │   ├── __init__.py
│   │   ├── base.py              # Abstract base class cho LLM client
│   │   ├── ollama_client.py     # Client gọi Ollama (draft generation)
│   │   └── intent_client.py     # Client gọi Intent Inference Server
│   ├── nodes/
│   │   ├── __init__.py
│   │   ├── intent_node.py       # Node 1: gọi IntentClient → IntentResult
│   │   ├── priority_node.py     # Node 2: rules/keywords → PriorityResult
│   │   ├── policy_node.py       # Node 3: lookup policies.py → PolicyResult
│   │   ├── draft_node.py        # Node 4: gọi OllamaClient → DraftResult
│   │   ├── validation_node.py   # Node 5: heuristic checks → ValidationResult
│   │   └── router_node.py       # Node 6: routing decision → RoutingResult
│   └── agent/
│       ├── __init__.py
│       └── orchestrator.py      # Workflow controller, gom WorkflowTrace
├── notebooks/
│   └── intent_server.ipynb      # Colab notebook: chạy Intent Inference Server
├── docs/
│   └── requirements.md
└── examples/
    └── sample_requests.json     # 10+ tin nhắn mẫu, đa dạng intent
```

---

## 3. Kế hoạch triển khai theo phase

### Phase 1 — Foundation

**Mục tiêu:** Thiết lập khung dự án, schemas, và config.

| # | File | Nội dung chính |
|---|------|----------------|
| 1.1 | `requirements.txt` | fastapi, uvicorn, pydantic-settings, httpx, python-dotenv |
| 1.2 | `.env.example` | `OLLAMA_URL=`, `INTENT_API_URL=`, `OLLAMA_MODEL=`, `INTENT_MODEL_ID=` |
| 1.3 | `.gitignore` | `.env`, `__pycache__`, `*.pyc`, `*.egg-info` |
| 1.4 | `app/core/settings.py` | `class Settings(BaseSettings)`, đọc từ `.env`, singleton `get_settings()` |
| 1.5 | `app/core/schemas.py` | Toàn bộ Pydantic models (xem chi tiết bên dưới) |

**Schemas cần định nghĩa trong `schemas.py`:**
```python
# Input
class CustomerRequest(BaseModel):
    message: str

# Node outputs
class IntentResult(BaseModel):
    intent: str
    confidence: float
    top_k: list[dict]            # [{"intent": str, "score": float}]

class PriorityResult(BaseModel):
    level: Literal["low", "medium", "high"]
    reason: str
    matched_keywords: list[str]

class PolicyResult(BaseModel):
    intent: str
    policy_text: str
    guidelines: list[str]

class DraftResult(BaseModel):
    draft_reply: str
    missing_info: list[str]
    next_action: str

class ValidationResult(BaseModel):
    is_valid: bool
    issues: list[str]
    should_escalate: bool

class RoutingResult(BaseModel):
    action: Literal["reply", "ask_more", "escalate"]
    final_response: str
    reason: str

# Trace + final response
class WorkflowTrace(BaseModel):
    intent: IntentResult
    priority: PriorityResult
    policy: PolicyResult
    draft: DraftResult
    validation: ValidationResult
    routing: RoutingResult

class AgentResponse(BaseModel):
    message: str               # final response cho customer
    action: str                # reply | ask_more | escalate
    trace: WorkflowTrace       # intermediate outputs để debug/demo
```

---

### Phase 2 — Data layer

**Mục tiêu:** Dữ liệu policy cho 77 intents + test data.

| # | File | Nội dung chính |
|---|------|----------------|
| 2.1 | `app/data/policies.py` | Dict `POLICIES: dict[str, dict]` — key là intent name, value gồm `policy_text` và `guidelines` |
| 2.2 | `examples/sample_requests.json` | 10–12 tin nhắn mẫu, mỗi tin cover 1 intent khác nhau, bao gồm các case high/medium/low priority |

**77 intents cần cover trong `policies.py`** (từ `label_mapping.json`):

```
activate_my_card, age_limit, apple_pay_or_google_pay, atm_support,
automatic_top_up, balance_not_updated_after_bank_transfer,
balance_not_updated_after_cheque_or_cash_deposit, beneficiary_not_allowed,
cancel_transfer, card_about_to_expire, card_acceptance, card_arrival,
card_delivery_estimate, card_linking, card_not_working,
card_payment_fee_charged, card_payment_not_recognised,
card_payment_wrong_exchange_rate, card_swallowed, cash_withdrawal_charge,
cash_withdrawal_not_recognised, change_pin, compromised_card,
contactless_not_working, country_support, declined_card_payment,
declined_cash_withdrawal, declined_transfer, direct_debit_payment_not_recognised,
disposable_card_limits, edit_personal_details, exchange_charge, exchange_rate,
exchange_via_app, extra_charge_on_statement, failed_transfer,
fiat_currency_support, get_disposable_virtual_card, get_physical_card,
getting_spare_card, getting_virtual_card, lost_or_stolen_card,
lost_or_stolen_phone, order_physical_card, passcode_forgotten,
pending_card_payment, pending_cash_withdrawal, pending_top_up,
pending_transfer, pin_blocked, receiving_money, Refund_not_showing_up,
request_refund, reverted_card_payment?, supported_cards_and_currencies,
terminate_account, top_up_by_bank_transfer_charge, top_up_by_card_charge,
top_up_by_cash_or_cheque, top_up_failed, top_up_limits, top_up_reverted,
topping_up_by_card, transaction_charged_twice, transfer_fee_charged,
transfer_into_account, transfer_not_received_by_recipient, transfer_timing,
unable_to_verify_identity, verify_my_identity, verify_source_of_funds,
verify_top_up, virtual_card_not_working, visa_or_mastercard,
why_verify_identity, wrong_amount_of_cash_received,
wrong_exchange_rate_for_cash_withdrawal
```

**Structure của mỗi entry trong `POLICIES`:**
```python
"lost_or_stolen_card": {
    "policy_text": "If your card is lost or stolen, it must be blocked immediately...",
    "guidelines": [
        "Advise customer to block card immediately via app.",
        "Offer to order replacement card.",
        "Check if any unauthorized transactions occurred.",
    ]
}
```

---

### Phase 3 — Client layer

**Mục tiêu:** HTTP clients cho Ollama và Intent Inference Server.

| # | File | Nội dung chính |
|---|------|----------------|
| 3.1 | `app/clients/base.py` | `class BaseLLMClient(ABC)` với `async def generate(prompt: str) -> str` |
| 3.2 | `app/clients/ollama_client.py` | `class OllamaClient(BaseLLMClient)` — POST đến `OLLAMA_URL/api/generate`, handle timeout/error |
| 3.3 | `app/clients/intent_client.py` | `class IntentClient` — POST đến `INTENT_API_URL/predict`, trả về `IntentResult` |

**Lưu ý `ollama_client.py`:**
- Payload: `{"model": settings.ollama_model, "prompt": prompt, "stream": false}`
- Timeout: 60s (model generation có thể chậm)
- Nếu Ollama không available → raise `RuntimeError` rõ ràng

**Lưu ý `intent_client.py`:**
- Payload: `{"text": message}`
- Expected response: `{"intent": str, "confidence": float, "top_k": [...]}`
- Timeout: 30s
- Không kế thừa `BaseLLMClient` (classification ≠ generation interface)

---

### Phase 4 — Nodes

**Mục tiêu:** Implement 6 nodes theo đúng spec.

#### Node 1: `intent_node.py`

```python
async def run(message: str) -> IntentResult:
    client = IntentClient(settings.intent_api_url)
    return await client.predict(message)
```

- Chỉ là thin wrapper gọi `IntentClient`
- Không chứa model loading (model nằm trên Colab)

#### Node 2: `priority_node.py`

**Logic phân loại priority** (rules-based, không dùng LLM):

```
HIGH:   compromised_card, lost_or_stolen_card, lost_or_stolen_phone,
        pin_blocked, unable_to_verify_identity, transaction_charged_twice,
        card_swallowed, failed_transfer, declined_transfer
        HOẶC confidence < 0.5 (intent uncertain)

MEDIUM: declined_card_payment, declined_cash_withdrawal, card_not_working,
        top_up_failed, balance_not_updated_*, pending_transfer, request_refund,
        Refund_not_showing_up, extra_charge_on_statement

LOW:    tất cả còn lại (informational, inquiry intents)
```

Trả về `PriorityResult(level, reason, matched_keywords)`.

#### Node 3: `policy_node.py`

```python
def run(intent: str) -> PolicyResult:
    policy = POLICIES.get(intent, POLICIES["_default"])
    return PolicyResult(intent=intent, **policy)
```

- Lookup O(1) từ dict `POLICIES`
- Fallback `_default` nếu intent không có trong dict

#### Node 4: `draft_node.py`

**Prompt template:**
```
You are a banking customer support assistant.

Customer message: {message}
Detected intent: {intent} (confidence: {confidence:.0%})
Priority level: {priority_level}

Relevant policy:
{policy_text}

Guidelines:
{guidelines_formatted}

Write a professional, empathetic response to the customer.
Also identify: (1) any missing information needed, (2) recommended next action.

Respond in JSON format:
{{"draft_reply": "...", "missing_info": [...], "next_action": "..."}}
```

- Gọi `OllamaClient.generate(prompt)`
- Parse JSON response → `DraftResult`
- Nếu parse JSON thất bại → fallback: dùng toàn bộ output làm `draft_reply`, `missing_info=[]`

#### Node 5: `validation_node.py`

**Kiểm tra:**
1. `draft_reply` quá ngắn (< 50 ký tự) → issue: "response_too_short"
2. `confidence < 0.4` → issue: "low_intent_confidence", `should_escalate=True`
3. `priority == "high"` và `missing_info` không rỗng → issue: "high_priority_missing_info", `should_escalate=True`
4. `draft_reply` rỗng hoặc parse thất bại → issue: "draft_generation_failed", `should_escalate=True`

`is_valid = len(issues) == 0`

#### Node 6: `router_node.py`

**Logic routing:**
```
IF should_escalate OR priority == "high":
    action = "escalate"
    final_response = escalation_message

ELIF missing_info không rỗng AND NOT is_valid:
    action = "ask_more"
    final_response = ask_more_message (gắn missing_info vào)

ELSE:
    action = "reply"
    final_response = draft_reply
```

---

### Phase 5 — Orchestrator + API

| # | File | Nội dung chính |
|---|------|----------------|
| 5.1 | `orchestrator.py` | Gọi 6 node theo thứ tự, gom `WorkflowTrace`, return `AgentResponse` |
| 5.2 | `app/main.py` | `POST /chat` → gọi orchestrator; `GET /health` → status check |
| 5.3 | `run.py` | Chỉ: `uvicorn.run(app, host="0.0.0.0", port=8000)` |

**`orchestrator.py` skeleton:**
```python
async def run_workflow(request: CustomerRequest) -> AgentResponse:
    intent   = await intent_node.run(request.message)
    priority = priority_node.run(request.message, intent)
    policy   = policy_node.run(intent.intent)
    draft    = await draft_node.run(request.message, intent, priority, policy)
    validation = validation_node.run(draft, intent, priority)
    routing  = router_node.run(draft, validation, priority)

    trace = WorkflowTrace(intent=intent, priority=priority, policy=policy,
                          draft=draft, validation=validation, routing=routing)
    return AgentResponse(message=routing.final_response,
                         action=routing.action, trace=trace)
```

**API `/chat` response:** hiện tại trả về `AgentResponse` đầy đủ (có `trace`). Sẽ quyết định sau liệu có ẩn trace trong production response hay không.

---

### Phase 6 — Colab Intent Server

**Mục tiêu:** Notebook mới `notebooks/intent_server.ipynb` để chạy trên Colab.

**Nội dung notebook:**

1. Mount Google Drive (checkpoint tại `/content/drive/MyDrive/banking-intent-unsloth/`)
2. Clone repo `banking-intent-unsloth` (để lấy `scripts/inference.py`)
3. Install dependencies (Unsloth, bitsandbytes, FastAPI, uvicorn, pyngrok/pinggy)
4. Load `IntentClassification` — **sửa `__call__` trả về `(intent, confidence, top_k)`**
5. Định nghĩa FastAPI app với endpoint `POST /predict`
6. Chạy Pinggy để expose port 8001 → lấy public URL → paste vào `.env` của local project

**Modified `IntentClassification.__call__` output:**
```python
# Thêm softmax để tính confidence + top_k
import torch.nn.functional as F

probs = F.softmax(outputs.logits, dim=-1)[0]
top_k_values, top_k_indices = torch.topk(probs, k=5)
return {
    "intent": self.id2label[probs.argmax().item()],
    "confidence": probs.max().item(),
    "top_k": [{"intent": self.id2label[i.item()], "score": s.item()}
              for i, s in zip(top_k_indices, top_k_values)]
}
```

---

### Phase 7 — Documentation

| # | File | Nội dung |
|---|------|----------|
| 7.1 | `README.md` | Mục tiêu project, workflow diagram, setup guide, URL demo video |

---

## 4. Quy tắc quan trọng (Implementation Rules)

### Bắt buộc (MUST)

| Rule | Lý do |
|------|-------|
| Intent node PHẢI gọi Colab inference server, không được dùng model khác | Yêu cầu cứng: phải dùng fine-tuned model từ Lab 2 |
| `run.py` chỉ chứa `uvicorn.run(...)`, không có business logic | Spec yêu cầu tách biệt entry point |
| Thứ tự node cố định: Intent→Priority→Policy→Draft→Validation→Router | Spec workflow |
| Tất cả URLs đọc từ `.env` qua `settings.py`, không hardcode | Pinggy URL thay đổi mỗi session |
| `policies.py` cover đủ 77 intents của BANKING77 | Spec yêu cầu |
| `base.py` là abstract class, `OllamaClient` kế thừa | Spec yêu cầu abstraction layer |

### Không được làm (MUST NOT)

| Rule | Lý do |
|------|-------|
| Không commit `.env` file | Chứa API URLs private |
| Không load model trong `intent_node.py` hoặc bất kỳ node nào local | Model chỉ chạy trên Colab |
| Không để business logic trong `run.py` | Vi phạm spec |
| Không bỏ qua `validation_node` dù kết quả luôn `is_valid=True` | Node bắt buộc có mặt trong workflow |

### Khuyến nghị (SHOULD)

| Rule | Lý do |
|------|-------|
| Dùng `async/await` cho các node gọi HTTP (intent, draft) | Non-blocking I/O |
| Priority node và Policy node là sync (không cần async) | Không I/O, chỉ computation local |
| `IntentClient` và `OllamaClient` dùng `httpx.AsyncClient` | Consistent async pattern |
| Thêm `GET /health` endpoint check connectivity Ollama + Intent server | Dễ debug khi demo |

---

## 5. Checklist triển khai

### Phase 1 — Foundation
- [ ] `requirements.txt`
- [ ] `.env.example`
- [ ] `.gitignore`
- [ ] `app/core/settings.py`
- [ ] `app/core/schemas.py`

### Phase 2 — Data layer
- [ ] `app/data/policies.py` (77 intents)
- [ ] `examples/sample_requests.json`

### Phase 3 — Client layer
- [ ] `app/clients/base.py`
- [ ] `app/clients/ollama_client.py`
- [ ] `app/clients/intent_client.py`

### Phase 4 — Nodes
- [ ] `app/nodes/intent_node.py`
- [ ] `app/nodes/priority_node.py`
- [ ] `app/nodes/policy_node.py`
- [ ] `app/nodes/draft_node.py`
- [ ] `app/nodes/validation_node.py`
- [ ] `app/nodes/router_node.py`

### Phase 5 — Orchestrator + API
- [ ] `app/agent/orchestrator.py`
- [ ] `app/main.py`
- [ ] `run.py`

### Phase 6 — Colab Intent Server
- [ ] `notebooks/intent_server.ipynb`

### Phase 7 — Documentation
- [ ] `README.md`
- [ ] Video demo (2–5 phút)
- [ ] Push lên GitHub

---

## 6. Câu hỏi còn lại cần xác nhận

1. **HuggingFace model ID**: Tên repository HF của fine-tuned model là gì (dạng `username/repo-name`)? Cần để notebook tải model trực tiếp từ HF thay vì phải restore từ Drive.
2. **Ngôn ngữ response**: Draft reply của `draft_node` sẽ sinh ra tiếng Anh hay tiếng Việt? (Theo BANKING77 là dataset tiếng Anh nên tin nhắn input cũng tiếng Anh — nên giữ English là hợp lý.)
