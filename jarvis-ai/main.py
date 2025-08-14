import sys
from typing import Optional

from config import get_settings
from wake_word import WakeWordDetector
from stt import capture_and_transcribe
from nlp import parse_user_intent, ask_ai
from system_control import open_app, close_app
from tts import speak, play_beep


def run_once() -> None:
    settings = get_settings()

    if settings.text_mode:
        print("[Text Mode] Type your query. Type 'exit' to quit.")
        while True:
            user = capture_and_transcribe()
            if not user:
                continue
            if user.lower() in {"exit", "quit"}:
                break
            intent = parse_user_intent(user)
            if intent["type"] == "system" and intent["action"] and intent["target"]:
                if intent["action"] == "open":
                    ok, msg = open_app(intent["target"])  # type: ignore
                else:
                    ok, msg = close_app(intent["target"])  # type: ignore
                print(msg)
                speak(msg)
            else:
                response = ask_ai(intent["raw"])  # type: ignore
                print(f"Jarvis: {response}")
                speak(response)
        return

    detector = WakeWordDetector()
    detector.start()

    print("Jarvis is listening... Say the wake word.")
    try:
        while True:
            woke = detector.wait_for_wake()
            if not woke:
                break
            play_beep()
            print("Listening for your command...")
            user = capture_and_transcribe()
            if not user:
                continue
            print(f"You: {user}")

            intent = parse_user_intent(user)
            if intent["type"] == "system" and intent["action"] and intent["target"]:
                if intent["action"] == "open":
                    ok, msg = open_app(intent["target"])  # type: ignore
                else:
                    ok, msg = close_app(intent["target"])  # type: ignore
                print(msg)
                speak(msg)
            else:
                response = ask_ai(intent["raw"])  # type: ignore
                print(f"Jarvis: {response}")
                speak(response)
            print("(Back to idle listening)")
    except KeyboardInterrupt:
        pass
    finally:
        detector.stop()


if __name__ == "__main__":
    run_once()