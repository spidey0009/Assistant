import webbrowser
import pyttsx3
import wikipedia
import datetime
import os
import sys
from gtts import gTTS
import time
import speech_recognition as sr
import playsound
import random


def speak(sentence):
    kenny=pyttsx3.init('sapi5')
    voices=kenny.getProperty('voices')
    kenny.setProperty('voice',voices[4].id)
    kenny.say(sentence)
    kenny.runAndWait()
speak("Hello sir!!, Im your assistant Siri")
time.sleep(0.3)

def greet():
    currenTime=int(datetime.datetime.now().hour)
    if currenTime>=12 and currenTime<=16:
        speak("Good Afternoon, How can i Help?")
    elif currenTime>=17 and currenTime<=19:
        speak("Good Evening, How can i Help?")
    elif currenTime>=18 and currenTime<=0:
        speak("Hey there!!, How can I help?")


def inputvoice():
    r=sr.Recognizer()
    with sr.Microphone() as thing:
        speak("im listening")
        r.pause_threshold=1
        voice=r.listen(thing)
        try:
            voice_rec1=r.recognize_google(voice,language="en-in")
            voice_rec=voice_rec1.lower()
            print(voice_rec)

            if "hi" in voice_rec:
                speak("Hi buddy")
            elif "open google" in voice_rec:
                speak("Opening Google")
                webbrowser.open("www.google.com")
            elif "open gmail" in voice_rec:
                speak("Opening Gmail")
                webbrowser.open("www.gmail.com")
            elif "open youtube" in voice_rec:
                speak("Opening youtube")
                webbrowser.open("www.youtube.com")
            elif "open facebook" in voice_rec:
                speak("Opening Facebook")
                webbrowser.open("www.facebook.com")

            elif "play music" in voice_rec:
                speak("Enjoy your music")
                musicFolder="D:\\Songs\\"
                music=["haledil","Paris","pillowtalk","PUBG"]
                random1=musicFolder+random.choice(music)+".mp3"
                os.system(random1)
            elif voice_rec=="bye":
                speak("bye bye")
                quit()
            else:
                internet=wikipedia.summary(voice_rec,4)

                speak("Wikipdeida says")
                time.sleep(1)
                speak(internet)



        except sr.UnknownValueError:
            speak("Pardon me, Can u repeat!!")
            inputvoice()



greet()
while True:
    inputvoice()













