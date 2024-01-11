import openai
from utils import api_key

openai.api_key = api_key

completion = openai.ChatCompletion.create(model = "gpt-3.5-turbo", messages = [{"role": "user", "content" : "Write an essay about penguins"}])
print(completion.choices[0].message.content)