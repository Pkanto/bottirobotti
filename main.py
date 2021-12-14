import requests
import wikipedia
import pywhatkit as kit
from email.message import EmailMessage
import smtplib
from decouple import config
import pyttsx3
from datetime import datetime
import speech_recognition as sr
from random import choice
from utils import opening_text


USERNAME = "Pasi"
BOTNAME = "Bottirobotti"

engine = pyttsx3.init()

# Set Rate
engine.setProperty('rate', 190)

# Set Volume
engine.setProperty('volume', 1.0)

# Set Voice (Female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    
    engine.say(text)
    engine.runAndWait()



def greet_user():
#Hakee ajan ja tervehtii
    
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Hyvää huomenta {USERNAME}")
    elif (hour >= 12) and (hour < 16):
        speak(f"Hyvää iltapäivää {USERNAME}")
    elif (hour >= 16) and (hour < 19):
        speak(f"Hyvää iltaa {USERNAME}")
    speak(f"I am {BOTNAME}. How may I assist you?")

def take_user_input():
    #ottaa vastaan käyttäjän antaman äänen

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Kuunnellaan....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Tunnistetaan ääntä...')
        query = r.recognize_google(audio, language='en-in')
        if not 'exit' in query or 'stop' in query:
            speak(choice(opening_text))
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("Hyvää iltaa hyvä herra")
            else:
                speak('Hyvää päivää hyvä herra')
            exit()
    except Exception:
        speak('Pahoittelen en ymmärrä sinua')
        query = 'None'
    return query