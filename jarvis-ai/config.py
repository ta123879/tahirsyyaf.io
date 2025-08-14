import os
from dataclasses import dataclass, field
from typing import Dict, Optional

try:
    from dotenv import load_dotenv  # type: ignore
    load_dotenv()
except Exception:
    pass


def _getenv_bool(name: str, default: bool = False) -> bool:
    value = os.getenv(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


@dataclass
class Settings:
    # API keys
    openai_api_key: str = field(default_factory=lambda: os.getenv("OPENAI_API_KEY", ""))
    groq_api_key: str = field(default_factory=lambda: os.getenv("GROQ_API_KEY", ""))
    elevenlabs_api_key: str = field(default_factory=lambda: os.getenv("ELEVENLABS_API_KEY", ""))
    porcupine_access_key: str = field(default_factory=lambda: os.getenv("PORCUPINE_ACCESS_KEY", ""))

    # Models and providers
    openai_chat_model: str = field(default_factory=lambda: os.getenv("OPENAI_CHAT_MODEL", "gpt-4o-mini"))
    stt_model: str = field(default_factory=lambda: os.getenv("OPENAI_TRANSCRIPTION_MODEL", "whisper-1"))
    tts_provider: str = field(default_factory=lambda: os.getenv("TTS_PROVIDER", "elevenlabs"))  # elevenlabs|coqui|pyttsx3

    # TTS settings
    elevenlabs_voice_id: str = field(default_factory=lambda: os.getenv("ELEVENLABS_VOICE_ID", "21m00Tcm4TlvDq8ikWAM"))

    # Wake word
    wake_word_keyword: str = field(default_factory=lambda: os.getenv("WAKE_WORD_KEYWORD", "porcupine"))
    wake_word_path: str = field(default_factory=lambda: os.getenv("WAKE_WORD_PATH", ""))  # .ppn path for custom keyword like Jarvis

    # Audio
    language_hint: str = field(default_factory=lambda: os.getenv("LANGUAGE_HINT", "auto"))  # e.g., "auto", "ur", "en"
    sample_rate: int = int(os.getenv("AUDIO_SAMPLE_RATE", "16000"))
    record_seconds: int = int(os.getenv("RECORD_SECONDS", "6"))

    # Behavior toggles
    verbose: bool = _getenv_bool("VERBOSE", False)
    text_mode: bool = _getenv_bool("TEXT_MODE", False)
    use_groq_default: bool = _getenv_bool("USE_GROQ", False)

    # Platform
    platform: str = field(default_factory=lambda: os.getenv("JARVIS_PLATFORM", os.name))

    # App maps
    windows_apps: Dict[str, str] = field(default_factory=lambda: {
        "chrome": "chrome.exe",
        "word": "WINWORD.EXE",
        "notepad": "notepad.exe",
        "vscode": "Code.exe",
        "edge": "msedge.exe",
        "spotify": "Spotify.exe",
    })
    linux_apps: Dict[str, str] = field(default_factory=lambda: {
        "chrome": "google-chrome",
        "firefox": "firefox",
        "vscode": "code",
        "gedit": "gedit",
        "spotify": "spotify",
    })


_settings: Optional[Settings] = None


def get_settings() -> Settings:
    global _settings
    if _settings is None:
        _settings = Settings()
    return _settings