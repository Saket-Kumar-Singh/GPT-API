import openai
from utils import api_key

openai.api_key = api_key


messages = [
    {"role" : "system", "content" : "You are a kind helpful api. "},
]

while True:
    ip = input("User : ")
    if ip:
        messages.append(
            {"role":"user", "content" : ip },
        )
        chat = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo", messages = messages
        )

    reply = chat.choices[0].message.content
    print(f"Chat GPT : {reply}")
    messages.append({
        "role" : "assistant", "content ": reply
    },)    