from enum import Enum
from fastapi import HTTPException


class ChannelProvider(str, Enum):
    whatsapp_cloud = "whatsapp_cloud"
    twilio = "twilio"
    gupshup = "gupshup"


def normalize_incoming_text(provider: ChannelProvider, payload: dict) -> str:
    """Extract inbound user message text from different provider payload shapes."""
    if provider == ChannelProvider.whatsapp_cloud:
        return (
            payload.get("entry", [{}])[0]
            .get("changes", [{}])[0]
            .get("value", {})
            .get("messages", [{}])[0]
            .get("text", {})
            .get("body", "")
        )

    if provider == ChannelProvider.twilio:
        return payload.get("Body", "")

    if provider == ChannelProvider.gupshup:
        return payload.get("payload", {}).get("text", "")

    raise HTTPException(status_code=400, detail="Unsupported provider")
