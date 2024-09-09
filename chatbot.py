!pip install -q -U google-generativeai

import os
os.environ["API_KEY"] = "AIzaSyA8BQhZB3i2CwQDAZOfOyg4eP8Cqdi7dp8"

import google.generativeai as genai
import os

genai.configure(api_key=os.environ["API_KEY"])

import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()


def SpeakText(command):
    
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


while True:    
    
    try:
        
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)
            
            
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            
            
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(MyText)
            
            
            response_text = response.text.split(". ", 1)[-1]  
            
            print(response_text)
            
            
            SpeakText(response_text)
            break
            
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        
    except sr.UnknownValueError:
        print("Unknown error occurred")
