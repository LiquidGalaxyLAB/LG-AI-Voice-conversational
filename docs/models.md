# Descriptions of AI Models

## Speech-to-text

### Google Cloud AI Speech-to-Text with Gemini

Google provides a speech-to-text model API providing up to 60 minutes of transcribing audio per month using the Google Gemini model. The advanced speech AI utilizes Chirp, Google Cloud's foundation model for speech trained on a massive amount of data. With up to 60 minutes of free transcribing of audio per month, allowing users to have minimal barriers when using the API.

More details and official documentation can be found [here](https://cloud.google.com/speech-to-text/docs/speech-to-text-requests#synchronous-requests).

|        Parameters          |       Required/Optional      |                                       Values                                 | Value Type |
| :------------------------: | :--------------------------: | :--------------------------------------------------------------------------: | :---------:|
|           model            |           Required           |                                  "google_cloud_stt"                          |   String   |
|           audio            |           Required           |                         The text to be converted to speech                   |    File    |
|        google_model        |           Optional           |                           Model to use for transcribing                      |   String   |
|        use_enhanced        |           Optional           |                  Whether to use an enhanced model for transcription          |   Boolean  |


### Deepgram Speech-to-Text

Deepgram has an accurate (22% lower word error rate) API that is fast and many times cheaper than Vapi AI's services. On top of the cheap prices, Deepgram gives every new account $200 in credits, lastint up to 100,000 minutes of recording usage. Deepgram's voice-to-text is vastly faster than other services, being able to transcribe one hour of audio in twelve seconds.

More details and official documentation can be found [here](https://developers.deepgram.com/docs/tts-models)

|        Parameters          |       Required/Optional      |                                       Values                                 | Value Type |
| :------------------------: | :--------------------------: | :--------------------------------------------------------------------------: | :---------:|
|           model            |           Required           |                                   "deepgram_stt"                             |   String   |
|           audio            |           Required           |                         The text to be converted to speech                   |    File    |
|       deepgram_model       |           Optional           |                           Model to use for transcribing                      |   String   |
|           tier             |           Optional           |              The tier of the model to use, such as "enhanced" or "base"      |   Boolean  |


### AssemblyAI Speech-to-Text

AssemblyAI's speech-to-text models have the industry’s lowest Word Error Rate (WER), providing an accuracy rate of 92.5%+ resulting from 12.5 million hours of training data.

|        Parameters          |       Required/Optional      |                                       Values                                 | Value Type |
| :------------------------: | :--------------------------: | :--------------------------------------------------------------------------: | :---------:|
|           model            |           Required           |                                  "assemblyai_stt"                            |   String   |
|           audio            |           Required           |                         The text to be converted to speech                   |    File    |


## Text-to-speech


### Google Cloud AI with WaveNet TTS

The Google Cloud AI's text-to-speech API allows users to input text and get back an audio file in response, providing natural-sounding audio which can be customizable with options such as language, gender, and accent for all users to use the app. WaveNet was one of the first text-to-speech models that sounded natural-sounding speech, starting at Google Deepmind. The WaveNet model usage is free of charge for every 1 million characters per month.

More details and official documentation can be found [here](https://cloud.google.com/text-to-speech/docs/basics).

|        Parameters       |       Required/Optional      |                                                                  Values                                                                    | Value Type |
| :---------------------: | :--------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------: | :---------:|
|          model          |           Required           |                                                            "google_cloud_tts"                                                              |   String   |
|         content         |           Required           |                                                      The raw text to be transcribed                                                        |   String   |
|       language_code     |           Optional           |                     The language (and potentially also the region) of the voice expressed as a BCP-47 language tag                         |   String   |
|          name           |           Optional           |      The name of the voice. If not set, the service will choose a voice based on the other parameters such as languageCode and gender      |   String   |
|       speaking_rate     |           Optional           |                                               Speaking rate/speed, in the range [0.25, 4.0]                                                |   Float    |
|          pitch          |           Optional           |                                                 Speaking pitch, in the range [-20.0, 20.0]                                                 |   Float    |
|      volume_gain_db     |           Optional           |                   Volume gain (in dB) of the normal native volume supported by the specific voice, in the range [-96.0, 16.0]              |   Float    |
|     sample_rate_hertz   |           Optional           |                                             The synthesis sample rate (in hertz) for this audio                                            |   Float    |


### ElevenLabs TTS

With its very low latency of approximately 400ms using the Turbo model, this API can provide fast results so users don't have a large delay when using our applications. ElevenLabs provides a free tier allowing up to 10,000 characters per month.

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
|     use_speaker_boost      |           Optional           |  Enhances the voice to make it sound more like the speaker from the training |  Boolean   |


### Deepgram TTS

Deepgram's text-to-speech feature is the cheapest by far with credits given with every new account. The cost to maintain the app using Deepgram's API is very low while providing very high-quality transcriptions. The speed of the application is very quick compared to other services and is 30% more accurate than other services on average, leading the market across use-case categories. There is a variety of voices we can use for Deepgram, allowing contributors to freely customize the experience of the app.

The complete list of voice selections can be found [here](https://developers.deepgram.com/docs/tts-models).

|        Parameters       |       Required/Optional      |                             Values                               | Value Type |
| :---------------------: | :--------------------------: | :--------------------------------------------------------------: | :---------:|
|          model          |           Required           |                         "deepgram_tts"                           |   String   |
|         content         |           Required           |               The text to be converted to speech                 |   String   |
|          voice          |           Optional           |                  The voice model for the audio                   |   String   |


### Bark TTS

Bark is a text-to-speech model by Suno AI, which was used in mentor Vedant's project (Voice CMS) last year, which is a free API we can use to transcribe text to speech.

|        Parameters       |       Required/Optional      |                             Values                               | Value Type |
| :---------------------: | :--------------------------: | :--------------------------------------------------------------: | :---------:|
|          model          |           Required           |                           "bark_tts"                             |   String   |
|         content         |           Required           |               The text to be converted to speech                 |   String   |


## Groq TTT

Groq is an LPU that speeds up LLM responses, and it is free to use for our applications traffic. It provides various models for users to select, so they are able to test which one fits best to reduce any latency when users use our apps.

|        Parameters       |       Required/Optional      |                                 Values                                   | Value Type |
| :---------------------: | :--------------------------: | :----------------------------------------------------------------------: | :---------:|
|          model          |           Required           | "llama3-8b-8192", "llama3-70b-8192", "mixtral-8x7b-32768", "gemma-7b-it" |   String   |
|         content         |           Required           |                  The text to be sent to the LLM model                    |   String   |