import io
import time
import wave
from typing import Optional

import numpy as np

from config import get_settings

Settings = get_settings()


def _record_audio(seconds: int, sample_rate: int) -> bytes:
    """Record mono audio using sounddevice and return WAV bytes."""
    try:
        import sounddevice as sd  # type: ignore
    except Exception as exc:
        raise RuntimeError(f"Audio recording not available: {exc}")

    duration = max(1, int(seconds))
    num_frames = duration * sample_rate

    audio = sd.rec(frames=num_frames, samplerate=sample_rate, channels=1, dtype="float32")
    sd.wait()

    # Convert float32 [-1,1] to int16 and encode to WAV
    audio_int16 = np.clip(audio.flatten(), -1.0, 1.0)
    audio_int16 = (audio_int16 * 32767.0).astype(np.int16)

    buf = io.BytesIO()
    with wave.open(buf, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)  # 16-bit
        wf.setframerate(sample_rate)
        wf.writeframes(audio_int16.tobytes())
    return buf.getvalue()


def transcribe_wav_bytes(wav_bytes: bytes, language: Optional[str] = None) -> str:
    if not Settings.openai_api_key:
        return "Speech-to-text not configured. Please set OPENAI_API_KEY."

    try:
        from openai import OpenAI  # type: ignore
        client = OpenAI(api_key=Settings.openai_api_key)

        file_like = io.BytesIO(wav_bytes)
        file_like.name = "speech.wav"  # needed by some libs for mime-type
        args = {"model": Settings.stt_model, "file": file_like}
        if language and language not in {"auto", ""}:
            args["language"] = language
        result = client.audio.transcriptions.create(**args)
        # API returns an object with 'text'
        text = getattr(result, "text", None)
        if not text and isinstance(result, dict):
            text = result.get("text")
        return text or ""
    except Exception as exc:
        return f"(STT error) {exc}"


def capture_and_transcribe(seconds: Optional[int] = None) -> str:
    if Settings.text_mode:
        try:
            return input("You (type): ").strip()
        except EOFError:
            return ""

    sec = seconds if seconds is not None else Settings.record_seconds
    try:
        wav_bytes = _record_audio(sec, Settings.sample_rate)
    except Exception as exc:
        return f"(Audio capture error) {exc}"

    return transcribe_wav_bytes(wav_bytes, language=Settings.language_hint)