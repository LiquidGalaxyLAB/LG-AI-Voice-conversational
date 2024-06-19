import os
import requests
from fastapi import FastAPI, HTTPException, Request
from groq import Groq
from dotenv import load_dotenv
from model_config import MODEL_CONFIGS

load_dotenv()
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
app = FastAPI()

@app.post("/speech-to-text/")
async def speech_to_text(request: Request):
    data = await request.json()
    model = data.get("model")
    params = data.get("params")

    model_config = MODEL_CONFIGS.get(model)
    if not model_config:
        raise HTTPException(status_code=400, detail="Model not found.")

    for param in model_config["required"]:
        if param not in params:
            raise HTTPException(status_code=400, detail=f"Missing required parameter: {param}")

    headers = {
        "Authorization": f"Bearer {os.environ.get(f'{model.upper()}_API_KEY')}"
    }
    body = {key: params[key] for key in model_config["required"]}

    for param in model_config["optional"]:
        if param in params:
            body[param] = params[param]

    if model == "google_cloud_gemini":
        response = requests.post(
            "https://speech.googleapis.com/v1/speech:recognize",
            headers=headers,
            json={"config": {k: v for k, v in body.items() if k != "content"}, "audio": {"content": body["content"]}}
        )
    elif model == "vapi_ai_stt":
        response = requests.post(
            "https://api.vapi.ai/v1/speech-to-text",
            headers=headers,
            json=body
        )
    elif model == "deepgram_stt":
        response = requests.post(
            "https://api.deepgram.com/v1/listen",
            headers=headers,
            files={"audio": body["content"]}
        )
    return response.json()

@app.post("/text-to-speech/")
async def text_to_speech(request: Request):
    data = await request.json()
    model = data.get("model")
    params = data.get("params")

    model_config = MODEL_CONFIGS.get(model)
    if not model_config:
        raise HTTPException(status_code=400, detail="Unsupported model")

    for param in model_config["required"]:
        if param not in params:
            raise HTTPException(status_code=400, detail=f"Missing required parameter: {param}")

    headers = {
        "Authorization": f"Bearer {os.environ.get(f'{model.upper()}_API_KEY')}"
    }
    body = {key: params[key] for key in model_config["required"]}

    for param in model_config["optional"]:
        if param in params:
            body[param] = params[param]

    if model == "google_cloud_wavenet":
        response = requests.post(
            "https://texttospeech.googleapis.com/v1/text:synthesize",
            headers=headers,
            json=body
        )
    elif model == "vapi_ai_tts":
        response = requests.post(
            "https://api.vapi.ai/v1/text-to-speech",
            headers=headers,
            json=body
        )
    elif model == "deepgram_tts":
        response = requests.post(
            "https://api.deepgram.com/v1/synthesize",
            headers=headers,
            json=body
        )
    return response.json()

@app.post("/groq/")
async def create_chat_completion(request: Request):
    data = await request.json()
    model = data.get("model")
    messages = data.get("messages")

    models = ["llama3-8b-8192", "llama3-70b-8192", "mixtral-8x7b-32768", "gemma-7b-it"]
    if model not in models:
        return "Model not found."
    try:
        chat_completion = client.chat.completions.create(
            messages=messages,
            model=model
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {str(e)}"
