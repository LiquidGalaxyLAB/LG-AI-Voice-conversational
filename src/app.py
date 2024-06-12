from flask import Flask, request, jsonify
from models.speech_to_text import vapi_ai as stt_model
from models.text_to_speech import vapi_ai as tts_model

app = Flask(__name__)

@app.route('/speech-to-text', methods=['POST'])
def speech_to_text():
    model_name = request.headers.get('X-STT-Model')
    if not model_name:
        return jsonify({'error': 'X-STT-Model header is missing'}), 400

    audio_data = request.data
    text = stt_model.transcribe(audio_data)
    
    return jsonify({'text': text})

@app.route('/text-to-speech', methods=['POST'])
def text_to_speech():
    model_name = request.headers.get('X-TTS-Model')
    if not model_name:
        return jsonify({'error': 'X-TTS-Model header is missing'}), 400

    text_data = request.json.get('text')
    if not text_data:
        return jsonify({'error': 'No text provided'}), 400

    audio = tts_model.synthesize(text_data)
    
    return audio

@app.route('/mute-mic', methods=['POST'])
def mute_mic():
    model_name = request.headers.get('X-Model')
    if not model_name:
        return jsonify({'error': 'X-Model header is missing'}), 400

    muted = request.json.get('muted', True)

    stt_model.set_muted(muted)
    
    return jsonify({'muted': muted})

if __name__ == '__main__':
    app.run(debug=True)
