import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
import time
import threading
import keyboard

def command_generator(speechortext):
    engine = pyttsx3.init()
    r = sr.Recognizer()
    if (speechortext=="t"):
        while True:
            command=input("Enter your prompt: ").lower().strip()
            if("quit" in command and "google" in command):
                engine.say("Had a great time with you, lets meet again soon!!")
                engine.runAndWait()
                exit()
            else:
                return command
    elif (speechortext=="s"):
        while True:
            try:
                with sr.Microphone() as source:
                    print("Listning...")
                    r.adjust_for_ambient_noise(source, duration=1)
                    audio = r.listen(source, timeout=3, phrase_time_limit=1 )
                    print(r.recognize_google(audio))
                    command=r.recognize_google(audio)
                    code= command.lower().split(" ")
                if ("quit" in code and "google" in code):
                    print("Google back to sleep!!")
                    engine.say("Had a great time with you, lets meet again soon!!")
                    engine.runAndWait()
                    exit()
                return command

            except Exception:
                print("Sorry, no speech detected.")

def gem(command, GEMINI_API_KEY, speechortext):
    URLS = {
        "google": "https://google.com",
        "youtube": "https://youtube.com",
        "instagram": "https://www.instagram.com/kirthan.nb/",
        "facebook": "https://facebook.com",
        "github": "https://github.com/KirthanNB",
        "linkedin": "https://www.linkedin.com/in/kirthan-nb-8b522530b/"
    }

    engine = pyttsx3.init()
    for keyword, url in URLS.items():
        if f"open {keyword}" in command:
            print(f"Opening {keyword}...")
            engine.say(f"Opening {keyword}")
            engine.runAndWait()
            webbrowser.open(url)
            return
    gemini(command, GEMINI_API_KEY, speechortext)



def awaken(GEMINI_API_KEY, speechortext):
    print("Google Awaken!!")
    engine.say("Glad to hear you called for google.; how may i help you today\n")
    engine.runAndWait()
    while True: 
        command= command_generator(speechortext)
        gem(command, GEMINI_API_KEY, speechortext)
    
    
def gemini(command, GEMINI_API_KEY, speechortext):
    a=command
    engine = pyttsx3.init()
    if GEMINI_API_KEY != None:
        while True:

            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"

            headers = {
                "Content-Type": "application/json"
            }

            data = {
                "contents": [{
                    "parts": [{"text": a + ', (keep response limit in 80 words untill and unless specified out of this box)'}]
                }]
            }

            response = requests.post(url, headers=headers, json=data)

            if response.status_code == 200:
                rep=response.json().get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "No response found.")
                print(f"\n{rep}")
                speak_thread =threading.Thread(target=lambda:(engine.say(rep), engine.runAndWait()))
                speak_thread.start()
                keyboard.read_event()
                engine.stop()
                
            else:
                print("Error:", response.status_code, response.text)
            a=command_generator(speechortext)
            gem(a, GEMINI_API_KEY, speechortext)
    else:
        print("Gemini API Key is required to process your request!!")
        engine.say("Gemini API Key is required to process your request!!")
        engine.runAndWait()
        a=command_generator(speechortext)
        gem(a, GEMINI_API_KEY, speechortext)

engine = pyttsx3.init()
r = sr.Recognizer()
voices = engine.getProperty('voices')       
engine.setProperty('voice', voices[0].id)
rate = engine.getProperty('rate')                          
engine.setProperty('rate', 180)
print("Welcome to Kirthan's new Python-Project!!")
print("""\nHere is a small Exploring guide\n\nYou can open Google, Youtube, Linkedin, Instagram, Github, Facebook in a single call!!\nAnd the more exciting part is that you can also chat with me and have a great time spent together!!\nMake sure to have stable Internet Connection...\n\n\nYou can call for "Quit Google" to end this program\n""")
engine.say("Hello Welcome to Keertan's New python-project, please take a second to read message displayed out here in terminal. Thank you!!")
engine.runAndWait()
time.sleep(2)
engine.say("Here is a small Exploring guide\n\nYou can open Google, Youtube, Linkedin, Github, Facebook in a single call!!\nAnd the more exciting part is that you can also chat with me and have a great time spent together!!Make sure to have stable Internet Connection for using voice to speech mode and using API\n\n\nYou can call for Quit Google to end this program")
engine.runAndWait()
print("Initialising Google...")
engine.say("Initialising Google...")
engine.runAndWait()
time.sleep(1)
engine.say("Please select,, T for texting your promts,, S for speech mode, however i answer in both text and voice mode")
engine.runAndWait()
while True:
    speechortext = input("Enter T (Text mode) or S (Speech mode): ").lower().strip()
    if speechortext in ["t", "s"]:
        while True:
            engine.say("Enter your Gemini API Key")
            engine.runAndWait()
            sn=input("Do you have Gemini_API_Key:\nY (yes) N (no): ").lower()
            if sn=="y":
                GEMINI_API_KEY=input("Enter Your GEMINI_API_KEY: ")
                awaken(GEMINI_API_KEY, speechortext)
            elif sn=="n":
                print("You can still explore opening websites mentioned eariler...")
                engine.say("You can still explore opening websites mentioned eriler.")
                engine.runAndWait()
                awaken(None, speechortext)