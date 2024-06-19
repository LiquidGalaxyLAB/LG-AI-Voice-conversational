# model_config.py

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
    "google_cloud_wavenet": {
        "required": ["text", "languageCode", "model", "audioEncoding"],
        "optional": ["name", "ssmlGender", "customVoice", "reportedUsage", "speakingRate", "pitch", "volumeGainDb", "sampleRateHertz"]
    },
    "deepgram_tts": {
        "required": ["inputText", "voice", "audioConfig"],
        "optional": ["sampleRateHertz", "effectsProfileId"]
    },
    "elevenlabs_tts": {
        "required": ["inputText", "voice", "audioConfig"],
        "optional": ["sampleRateHertz", "effectsProfileId"]
    },
    "chat_tts": {
        "required": ["inputText", "voice", "audioConfig"],
        "optional": ["sampleRateHertz", "effectsProfileId"]
    },
    "bark_tts": {
        "required": [],
        "optional": []
    }
}
