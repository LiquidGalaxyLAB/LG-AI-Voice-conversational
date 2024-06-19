# Voice Integration API Documentation

## Overview

This API provides endpoints for speech-to-text (STT) and text-to-speech (TTS) conversions using the various models. It also supports muting/unmuting the microphone to allow users to easily integrate the feature into their application.

## Running the Server

Ensure [Docker](https://www.docker.com/products/docker-desktop/) is installed.

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