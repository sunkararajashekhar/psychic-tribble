from app.providers import ChannelProvider, normalize_incoming_text


def test_provider_normalization():
    assert (
        normalize_incoming_text(
            ChannelProvider.whatsapp_cloud,
            {"entry": [{"changes": [{"value": {"messages": [{"text": {"body": "hello"}}]}}]}]},
        )
        == "hello"
    )
    assert normalize_incoming_text(ChannelProvider.twilio, {"Body": "hi"}) == "hi"
    assert normalize_incoming_text(ChannelProvider.gupshup, {"payload": {"text": "hey"}}) == "hey"
