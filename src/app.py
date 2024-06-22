import os
import requests
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import FileResponse
from groq import Groq
from dotenv import load_dotenv
from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
from IPython.display import Audio
from tempfile import NamedTemporaryFile
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

@app.post("/text-to-speech")
async def text_to_speech_bark(request: Request):
    data = await request.json()
    model = data.get("model")

    model_config = MODEL_CONFIGS.get(model)
    if not model_config:
        raise HTTPException(status_code=400, detail="Model not found.")
    
    if model == "bark_tts":
        content = data.get("content")

        try:
            audio_array = generate_audio(content)
            with NamedTemporaryFile(delete=False, suffix=".wav") as temp_file:
                write_wav(temp_file.name, SAMPLE_RATE, audio_array)
                temp_file_path = temp_file.name
            return FileResponse(temp_file_path, media_type="audio/wav", filename="bark_generation.wav")

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

@app.post("/groq/")
async def create_chat_completion(request: Request):
    data = await request.json()
    model = data.get("model")
    content = data.get("content")
    model_config = MODEL_CONFIGS.get("groq")
    models = ["llama3-8b-8192", "llama3-70b-8192", "mixtral-8x7b-32768", "gemma-7b-it"]

    if not model_config:
        raise HTTPException(status_code=400, detail="Model config not found.")
    
    if not model or model not in models or not content:
        raise HTTPException(status_code=400, detail="Model and content are required.")
    
    messages = [{"role": "user", "content": content}]
    
    try:
        chat_completion = client.chat.completions.create(
            messages=messages,
            model=model
        )
        return {"content": chat_completion.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
