MODEL_CONFIGS = {
    # Speech-to-text
    "google_cloud_stt": {
        "required": ["model", "audio"],
        "optional": []
    },
    "deepgram_stt": {
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
    "chat_tts": {
        "required": ["model", "content"],
        "optional": []
    },
    "bark_tts": {
        "required": ["model", "content"],
        "optional": []
    },
    # Groq
    "groq": {
        "required": ["model", "content"]
    }
}
