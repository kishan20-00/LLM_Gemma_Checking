import requests
import json

url = "https://434e-34-141-141-241.ngrok-free.app/generate"

# Single prompt
prompt = "Hi"

response = requests.post(url, json={"prompt": prompt}, verify=False)

if response.status_code == 200:
    print(f"Prompt: {prompt}\nResponse: {response.json().get('response')}\n")
else:
    print(f"Error: {response.status_code}, {response.text}")
