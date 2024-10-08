# Voice Integration API Documentation


## Overview

This API provides endpoints for speech-to-text, text-to-speech, and text-to-text via Groq using various models to allow for users to have more flexibility in their options.


## Authorization

Rename the `env_example` file to `.env` and set each appropriate API keys as listed below without quotes as shown in the file.

- ELEVENLABS_API_KEY
    - Key can be generated [here](https://elevenlabs.io/app/speech-synthesis) under `Profile + API Key`.
- DEEPGRAM_API_KEY
    - Key can be generated [here](https://console.deepgram.com/).
- ASSEMBLYAI_API_KEY
    - Key can be generated [here](https://www.assemblyai.com/app).
- GROQ_API_KEY
    - Key can be generated [here](https://console.groq.com/keys).
- GOOGLE_APPLICATION_CREDENTIALS
    - Navigate to https://console.cloud.google.com/.
    - Create a project for you application.
    - In the left sidebar, go to `IAM & Admin` -> `Service Accounts`.
    - Click `Create Service Account` and create an account.
    - In the account you created, click the three dots on the right and.select `Manage keys`.
    - Click `Add key` -> `Create new key`.
    - Select JSON as the key type and click `Create`. This will store your key as a JSON file, which you need to add to your project locally.
    - After downloading the file, replace the `password_example.json` file with your key and save it under the `credentials` folder.
    - Update the `name-of-your-credentials-file.json` part of the `.env` file with your JSON file name.
    - To enable the Google Cloud Speech-to-Text API, head [here](https://console.cloud.google.com/apis/api/speech.googleapis.com) and enable the API for your project.
    - To enable the Google Cloud Text-to-Speech API, head [here](https://console.cloud.google.com/apis/api/texttospeech.googleapis.com) and enable the API for your project.


## Running the Server

Ensure [Docker Desktop](https://www.docker.com/products/docker-desktop/) is installed and have the application open while using the API.

Build the Docker image:
```
docker build -t ubuntu-python3 .
```

Run the container:
```
docker run -it --env-file .env -p 8440:8440 --rm ubuntu-python3:latest
```


## API Endpoints

The API is configured in such a way that users can pass in all the fields can be passed in as one JSON object. The models documentation has a list of all required and optional parameters for each model, where contributors can decide to customize the usage.

### Speech-to-Text

Convert audio to text using a specified model.

URL:`http://localhost:8440/speech-to-text`

Method: `POST`

Headers: `Content-Type: application/json`

Example:

```
{
  "model": "google_cloud_stt",
  "audio": "<audio_file_content>"
}
```

`200 OK`: On success, returns the transcribed text.

`400 Bad Request`: If required parameters are missing.

Example CURL Command:

```
curl.exe -X POST "http://localhost:8440/speech-to-text/" `
  -F "model=google_cloud_stt" `
  -F "audio=@example.wav"
```

Example Response:

```
{"transcript":"yeah as as much as um it's worth celebrating uh the first Space Walk um with an all female team um I think many of us are looking forward to it just being normal and um I think if it signifies anything it is uh to honor the the women who came before us who um were skilled and qualified um and didn't get uh the same opportunities that we have today"}
```

### Text-to-Speech

Convert text to audio using a specified model.

URL: `http://localhost:8440/text-to-speech`

Method: `POST`

Headers: `Content-Type: application/json`

Example:

```
{
  "model": "google_cloud_tts",
  "content": "Hello, how are you doing today?"
}

```

Response:

`200 OK`: On success, returns the audio data.

`400 Bad Request`: If required parameters are missing.

Example CURL Command:

```
curl.exe -X POST "http://localhost:8440/text-to-speech" `
  -H "Content-Type: application/json" `
  -d "{`"model`":`"google_cloud_tts`",`"content`":`"Hello, this is a test message.`"}" `
  --output google_cloud_tts.wav
```

Example Response:

An audio file will be generated under:

```
google_cloud_tts.wav
```

### Groq

Sends text to the Groq LPU and responds with the response message.

URL: `http://localhost:8440/groq`

Method: `POST`

Headers: `Content-Type: application/json`

Example:

```
{
  "model": "gemma-9b-it",
  "content": "Hello, How are you doing today?"
}
```

Response:

`200 OK`: On success, returns the text data.

`400 Bad Request`: If required parameters are missing.

Example CURL Command:

```
curl.exe -X POST "http://localhost:8440/groq/" `
  -H "Content-Type: application/json" `
  --data-raw '{"model":"gemma2-9b-it","content":"hello"}'
```

Example Response:

```
{"content":"Hello! 👋  How can I help you today?\n"}
```

## Example API Call in Flutter

```
import 'package:http/http.dart' as http;
import 'dart:convert';

Future<Map<String, dynamic>> callAPI(String url, String model, String content) async {
  var response = await http.post(
    Uri.parse(url),
    headers: {
      "Content-Type": "application/json"
    },
    body: jsonEncode({
      "model": model,
      "content": content
    })
  );

  if (response.statusCode == 200) {
    print("API Call Successful");
    return jsonDecode(response.body);
  } else {
    print("Failed to call API: ${response.statusCode}");
    throw Exception('Failed to load data');
  }
}
```