from utils import api_key
import openai
import pyttsx3 
import requests
import time
import multiprocessing


openai.api_key = api_key
engine = pyttsx3.init()

URL = "https://api.openai.com/v1/chat/completions"

stop_event = multiprocessing.Event()
message = [{"role" : "system" , "content" : "You are a friendly AI"},]
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id)

def output_message(message, ip):
    message.append({
        "role" : "user",
        "content" : f"{ip}"
    })


    payload = {
        "model" : "gpt-3.5-turbo",
        "messages" : message, 
        "temperature" : 1.0,
        "n" : 1,
        "stream" : False,
        "presence_penalty" : 0,
        "frequency_penalty" : 0   
    }


    response = requests.post(URL, headers=headers, json = payload, stream = False)
    response = response.json()
    # print(response)
    txt = response["choices"][0]["message"]["content"]
    print("ChatGPT: ", txt)
    engine.say(txt)
    # engine.say("Hi This is sample text 2")
    stop_event.set()
    engine.runAndWait()
    message.append({
        "role" : "assistant",
        "content" : txt
    })
    # print("Done")
    time.sleep(2) 



def generating():
    while not stop_event.is_set():
        print(".", end = "") 
        time.sleep(0.1)  
    if stop_event.is_set():
        print(end = "\n")
        print("Done", end = "\n")        

headers = {
    "content_type" : "application/json",
    "Authorization" : f"Bearer {openai.api_key}"
}


if __name__ == "__main__":
    
    while(True):
        stop_event = multiprocessing.Event()
        ip = input("User : ")
        if(ip.lower() == "good bye"):
            print("Chat GPT : ", "Goodbye! If you have any more questions in the future, feel free to ask. Have a great day!")
            engine.say("Goodbye! If you have any more questions in the future, feel free to ask. Have a great day!")
            engine.runAndWait()
            break

        output_message(message, ip)
        # print("generating", end = " ")
        # thread1 = multiprocessing.Process(target = output_message, args = (message, ip))
        # thread2 = multiprocessing.Process(target = generating)
        # thread1.start()
        # thread2.start()

        # time.sleep(15)

        # thread1.terminate()
        # thread2.terminate()

        # thread1.join()
        # thread2.join()
    