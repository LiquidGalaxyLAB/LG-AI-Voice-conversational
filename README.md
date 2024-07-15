# LG AI Voice Conversation

Documentation to integrate AI voices to LG applications. The REST API is split into three endpoints: speech-to-text, text-to-text via Groq, and text-to-speech. The documentation is split into three seperate pages, one for all the model descriptions with required and optional parameters, one for how to setup and use the API, and a pricing documentation.

The table below lists all the models used in the project:


## AI Models

|        Speech-to-Text       |              Text-to-Speech           |   LLM (via Groq)   |
| :-------------------------: | :-----------------------------------: | :----------------: |
| Google Cloud AI with Gemini |      Google Cloud AI with WaveNet     |    Gemma2-9b-it    |
|          Deepgram           |                Deepgram               |    Gemma-7b-It     |
|         AssemblyAI          |              llElevenLabs             | Mixtral-8x7b-32768 |
|                             |                  Bark                 |   Llama3-8b-8192   |
|                             |                                       |   Llama3-70b-8192  |


## Model Documentation

Link to the description of the models and costs are [here](./docs/models.md).


## API Documentation

Link to the API usage for voice-to-voice integrations for LG apps are [here](./docs/api.md).


## Pricing

Link to the list of all the model pricing are listed [here](./docs/pricing.md).