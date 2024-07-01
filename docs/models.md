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

https://developers.deepgram.com/docs/tts-models

|        Parameters       |       Required/Optional      |                             Values                               |
| :---------------------: | :--------------------------: | :--------------------------------------------------------------: |
|          model          |           Required           |  |
|         content         |           Required           |               The text to be converted to speech                 |
|          voice          |           Optional           |      The voice model for the audio (default: aura-asteria-en)    |
|        language         |           Optional           | Specifies the language of the speech (default: ) |
|         diarize         |           Optional           | Recognize speaker changes. Each word in transcript will be assigned a speaker number starting at 0. (Default false)          |
|      diarize_version    |           Optional           | Number of alternadiarize_version |
|        dictation        |           Optional           | Spoken dictation commands will be converted to punctuation marks. e.g., comma to , (Default false) |
|     detect_entities     |           Optional           | Entity Detection identifies and extracts key entities from content in submitted audio (Default false) |



## Text-to-speech


### Google Cloud AI with WaveNet TTS

The Google Cloud AI's text-to-speech API allows users to input text and get back an audio file in response, providing natural-sounding audio which can be customizable with options such as language, gender, and accent for all users to use the app. WaveNet was one of the first text-to-speech models that sounded natural-sounding speech, starting at Google Deepmind. The pricing is very feasible for our use cases, as the WaveNet model's usage is free of charge for every 1 million characters per month.

More details and official documentation can be found [here](https://cloud.google.com/text-to-speech/docs/basics).

|        Parameters       |       Required/Optional      |                                                                  Values                                                                    | Value Type |
| :---------------------: | :--------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------: | :---------:|
|          model          |           Required           |                                                            "google_cloud_tts"                                                              |   String   |
|         content         |           Required           |                                                      The raw text to be transcribed                                                        |   String   |
|       languageCode      |           Optional           |                     The language (and potentially also the region) of the voice expressed as a BCP-47 language tag                         |   String   |
|          name           |           Optional           |      The name of the voice. If not set, the service will choose a voice based on the other parameters such as languageCode and gender      |   String   |
|       speakingRate      |           Optional           |                                               Speaking rate/speed, in the range [0.25, 4.0]                                                |   Float    |
|          pitch          |           Optional           |                                                 Speaking pitch, in the range [-20.0, 20.0]                                                 |   Float    |
|      volume_gain_db     |           Optional           |                   Volume gain (in dB) of the normal native volume supported by the specific voice, in the range [-96.0, 16.0]              |   Float    |
|     sampleRateHertz     |           Optional           |                                             The synthesis sample rate (in hertz) for this audio                                            |   Float    |


### ElevenLabs TTS

This API generates an MP3 file from text in 29 languages, which can be customized to provide accessibility to as many users in the world as we can. With its very low latency of approximately 400ms using the Turbo model, this API can provide fast results so users don't have a large delay when waiting for a response back from the app combined with Groq's LPU. The feature provides a free tier allowing up to 10,000 characters per month, which may be too little considering we have users from around the world who may use our app. The pricing isn't too cheap considering other options, but the multi-language feature is appealing to allow everyone to use the app.

The complete list of voice selections can be found [here](https://elevenlabs.io/docs/voices/premade-voices#current-premade-voices).

The complete list of model selections can be found [here](https://help.elevenlabs.io/hc/en-us/articles/17883183930129-What-models-do-you-offer-and-what-is-the-difference-between-them).

|        Parameters          |       Required/Optional      |                                       Values                                 | Value Type |
| :------------------------: | :--------------------------: | :--------------------------------------------------------------------------: | :---------:|
|           model            |           Required           |                                  "elevenlabs_tts"                            |   String   |
|          content           |           Required           |                         The text to be converted to speech                   |   String   |
|         voice_id           |           Optional           |                                 Voice ID to be used                          |   String   |
|         model_id           |           Optional           |                     Identifier of the model that will be used                |   String   |
|         latency            |           Optional           |                       Latency optimizations at cost of quality               |   String   |
|        stability           |           Optional           |                          Adjusts the stability of the voice                  |   Float    |
|        similarity          |           Optional           |                     Enhances the similarity to the target voice              |   Float    |
|          style             |           Optional           |                      Modifies the speaking style of the voice                |   Float    |
|     use_speaker_boost      |           Optional           |  Enhances the voice to make it sound more like the speaker from the training | True/False |


### Deepgram TTS

Deepgram's text-to-speech feature is the cheapest by far with credits given with every new account. The cost to maintain the app using Deepgram's API is very low while providing very high-quality transcriptions. The speed of the application is very quick compared to other services and is 30% more accurate than other services on average, leading the market across use-case categories. There is a variety of voices we can use for Deepgram, allowing contributors to freely customize the experience of the app.

The complete list of voice selections can be found [here](https://developers.deepgram.com/docs/tts-models).

|        Parameters       |       Required/Optional      |                             Values                               | Value Type |
| :---------------------: | :--------------------------: | :--------------------------------------------------------------: | :---------:|
|          model          |           Required           |                         "deepgram_tts"                           |   String   |
|         content         |           Required           |               The text to be converted to speech                 |   String   |
|          voice          |           Optional           |                  The voice model for the audio                   |   String   |


### ChatTTS

ChatTTS offers several benefits, including multi-language support, making it accessible to a wide range of users. Its extensive training on approximately 10 million hours of Chinese and English data results in high-quality, natural-sounding voice synthesis. ChatTTS is well-suited for dialog tasks typically managed by LLMs, providing fluid conversations for various applications and services.

The project team plans to open source a trained base model, enabling academic researchers and developers to further study and develop the technology. Additionally, the team is focused on enhancing the model's controllability, adding watermarks, and integrating it with LLMs to ensure safety and reliability. ChatTTS offers ease of use by requiring only text input to generate corresponding voice files, making it a convenient solution for voice synthesis.


### Bark TTS

Bark is a text-to-speech model by Suno AI, which will be used as the final layer in the application's process to help us voice the story generated by our LLM model to the tablet so users can listen to it. Not only does this provide accessibility features so everyone can enjoy the application, but it is also a way to integrate the latest growth of AI into Liquid Galaxy applications one step at a time.

Used in mentor Vedant's GSoC project from last year (Voice CMS), Bark can take text and generate a voice to read the given input. Bark's API processes the given text and produces a WAV file, which will be opened automatically on the local devices to initiate the narration upon generation of the audio file.

|        Parameters       |       Required/Optional      |                             Values                               | Value Type |
| :---------------------: | :--------------------------: | :--------------------------------------------------------------: | :---------:|
|          model          |           Required           |                           "bark_tts"                             |   String   |
|         content         |           Required           |               The text to be converted to speech                 |   String   |