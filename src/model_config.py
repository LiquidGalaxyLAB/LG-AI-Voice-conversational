MODEL_CONFIGS = {
    # Speech-to-text
    "google_cloud_stt": {
        "required": ["model", "audio"],
        "optional": ["google_model", "use_enhanced"]
    },
    "deepgram_stt": {
        "required": ["model", "audio"],
        "optional": ["deepgram_model", "tier"] 
    },
    "assemblyai_stt": {
        "required": ["model", "audio"],
        "optional": []
    },
    # Text-to-speech
    "google_cloud_tts": {
        "required": ["model", "content"],
        "optional": ["language_code", "name", "speaking_rate", "pitch", "volume_gain_db", "sample_rate_hertz"]
    },
    "deepgram_tts": {
        "required": ["model", "content"],
        "optional": ["voice"]
    },
    "elevenlabs_tts": {
        "required": ["model", "content"],
        "optional": ["voice_id", "model_id", "latency", "stability", "similarity", "style", "use_speaker_boost"]
    },
    # Groq
    "groq": {
        "required": ["model", "content"]
    }
}
