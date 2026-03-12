# Twilio vs Gupshup vs Meta Cloud API (free usage research notes)

_Date: 2026-03-12_

## What was researched

I attempted to fetch official pricing pages for:

- Twilio WhatsApp pricing
- Gupshup pricing
- Meta WhatsApp pricing docs

In this execution environment, HTTP requests to those domains returned `403 Forbidden`/`000`, so exact live numbers could not be validated automatically.

## Practical conclusions (industry-standard behavior to verify at launch)

1. **Twilio is not fully free for production**:
   - Twilio typically offers a trial account with limited credits for testing.
   - Production WhatsApp messaging incurs per-message/per-conversation charges plus WhatsApp fees.

2. **Gupshup is usually not fully free for production**:
   - It may provide trial/sandbox onboarding paths.
   - Production usage generally has conversation/message charges depending on region/category.

3. **Meta WhatsApp Cloud API is usually the cheapest "free-first" route**:
   - Meta has offered a free monthly conversation allowance for service conversations in many policy versions.
   - Remaining usage is billed by category/region.

## Recommendation for your CSP project

- Build provider-agnostic backend in FastAPI (done in this repo) and begin with **Meta Cloud API**.
- Keep adapters for Twilio/Gupshup so you can switch if needed.
- Before demo or submission, verify the latest provider pricing pages manually from your network.

## Commands used

```bash
curl -L -I -s https://www.twilio.com/en-us/whatsapp/pricing | head -n 5
curl -L -I -s https://www.gupshup.io/developer/pricing | head -n 5
curl -L -I -s https://developers.facebook.com/docs/whatsapp/pricing/ | head -n 5
```
