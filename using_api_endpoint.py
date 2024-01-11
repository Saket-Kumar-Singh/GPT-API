from utils import api_key
import openai
import requests

openai.api_key = api_key

URL = "https://api.openai.com/v1/chat/completions"

payload = {
    "model" : "gpt-3.5-turbo",
    "messages" : [{"role" : "user", "content" : f"write a 3 word sentence"}],
    "temperature" : 1.0,
    "top_p" : 1.0,
    "n" : 1,
    "stream" : False,
    "presence_penalty" : 0,
    "frequency_penalty" : 0,
}


headers = {
    "Content_type" : "application/json",
    "Authorization" : f"Bearer {openai.api_key}"
}

response = requests.post(URL, headers=headers, json = payload, stream = False)
response = response.json()

print(response)
print("ChatGPT: ",  response["choices"][0]["message"]["content"])