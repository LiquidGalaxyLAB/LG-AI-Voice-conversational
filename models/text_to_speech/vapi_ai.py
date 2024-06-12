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

    def synthesize(self, text_data):
        url = f'{self.base_url}/synthesize'
        data = {
            "text": text_data,
            "sessionId": self.session_id
        }
        response = requests.post(url, headers=self.headers, json=data)
        response.raise_for_status()
        return response.content

vapi_ai_instance = VapiAI('public-key')

def synthesize(text_data):
    return vapi_ai_instance.synthesize(text_data)
