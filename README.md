# FastAPI Welfare Chatbot (WhatsApp + Groq) for CSP project

This project is a starter chatbot backend for Indian public-benefit guidance with:

- **PM-KISAN** (benefits, eligibility hints, complaint guidance)
- **Student scholarships** (discovery + eligibility checklist)
- **Health schemes** (overview + eligibility hints)
- **Groq AI agent mode** for free-text questions

It supports inbound payload normalization for:
- Meta WhatsApp Cloud API
- Twilio WhatsApp
- Gupshup

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export GROQ_API_KEY=your_key_here
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000/docs`.

## Example request

```json
{
  "provider": "twilio",
  "user_id": "student-42",
  "payload": { "Body": "hi" }
}
```

## Conversation flow

1. User says `hi` / `menu`.
2. Bot shows main menu:
   - PM-KISAN
   - Scholarships
   - Health schemes
   - Groq AI agent
3. Submenus return guidance cards or complaint flow prompts.
4. AI mode lets users ask natural-language questions; `menu` exits AI mode.

## Groq integration

- Uses OpenAI-compatible client with `base_url=https://api.groq.com/openai/v1`.
- Model defaults to `llama-3.1-8b-instant` (override via `GROQ_MODEL`).
- If `GROQ_API_KEY` is missing, bot returns a safe fallback message.

## Project docs

- Build/deployment plan: `docs/build_plan.md`
- Pricing/free-tier research notes: `docs/pricing_research.md`

## Important disclaimer

This assistant provides guidance, not legal or official determination.
Always cross-check final eligibility and complaint submission details with official government portals.
