from fastapi.testclient import TestClient

from app.main import app
from app.menu import default_menu, render_menu, select_option


client = TestClient(app)


def test_render_menu_contains_new_options():
    menu = default_menu()
    text = render_menu(menu)
    assert "1) PM-KISAN: benefits, eligibility, complaints" in text
    assert "4) Ask Groq AI agent" in text


def test_select_option_valid_and_invalid():
    menu = default_menu()
    assert select_option(menu, "1").key == "pm_kisan"
    assert select_option(menu, "9") is None


def test_chat_flow_menu_and_submenu():
    payload = {"provider": "twilio", "user_id": "u1", "payload": {"Body": "hi"}}
    response = client.post("/chat/incoming", json=payload)
    assert response.status_code == 200
    assert "Main Menu" in response.json()["reply"]

    pick = {"provider": "twilio", "user_id": "u1", "payload": {"Body": "1"}}
    response = client.post("/chat/incoming", json=pick)
    assert "PM-KISAN" in response.json()["reply"]


def test_ai_mode_without_key_returns_fallback():
    client.post("/chat/incoming", json={"provider": "twilio", "user_id": "u2", "payload": {"Body": "hi"}})
    client.post("/chat/incoming", json={"provider": "twilio", "user_id": "u2", "payload": {"Body": "4"}})
    response = client.post(
        "/chat/incoming", json={"provider": "twilio", "user_id": "u2", "payload": {"Body": "am i eligible"}}
    )
    assert "GROQ_API_KEY is not configured" in response.json()["reply"]
