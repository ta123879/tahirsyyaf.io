import re
from typing import Dict, Optional, Tuple

from config import get_settings

Settings = get_settings()


def _normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip().lower())


def parse_user_intent(text: str) -> Dict[str, Optional[str]]:
    """
    Very lightweight intent extraction.
    Returns dict with keys: type ('system'|'ai'), action ('open'|'close'|None), target (e.g., 'chrome'|None), raw
    Handles simple English and basic Urdu phrases:
      - open: "open", "launch", Urdu: "khol", "kholo", "khol do"
      - close: "close", "exit", Urdu: "band", "band kar do"
    """
    raw = text
    text = _normalize(text)

    # Map synonyms
    open_synonyms = ["open", "launch", "start", "run", "khol", "kholo", "khol do"]
    close_synonyms = ["close", "exit", "quit", "shutdown", "band", "band karo", "band kar do"]

    # Known targets
    known_apps = set((Settings.windows_apps if sys_platform_is_windows() else Settings.linux_apps).keys())
    aliases = {
        "google chrome": "chrome",
        "microsoft word": "word",
        "code": "vscode",
        "visual studio code": "vscode",
        "ms edge": "edge",
    }

    # Determine action
    action: Optional[str] = None
    for token in open_synonyms:
        if token in text:
            action = "open"
            break
    if action is None:
        for token in close_synonyms:
            if token in text:
                action = "close"
                break

    # Extract target (very naive)
    target: Optional[str] = None
    if action is not None:
        # Try alias match
        for alias, canonical in aliases.items():
            if alias in text:
                target = canonical
                break
        if target is None:
            # Try known app names
            for app in sorted(known_apps, key=len, reverse=True):
                if app in text:
                    target = app
                    break

    if action and target:
        return {"type": "system", "action": action, "target": target, "raw": raw}

    return {"type": "ai", "action": None, "target": None, "raw": raw}


def sys_platform_is_windows() -> bool:
    import sys
    return sys.platform.startswith("win")


# AI routing

def ask_ai(prompt: str, provider: Optional[str] = None) -> str:
    provider = (provider or ("groq" if Settings.use_groq_default else "openai")).lower()
    system_message = (
        "You are Jarvis, a helpful, concise AI assistant. "
        "User may speak mixed Urdu and English. Reply in clear, natural speech-ready sentences. "
        "Be brief when appropriate."
    )

    if provider == "groq" and Settings.groq_api_key:
        try:
            import groq  # type: ignore
            client = groq.Groq(api_key=Settings.groq_api_key)
            completion = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": prompt},
                ],
                temperature=0.5,
            )
            return completion.choices[0].message.content or ""
        except Exception as exc:
            return f"(AI error via Groq) {exc}"

    # Default: OpenAI
    if Settings.openai_api_key:
        try:
            from openai import OpenAI  # type: ignore
            client = OpenAI(api_key=Settings.openai_api_key)
            completion = client.chat.completions.create(
                model=Settings.openai_chat_model,
                messages=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": prompt},
                ],
                temperature=0.5,
            )
            return completion.choices[0].message.content or ""
        except Exception as exc:
            return f"(AI error via OpenAI) {exc}"

    return "AI provider not configured. Please set OPENAI_API_KEY or GROQ_API_KEY."