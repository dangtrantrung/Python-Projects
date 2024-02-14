import pyttsx3
import datetime

friday=pyttsx3.init()
voice=friday.getProperty('voices')
friday.setProperty('voice',voice[0].id)
def speak(audio):
    print('F.R.I.D.A.Y:  '+audio)
    print(".")
    friday.say(audio)
    friday.runAndWait()
#speak('Hello Youtube')

def time():
    Time=datetime.datetime.now().strftime("%I:%M:%p")
    speak(Time)
#time()

def welcome():
    hour=datetime.datetime.now().hour
    if hour >=6 and hour <12:
        speak("Good morning sir")
    elif hour >=12 and hour <18:
        speak("Good afternoon sir")
    elif hour >=18 and hour <24:
        speak("Good night sir")
    speak("How can i help you?")

if __name__=="__main__":
    welcome()