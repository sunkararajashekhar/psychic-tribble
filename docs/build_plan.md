# Build plan: FastAPI + Groq WhatsApp Welfare Assistant

## Goal
Create an automated chatbot for:
- PM-KISAN benefits/eligibility/complaints
- Student scholarship eligibility discovery
- Government health scheme guidance

## Architecture
1. **Inbound channel adapters**
   - WhatsApp Cloud API webhook
   - Twilio webhook adapter
   - Gupshup webhook adapter
2. **Conversation orchestrator (agent controller)**
   - Menu/submenu finite-state routing
   - Intent detection fallback
   - AI Q&A mode using Groq LLM
3. **Knowledge/tool layer**
   - Structured scheme cards (benefits, eligibility hints)
   - Complaint guidance templates
   - Optional retrieval over PDF/government pages
4. **State & storage**
   - MVP: in-memory session state
   - Production: Redis for session + Postgres for logs
5. **Observability & guardrails**
   - Request logs, PII-safe logging
   - "not legal advice" style disclaimer and escalation

## Delivery phases

### Phase 1 (MVP - this repo)
- FastAPI endpoint `/chat/incoming`
- Menu/submenu for PM-KISAN, scholarships, health schemes
- Groq AI agent mode
- Provider input normalization

### Phase 2
- Add outbound provider senders (Cloud API/Twilio/Gupshup)
- Replace static text with source-backed retrieval
- Add bilingual Hindi + English responses

### Phase 3
- Multi-agent automation:
  - **Policy agent**: answers rules and eligibility hints
  - **Form agent**: complaint filing checklist and next-step generation
  - **Escalation agent**: confidence threshold + human handoff
- Add analytics dashboard for top intents and drop-off points

### Phase 4
- Deploy (Render/Railway/Fly.io), HTTPS webhook, CI tests
- Add Redis + Postgres + tracing

## Free-first deployment suggestion
- Start with Meta Cloud API if free conversation allowance fits your project scale.
- Use Groq free developer tier for LLM prototyping.
- Keep Twilio/Gupshup adapters optional for future portability.
