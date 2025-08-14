from typing import Optional

from config import get_settings

Settings = get_settings()


class WakeWordDetector:
    def __init__(self):
        self._porcupine = None
        self._recorder = None
        self._ok = False

        if Settings.text_mode:
            self._ok = True
            return

        try:
            import pvporcupine  # type: ignore
            from pvrecorder import PvRecorder  # type: ignore

            if Settings.wake_word_path:
                self._porcupine = pvporcupine.create(
                    access_key=Settings.porcupine_access_key,
                    keyword_paths=[Settings.wake_word_path],
                )
            else:
                # Use built-in keyword ("porcupine" is always available). Custom "Jarvis" requires a PPN.
                self._porcupine = pvporcupine.create(
                    access_key=Settings.porcupine_access_key,
                    keywords=[Settings.wake_word_keyword],
                )
            self._recorder = PvRecorder(device_index=-1, frame_length=self._porcupine.frame_length)
            self._ok = True
        except Exception:
            # Fallback: will use text prompt
            self._ok = True

    def start(self):
        if Settings.text_mode:
            return
        if self._recorder is not None:
            try:
                self._recorder.start()
            except Exception:
                pass

    def stop(self):
        try:
            if self._recorder is not None:
                self._recorder.stop()
                self._recorder.delete()
            if self._porcupine is not None:
                self._porcupine.delete()
        except Exception:
            pass

    def wait_for_wake(self) -> bool:
        """Blocks until wake word detected or text-mode confirmation."""
        if not self._ok:
            return False

        if Settings.text_mode:
            try:
                _ = input("Say 'Jarvis' (press Enter to simulate): ")
                return True
            except EOFError:
                return False

        if self._porcupine is None or self._recorder is None:
            return False

        try:
            while True:
                pcm = self._recorder.read()
                result = self._porcupine.process(pcm)
                if result >= 0:
                    return True
        except KeyboardInterrupt:
            return False
        except Exception:
            return False