# Jarvis AI Assistant (Python)

Requirements:
- Python 3.10+
- API keys in environment: `OPENAI_API_KEY`, optional `GROQ_API_KEY`, optional `ELEVENLABS_API_KEY`
- Optional Porcupine Access Key: `PORCUPINE_ACCESS_KEY` and custom keyword path `WAKE_WORD_PATH`

Setup
1. Create venv and install deps:
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Export environment variables (or use a `.env` file):
```
export OPENAI_API_KEY=YOUR_KEY
# export GROQ_API_KEY=YOUR_GROQ_KEY
# export ELEVENLABS_API_KEY=YOUR_E11_KEY
# export PORCUPINE_ACCESS_KEY=YOUR_PV_KEY
# export WAKE_WORD_PATH=/absolute/path/to/jarvis_en_windows_v2_1_0.ppn
```

3. Run in text mode first to validate flow:
```
export TEXT_MODE=true
python main.py
```

4. Disable text mode and use wake word (Porcupine):
```
unset TEXT_MODE
python main.py
```

Notes
- On Windows, configure `windows_apps` in `config.py` for app mapping.
- For Linux, uses `pkill` for close.
- TTS defaults to ElevenLabs if API key is set; otherwise falls back to `pyttsx3`.
- STT uses OpenAI Whisper via API; set `LANGUAGE_HINT` to `auto`, `en`, or `ur`.