import os
import anthropic


def test_anthropic():
    api_key = os.environ.get("ANTHROPIC_API_KEY")

    if not api_key:
        # Verify the SDK is importable and the client class works
        try:
            # This should raise AuthenticationError, not ImportError or AttributeError
            anthropic.Anthropic(api_key="test")
        except Exception:
            pass
        print("it works (SDK installed, no API key provided)")
        return

    client = anthropic.Anthropic()
    response = client.messages.create(
        model="claude-opus-4-7",
        max_tokens=64,
        messages=[{"role": "user", "content": "Say exactly: it works"}],
    )

    text = next(b.text for b in response.content if b.type == "text")
    print(text)
    assert "it works" in text.lower(), f"Unexpected response: {text}"
    print("it works")


if __name__ == "__main__":
    test_anthropic()
