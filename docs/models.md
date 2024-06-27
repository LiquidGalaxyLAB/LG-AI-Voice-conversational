# Descriptions of AI Models

## Speech-to-text

### Google Cloud AI Speech-to-Text with Gemini

Google provides a speech-to-text model API providing up to 60 minutes of transcribing audio per month using the Google Gemini model. The advanced speech AI utilizes Chirp, Google Cloud's foundation model for speech trained on a massive amount of data. Supporting 125 languages, the trained model has recognition and transcription for more spoken languages and accents which can assist many different users across the world. Providing three methods to perform this feature: synchronous, asynchronous, and streaming. Each method returns text results for post-processing, periodically, or in real-time to better suit a user's needs.

All Speech-to-Text API synchronous recognition requests must include a speech recognition config field (of type RecognitionConfig). A RecognitionConfig contains the following sub-fields as shown in the table below.

More details and official documentation can be found [here](https://cloud.google.com/speech-to-text/docs/speech-to-text-requests#synchronous-requests).

|        Parameters       |       Required/Optional      |                             Values                               |
| :---------------------: | :--------------------------: | :--------------------------------------------------------------: |
|         content         |           Required           |                  Audio to evaluate (Max 1 min)                   |
|           uri           |           Required           |                    URI for the audio content                     |
|         encoding        |           Required           |             Encoding scheme of the supplied audio                |
|      sampleRateHertz    |           Required           |          Sample rate (in Hertz) of the supplied audio            |
|       languageCode      |           Required           |          Language + Region/Locale (BCP-47 identifier)            |
|      maxAlternatives    |           Optional           |    Number of alternative transcriptions in response (default 1)  |
|      profanityFilter    |           Optional           |              Whether to filter out profane words                 |
|       speechContext     |           Optional           | Contains additional contextual information for processing audio. |


### Deepgram Speech-to-Text

Deepgram has an accurate (22% lower word error rate) API that is fast and many times cheaper than Vapi AI's services. On top of the cheap prices, Deepgram gives every new account $200 in credits, with the cheapest rate costing $0.0020/min and the most expensive costing $0.0145/min, the credits can last for 13,793 to 100,000 minutes of recording usage. If this is approved by the admins of the organization, I would need to test various models out on my own time to check for their accuracy to integrate into my app. Deepgram's voice-to-text is vastly faster than other services, being able to live-transcribe and transcribe one hour of audio in twelve seconds.

More details and official documentation can be found [here](https://developers.deepgram.com/reference/listen-file).

|        Parameters       |       Required/Optional      |                             Values                               |
| :---------------------: | :--------------------------: | :--------------------------------------------------------------: |
|         callback        |           Optional           | Callback URL to provide if you would like your submitted audio to be processed asynchronously                 |
|      callback_method    |           Optional           |                    Enable a callback method (Default false) |
|       custom_topic      |           Optional           | Custom topic you want the model to detect within your input audio if present (upto 100) |
|     custom_topic_mode   |           Optional           | When `strict`, model will only return topics submitted using the `custom_topic` param. When `extended`, the model will return its own detected topics in addition to those submitted using the custom_topic param (Default extended) |
|         diarize         |           Optional           | Recognize speaker changes. Each word in transcript will be assigned a speaker number starting at 0. (Default false)          |
|      diarize_version    |           Optional           | Number of alternadiarize_version |
|        dictation        |           Optional           | Spoken dictation commands will be converted to punctuation marks. e.g., comma to , (Default false) |
|     detect_entities     |           Optional           | Entity Detection identifies and extracts key entities from content in submitted audio (Default false) |
|     detect_language     |           Optional           | Detect the language of the provided audio (Default false) |
|      detect_topics      |           Optional           | Identify and extract key topics (Default false) |
|          extra          |           Optional           | To add an extra parameter in the query string and pass a key-value pair you would like to include in the response |
|       filler_words      |           Optional           | Whether to include words like "uh" and "um" in transcription output (Default false) |
|         intents         |           Optional           | Recognizes speaker intent throughout an entire transcript. Returns a list of text segments and the intents found within each segment |
|        keywords         |           Optional           | Uncommon proper nouns or other words to transcribe that are not a part of the model's vocabulary |
|        language         |           Optional           | The BCP-47 language tag that hints at the primary spoken language (Default en) |
|         model           |           Optional           | Spoken measurements will be converted to their corresponding abbreviations. e.g., milligram to mg (Default false) |
|      multichannel       |           Optional           | Transcribe each audio channel independently (Default false) |
|        numerals         |           Optional           | Convert numbers from written format (e.g., one) to numerical format (e.g., 1) (Default false) |
|       paragraphs        |           Optional           | Split audio into paragraphs (Default false) |
|    profanity_filter     |           Optional           | Split audio inRemove profanity from the transcript (Default false) |
|       punctuate         |           Optional           | Add punctuation and capitalization to the transcript (Default false) |
|        redact           |           Optional           | Redact sensitive information, replacing redacted content with asterisks (*). Can send multiple instances in query string (Default false) |
|        replace          |           Optional           | Terms or phrases to search for in the submitted audio and replace. Can send multiple instances in query string |
|      smart_format       |           Optional           | Apply formatting to transcript output. When set to true, additional formatting will be applied to transcripts to improve readability. (Default false) |
|        search           |           Optional           | Terms or phrases to search for in the submitted audio. Can send multiple instances in query string |
|       sentiment         |           Optional           | Recognizes the sentiment of the entire transcript and detects a shift in sentiment throughout the transcript. Returns a list of text segments and the sentiment found within each segment |
|       summarize         |           Optional           | Summarize content (Default v2) |
|         tag             |           Optional           | Tag to associate with the request |
|        topics           |           Optional           | Detects topics throughout an entire transcript. Returns a list of text segments and the topics found within each segment |
|      utterances         |           Optional           | Segment speech into meaningful units based on gaps in speech (Default false) |
|      utt_split          |           Optional           | Length of time in seconds used to split utterances (Default 0.8) |
|       version           |           Optional           | Version of the model to use (Default latest) |


## Text-to-speech

### Google Cloud AI with WaveNet

The Google Cloud AI's text-to-speech API allows users to input text and get back an audio file in response, providing natural-sounding audio which can be customizable with options such as language, gender, and accent for all users to use the app. WaveNet was one of the first text-to-speech models that sounded natural-sounding speech, starting at Google Deepmind. The pricing is very feasible for our use cases, as the WaveNet model's usage is free of charge for every 1 million characters per month.

More details and official documentation can be found [here](https://cloud.google.com/text-to-speech/docs/basics).


|        Parameters       |       Required/Optional      |                                                                  Values                                                                    |
| :---------------------: | :--------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------: |
|          text           |           Required           |                                                      The raw text to be transcribed                                                        |
|       languageCode      |           Required           |                     The language (and potentially also the region) of the voice expressed as a BCP-47 language tag                         |
|          model          |           Required           |                                        The name of the AutoML model that synthesizes the custom voice                                      |
|      audioEncoding	    |           Required           |                                                   The format of the audio byte stream                                                      |
|          name           |           Optional           |      The name of the voice. If not set, the service will choose a voice based on the other parameters such as languageCode and gender      |
|       ssmlGender        |           Optional           | The preferred gender of the voice. If not set, the service will choose a voice based on the other parameters such as languageCode and name |
|       customVoice       |           Optional           |        The configuration for a custom voice. If set, the service will choose the custom voice matching the specified configuration         |
|      reportedUsage      |           Optional           |                                         The usage of the synthesized audio to be reported                                                  |
|       speakingRate      |           Optional           |                                               Speaking rate/speed, in the range [0.25, 4.0]                                                |
|          pitch          |           Optional           |                                                 Speaking pitch, in the range [-20.0, 20.0]                                                 |
|       volumeGainD       |           Optional           |                   Volume gain (in dB) of the normal native volume supported by the specific voice, in the range [-96.0, 16.0]              |
|     sampleRateHertz     |           Optional           |                                             The synthesis sample rate (in hertz) for this audio                                            |

### llElevenLabs

This API generates an MP3 file from text in 29 languages, which can be customized to provide accessibility to as many users in the world as we can. With its very low latency of approximately 400ms using the Turbo model, this API can provide fast results so users don't have a large delay when waiting for a response back from the app combined with Groq's LPU. The feature provides a free tier allowing up to 10,000 characters per month, which may be too little considering we have users from around the world who may use our app. The pricing isn't too cheap considering other options, but the multi-language feature is appealing to allow everyone to use the app.

More details and official documentation can be found [here](https://elevenlabs.io/docs/api-reference/text-to-speech).

|        Parameters          |       Required/Optional      |                                                                  Values                                                                    |
| :------------------------: | :--------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------: |
|           text             |           Required           |                                                 The text that will get converted into speech.                                              |
|         voice_id           |           Required           |                                                            Voice ID to be used                                                             |
|      enable_logging        |           Optional           |                               Full privacy mode will be used for the request when set to false (detault true)                              |
| optimize_streaming_latency |           Optional           |                                  The name of the AutoML model that synthesizes the custom voice (default 0)                                |
|       output_format	       |           Optional           |                                           Output format of the generated audio (default mp3_44100_128)                                     |
|         model_id           |           Optional           |                                      Identifier of the model that will be used (default eleven_monolingual_v1)                             |
|      voice_settings        |           Optional           |                                         Voice settings overriding stored setttings for the given voice                                     |
|  pronunciation_dictionary_locators |           Optional           |       A list of pronunciation dictionary locators (id, version_id) to be applied to the text        |
|      seed         |           Optional           |                                         sample deterministically                                                 |
|       previous_text         |           Optional           |                                      The text that came before the text of the current request                                              |
|          next_text         |           Optional           |                                            next_text                                     |
|    previous_request_ids          |           Optional           |         A list of request_id of the samples that were generated before this generation             |
|     next_request_ids        |           Optional           |                    A list of request_id of the samples that were generated before this generation                                        |

### Deepgram

Deepgram's text-to-speech feature is the cheapest by far, costing $0.0150 for characters with $200 given in credits with every new account, the cost to maintain the app using Deepgram's API is very low while providing very high-quality transcriptions. The speed of the application is very quick compared to other services and is 30% more accurate than other services on average, leading the market across use-case categories.

### ChatTTS

ChatTTS offers several benefits, including multi-language support, making it accessible to a wide range of users. Its extensive training on approximately 10 million hours of Chinese and English data results in high-quality, natural-sounding voice synthesis. ChatTTS is well-suited for dialog tasks typically managed by LLMs, providing fluid conversations for various applications and services.

The project team plans to open source a trained base model, enabling academic researchers and developers to further study and develop the technology. Additionally, the team is focused on enhancing the model's controllability, adding watermarks, and integrating it with LLMs to ensure safety and reliability. ChatTTS offers ease of use by requiring only text input to generate corresponding voice files, making it a convenient solution for voice synthesis.

### Bark

Bark is a text-to-speech model by Suno AI, which will be used as the final layer in the application's process to help us voice the story generated by our LLM model to the tablet so users can listen to it. Not only does this provide accessibility features so everyone can enjoy the application, but it is also a way to integrate the latest growth of AI into Liquid Galaxy applications one step at a time.

Used in mentor Vedant's GSoC project from last year (Voice CMS), Bark can take text and generate a voice to read the given input, as well as create other audio, such as background music or sound effects which could make this application have a more Liquid Galaxy immersive experience. Focusing on the main portion which is the generated story, we will display the story on a slave machine for the user to be able to read and it will also be read out loud through the tablet. Bark's API processes the given text and produces a WAV file, which will be opened automatically on the local devices to initiate the narration upon generation of the audio file.