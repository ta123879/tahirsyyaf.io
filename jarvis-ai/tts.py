import io
import math
from typing import Optional

import numpy as np

from config import get_settings

Settings = get_settings()


def play_beep(frequency_hz: int = 880, duration_ms: int = 180, volume: float = 0.25):
    try:
        import simpleaudio as sa  # type: ignore
    except Exception:
        return
    sample_rate = 16000
    t = np.linspace(0, duration_ms / 1000.0, int(sample_rate * duration_ms / 1000.0), False)
    tone = np.sin(2 * math.pi * frequency_hz * t) * volume
    audio = (tone * 32767).astype(np.int16)
    sa.play_buffer(audio, 1, 2, sample_rate)


def speak(text: str, provider: Optional[str] = None):
    provider = (provider or Settings.tts_provider).lower()

    if provider == "elevenlabs" and Settings.elevenlabs_api_key:
        try:
            from elevenlabs import ElevenLabs  # type: ignore

            client = ElevenLabs(api_key=Settings.elevenlabs_api_key)
            # Request WAV to avoid external decoders
            audio_stream = client.text_to_speech.convert(
                voice_id=Settings.elevenlabs_voice_id,
                model_id="eleven_multilingual_v2",
                text=text,
                output_format="wav",
            )
            audio_bytes = b"".join(chunk for chunk in audio_stream if chunk)

            try:
                import simpleaudio as sa  # type: ignore
                import wave
                import tempfile

                with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
                    tmp.write(audio_bytes)
                    tmp.flush()
                    with wave.open(tmp.name, "rb") as wf:
                        audio_data = wf.readframes(wf.getnframes())
                        sa.play_buffer(audio_data, wf.getnchannels(), wf.getsampwidth(), wf.getframerate()).wait_done()
            except Exception:
                pass
            return
        except Exception:
            # Fallback to pyttsx3 below
            pass

    # Fallback: offline pyttsx3
    try:
        import pyttsx3  # type: ignore

        engine = pyttsx3.init()
        engine.setProperty("rate", 185)
        engine.setProperty("volume", 0.95)
        engine.say(text)
        engine.runAndWait()
    except Exception:
        # Last resort: print
        print(f"Jarvis: {text}")