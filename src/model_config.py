MODEL_CONFIGS = {
    # Speech-to-text
    "google_cloud_gemini": {
        "required": ["encoding", "sampleRateHertz", "languageCode", "content"],
        "optional": ["maxAlternatives", "profanityFilter", "speechContext"]
    },
    "deepgram_stt": {
        "required": [],
        "optional": ["callback", "callback_method", "custom_topic", "custom_topic_mode", "diarize", "diarize_version", "dictation", "detect_entities", "detect_language", "detect_topics", "extra", "filler_words", "intents", "keywords", "language", "measurements", "model", "multichannel", "numerals", "paragraphs", "profanity_filter", "punctuate", "redact", "replace", "smart_format", "search", "sentiment", "summarize", "tag", "topics", "utterances", "utt_split", "version"] 
    },
    # Text-to-speech
    "google_cloud_tts": {
        "required": ["model", "content"],
        "optional": ["name", "ssmlGender", "customVoice", "reportedUsage", "speakingRate", "pitch", "volumeGainDb", "sampleRateHertz"]
    },
    "deepgram_tts": {
        "required": ["model", "content"],
        "optional": []
    },
    "elevenlabs_tts": {
        "required": ["model", "content"],
        "optional": []
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
