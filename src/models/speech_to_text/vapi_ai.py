import requests

class VapiAI:
    def __init__(self, public_key):
        self.public_key = public_key
        self.base_url = 'https://api.vapi.ai'
        self.headers = {'Authorization': f'Bearer {self.public_key}'}
        self.session_id = None

    def start_call(self, assistant=None, assistant_id=None, assistant_overrides=None):
        url = f'{self.base_url}/start'
        data = {}
        if assistant:
            data['assistant'] = assistant
        if assistant_id:
            data['assistantId'] = assistant_id
        if assistant_overrides:
            data['assistantOverrides'] = assistant_overrides
        
        response = requests.post(url, headers=self.headers, json=data)
        response.raise_for_status()
        self.session_id = response.json().get('sessionId')
        return response.json()

    def transcribe(self, audio_data):
        if not self.session_id:
            self.start_call()

        assistant = {
            "model": {
                "provider": "openai",
                "model": "gpt-3.5-turbo",
                "systemPrompt": "You're an assistant!"
            },
            "voice": {
                "provider": "11labs",
                "voiceId": "burt",
            },
        }
        
        call_response = self.start_call(assistant=assistant)
        return call_response.get('transcription', 'Transcription not available')

    def send_message(self, role, content):
        url = f'{self.base_url}/send'
        data = {
            "type": "add-message",
            "message": {
                "role": role,
                "content": content
            },
            "sessionId": self.session_id
        }
        response = requests.post(url, headers=self.headers, json=data)
        response.raise_for_status()
        return response.json()

    def set_muted(self, muted):
        url = f'{self.base_url}/mute'
        data = {
            "muted": muted,
            "sessionId": self.session_id
        }
        response = requests.post(url, headers=self.headers, json=data)
        response.raise_for_status()
        return response.json()

    def stop_session(self):
        url = f'{self.base_url}/stop'
        data = {
            "sessionId": self.session_id
        }
        response = requests.post(url, headers=self.headers, json=data)
        response.raise_for_status()
        self.session_id = None
        return response.json()

vapi_ai_instance = VapiAI('public-key')

def transcribe(audio_data):
    return vapi_ai_instance.transcribe(audio_data)

def send_message(role, content):
    return vapi_ai_instance.send_message(role, content)

def set_muted(muted):
    return vapi_ai_instance.set_muted(muted)

def stop_session():
    return vapi_ai_instance.stop_session()
