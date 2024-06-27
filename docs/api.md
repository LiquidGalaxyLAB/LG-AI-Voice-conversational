# Voice Integration API Documentation

## Overview

This API provides endpoints for speech-to-text (STT) and text-to-speech (TTS) conversions using the various models. It also supports muting/unmuting the microphone to allow users to easily integrate the feature into their application.

## Running the Server

Ensure [Docker](https://www.docker.com/products/docker-desktop/) is installed.

Navigate to the `src` directory.

Build the Docker image:

```
docker build -t voice-integration-api .
```

Run the container:
```
docker run -p 8000:8000 voice-integration-api
```

## Authorizaion

Create a `.env` in the `src/` directory and set each appropriate API keys as `MODEL_API_KEY`, where `MODEL` is replaced by the model you are using.

## API Endpoints

### Speech-to-Text

Convert audio to text using a specified model.

URL:`/speech-to-text`

Method: `POST`

Headers: `Content-Type: application/json`

Request Body: Raw audio data.

An object that contains all fields that are passed into the specific API.

`200 OK`: On success, returns the transcribed text.

`400 Bad Request`: If required parameters for the model is missing.

### Text-to-Speech

Convert text to audio using a specified model.

URL: `/text-to-speech`

Method: `POST`

Headers: `Content-Type: application/json`

Request Body:

An object that contains all fields that are passed into the specific API.

Response:

`200 OK`: On success, returns the audio data.

`400 Bad Request`: If required parameters for the model is missing.

### Groq

Sends text to the Groq LPU and responds with the response message.

URL: `/groq`

Method: `POST`

Headers: `Content-Type: application/json`

Request Body:

A `JSON object` containing `model`, and `content`, where content is a string of the messsage being sent to the LLM model, and model is one of:

- llama3-8b-8192
- llama3-70b-8192
- mixtral-8x7b-32768"
- gemma-7b-it

Example input:

```
{
    "model": "gemma-7b-it",
    "content": "How are you doing?"
}
```

Response:

`200 OK`: On success, returns the audio data:

```
{
    "content": "As a language model, I do not have personal experiences or physical health. However, I am functioning optimally and ready to assist you with any information or task you may have for me. How can I help you today?"
}
```

`400 Bad Request`: If required parameters for the model is missing.