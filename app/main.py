from collections import defaultdict
from typing import Dict

from fastapi import FastAPI
from pydantic import BaseModel

from app.groq_client import generate_with_groq
from app.menu import default_menu, render_menu, select_option
from app.providers import ChannelProvider, normalize_incoming_text
from app.schemes import COMPLAINT_CATEGORIES, SCHEMES, render_scheme_card

app = FastAPI(title="FastAPI Welfare Chatbot (WhatsApp-ready)")

user_state: Dict[str, str] = defaultdict(lambda: "root")
menu_root = default_menu()


class IncomingMessage(BaseModel):
    provider: ChannelProvider
    user_id: str
    payload: dict


def _render_complaint_menu() -> str:
    lines = ["Select complaint category:"]
    for code, label in COMPLAINT_CATEGORIES.items():
        lines.append(f"{code}) {label}")
    lines.append("Reply with the option number.")
    return "\n".join(lines)


@app.get("/")
def health() -> dict:
    return {"ok": True, "message": "Welfare chatbot API is running"}


@app.post("/chat/incoming")
def handle_incoming(message: IncomingMessage) -> dict:
    text = normalize_incoming_text(message.provider, message.payload).strip()
    lowered = text.lower()

    if lowered in {"hi", "hello", "menu", "start"}:
        user_state[message.user_id] = "root"
        return {"reply": render_menu(menu_root)}

    current = user_state[message.user_id]

    if current == "ai_agent":
        if lowered == "menu":
            user_state[message.user_id] = "root"
            return {"reply": render_menu(menu_root)}
        return {"reply": generate_with_groq(text)}

    if current == "pm_kisan_complaint_flow":
        category = COMPLAINT_CATEGORIES.get(text)
        if category:
            user_state[message.user_id] = "root"
            return {
                "reply": (
                    f"Complaint category selected: {category}.\n"
                    "Please gather Aadhaar, registered mobile number, bank details, and application reference. "
                    "File complaint via official PM-KISAN/state helpdesk channels.\n\n"
                    f"{render_menu(menu_root)}"
                )
            }
        return {"reply": "Invalid complaint option.\n" + _render_complaint_menu()}

    if current == "root":
        top = select_option(menu_root, text)
        if not top:
            return {"reply": "Invalid option.\n" + render_menu(menu_root)}

        if top.key == "ai_agent":
            user_state[message.user_id] = "ai_agent"
            return {
                "reply": "AI agent enabled (Groq). Ask your question, or type 'menu' to go back."
            }

        user_state[message.user_id] = top.key
        return {"reply": render_menu(top)}

    section = next((n for n in menu_root.children.values() if n.key == current), None)
    if section:
        selected = select_option(section, text)
        if not selected:
            return {"reply": f"Invalid option.\n{render_menu(section)}"}

        user_state[message.user_id] = "root"

        if selected.key.startswith("pm_kisan"):
            if selected.key == "pm_kisan_complaint":
                user_state[message.user_id] = "pm_kisan_complaint_flow"
                return {"reply": _render_complaint_menu()}
            return {"reply": render_scheme_card(SCHEMES["pm_kisan"]) + "\n\n" + render_menu(menu_root)}

        if selected.key.startswith("scholarships"):
            return {"reply": render_scheme_card(SCHEMES["scholarships"]) + "\n\n" + render_menu(menu_root)}

        if selected.key.startswith("health"):
            return {"reply": render_scheme_card(SCHEMES["health_schemes"]) + "\n\n" + render_menu(menu_root)}

    user_state[message.user_id] = "root"
    return {"reply": render_menu(menu_root)}
