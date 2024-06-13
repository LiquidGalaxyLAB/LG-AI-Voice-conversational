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

## API Endpoints

### Speech-to-Text

Convert audio to text using a specified model.

URL:`/speech-to-text`

Method: `POST`

Headers: `X-STT-Model`: The model to use for speech-to-text conversion.

Request Body: Raw audio data.

Response: `200 OK`: On success, returns the transcribed text:

```
{
    "text": "Transcribed text"
}
```

`400 Bad Request`: If X-STT-Model header is missing or audio data is not provided.

### Text-to-Speech

Convert text to audio using a specified model.

URL: `/text-to-speech`

Method: `POST`

Headers: `X-TTS-Model`: The model to use for text-to-speech conversion.

Request Body:

`text`: The text to be converted to audio.

```
{
    "text": "Hello, how are you?"
}
```

Response:

`200 OK`: On success, returns the audio data.

`400 Bad Request`: If X-TTS-Model header or text is missing.

### Mute/Unmute Microphone

Mute or unmute the user's microphone.

URL: `/mute-mic`

Method: `POST`

Headers: `X-Model`: The model to use.

Request Body:

`muted`: Boolean indicating whether to mute or unmute the microphone.

```
{
    "muted": true
}
```

Response:

`200 OK`: On success, returns the current mute status.
