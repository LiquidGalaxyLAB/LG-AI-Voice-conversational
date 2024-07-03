import os
import uuid
import requests
# import ChatTTS
# import torch
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Request, UploadFile, File, Form
from fastapi.responses import FileResponse, JSONResponse
from groq import Groq
from bark import SAMPLE_RATE, generate_audio
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs
from deepgram import DeepgramClient, ClientOptionsFromEnv, SpeakOptions, FileSource, PrerecordedOptions
from google.cloud import texttospeech
from google.cloud import speech
from IPython.display import Audio
from scipy.io.wavfile import write as write_wav
from tempfile import NamedTemporaryFile
from model_config import MODEL_CONFIGS

load_dotenv()
app = FastAPI()

@app.post("/speech-to-text/")
async def speech_to_text(
    model: str = Form(...), 
    audio: UploadFile = File(...)
):
    try:
        model_config = MODEL_CONFIGS.get(model)
        if not model_config:
            raise HTTPException(status_code=400, detail="Model not found.")

        audio_bytes = await audio.read()

        if model == "deepgram_stt":
            DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")
            if not DEEPGRAM_API_KEY:
                raise ValueError("DEEPGRAM_API_KEY is missing.")

            deepgram = DeepgramClient(api_key=DEEPGRAM_API_KEY)

            payload: FileSource = {"buffer": audio_bytes}

            options = PrerecordedOptions(
                model="nova-2",
                smart_format=True
            )

            response = deepgram.listen.prerecorded.v("1").transcribe_file(payload, options)

            transcript = response["results"]["channels"][0]["alternatives"][0]["transcript"]
            return JSONResponse(content={"transcript": transcript})
        
        elif model == "google_cloud_stt":
            client = speech.SpeechClient()

            audio_content = speech.RecognitionAudio(content=audio_bytes)

            config = speech.RecognitionConfig(
                encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
                language_code="en-US"
            )

            response = client.recognize(config=config, audio=audio_content)

            transcript = response.results[0].alternatives[0].transcript
            return JSONResponse(content={"transcript": transcript})

        raise HTTPException(status_code=400, detail="Unsupported model.")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")


@app.post("/text-to-speech")
async def text_to_speech(request: Request):
    data = await request.json()
    model = data.get("model")
    content = data.get("content")

    if model == "google_cloud_tts":
        try:
            language_code = data.get("language_code", "en-US")
            voice_name = data.get("name", "en-US-Wavenet-D")
            audio_encoding = data.get("audio_encoding", "LINEAR16")
            speaking_rate = data.get("speaking_rate", 1.0)
            pitch = data.get("pitch", 0.0)
            volume_gain_db = data.get("volume_gain_db", 0.0)
            sample_rate_hertz = data.get("sample_rate_hertz", None)

            client = texttospeech.TextToSpeechClient()
            synthesis_input = texttospeech.SynthesisInput(text=content)
            voice = texttospeech.VoiceSelectionParams(
                language_code=language_code, 
                name=voice_name
            )
            audio_config = texttospeech.AudioConfig(
                audio_encoding=texttospeech.AudioEncoding[audio_encoding],
                speaking_rate=speaking_rate,
                pitch=pitch,
                volume_gain_db=volume_gain_db,
                sample_rate_hertz=sample_rate_hertz
            )
            response = client.synthesize_speech(
                input=synthesis_input, voice=voice, audio_config=audio_config
            )

            with NamedTemporaryFile(delete=False, suffix=".wav") as temp_file:
                temp_file.write(response.audio_content)
                temp_file_path = temp_file.name

            return FileResponse(
                temp_file_path, media_type="audio/wav", filename="google_cloud.wav"
            )

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
    
    if model == "bark_tts":
        try:
            audio_array = generate_audio(content)
            with NamedTemporaryFile(delete=False, suffix=".wav") as temp_file:
                write_wav(temp_file.name, SAMPLE_RATE, audio_array)
                temp_file_path = temp_file.name
            return FileResponse(temp_file_path, media_type="audio/wav", filename="bark.wav")

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")


    if model == "elevenlabs_tts":
        ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

        if not ELEVENLABS_API_KEY:
            raise ValueError("ELEVENLABS_API_KEY is missing.")
        
        try:
            voice_id = data.get("voice_id", "pNInz6obpgDQGcFmaJgB")
            model_id = data.get("model_id", None)
            latency = data.get("latency", "0")
            stability = data.get("stability", 0.0)
            similarity = data.get("similarity", 0.0)
            style = data.get("style", 0.0)
            use_speaker_boost = data.get("use_speaker_boost", False)

            
            client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
        
            response = client.text_to_speech.convert(
            voice_id=voice_id,
            optimize_streaming_latency=latency,
            output_format="mp3_22050_32",
            text=content,
            model_id=model_id,
            voice_settings=VoiceSettings(
                stability=stability,
                similarity_boost=similarity,
                style=style,
                use_speaker_boost=use_speaker_boost,
                )
            )
            save_file_path = f"{uuid.uuid4()}.mp3"

            with open(save_file_path, "wb") as f:
                for chunk in response:
                    if chunk:
                        f.write(chunk)
            return FileResponse(save_file_path, media_type="audio/mpeg", filename="elevenlabs.mp3")

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")


    if model == "deepgram_tts":
        DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")

        if not DEEPGRAM_API_KEY:
            raise ValueError("DEEPGRAM_API_KEY is missing.")
        
        try:
            voice = data.get("voice", "aura-asteria-en")
            deepgram = DeepgramClient(api_key=DEEPGRAM_API_KEY, config=ClientOptionsFromEnv())
            options = SpeakOptions(model=voice)
            response = await deepgram.asyncspeak.v("1").save("deepgram.mp3", {"text": content}, options)
            return FileResponse("deepgram.mp3", media_type="audio/mpeg", filename="deepgram.mp3")

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
    
    # if model == "chatt_tts":
    #     try:
    #         chat = ChatTTS.Chat()
    #         chat.load_models()
    #         wavs = chat.infer([content], use_decoder=True)

    #         with NamedTemporaryFile(delete=False, suffix=".wav") as temp_file:
    #             write_wav(temp_file.name, 24000, wavs[0])
    #             temp_file_path = temp_file.name
    #         return FileResponse(temp_file_path, media_type="audio/wav", filename="chatt_tts.wav")

    #     except Exception as e:
    #         raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

@app.post("/groq/")
async def create_chat_completion(request: Request):
    data = await request.json()
    model = data.get("model")
    content = data.get("content")
    model_config = MODEL_CONFIGS.get("groq")
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
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
