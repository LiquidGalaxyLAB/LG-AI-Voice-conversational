from fastapi import FastAPI, HTTPException, Header, Request
from fastapi.responses import JSONResponse, StreamingResponse
from models.speech_to_text import vapi_ai as stt_model
from models.text_to_speech import vapi_ai as tts_model

app = FastAPI()

@app.post("/speech-to-text")
async def speech_to_text(request: Request, x_stt_model: str = Header(None)):
    if not x_stt_model:
        raise HTTPException(status_code=400, detail="X-STT-Model header is missing.")

    audio_data = await request.body()
    text = stt_model.transcribe(audio_data)
    
    return JSONResponse(content={"text": text})

@app.post("/text-to-speech")
async def text_to_speech(request: Request, x_tts_model: str = Header(None)):
    if not x_tts_model:
        raise HTTPException(status_code=400, detail="X-TTS-Model header is missing.")

    data = await request.json()
    text_data = data.get("text")
    if not text_data:
        raise HTTPException(status_code=400, detail="No text provided.")

    audio = tts_model.synthesize(text_data)
    
    return StreamingResponse(content=audio, media_type="audio/wav")

@app.post("/send-message")
async def send_message(request: Request, x_model: str = Header(None)):
    if not x_model:
        raise HTTPException(status_code=400, detail="X-Model header is missing.")

    data = await request.json()
    role = data.get("role", "user")
    message = data.get("message")
    response = stt_model.send_message(role, message)
    
    return JSONResponse(content=response)

@app.post("/mute-mic")
async def mute_mic(request: Request, x_model: str = Header(None)):
    if not x_model:
        raise HTTPException(status_code=400, detail="X-Model header is missing")

    data = await request.json()
    muted = data.get("muted", True)
    stt_model.set_muted(muted)
    
    return JSONResponse(content={"muted": muted})
