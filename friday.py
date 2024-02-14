import pyttsx3
import datetime
# speech to text
import speech_recognition as sr
import webbrowser as wb


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
    speak("I'm Friday AI Assistant. How can i help you?")

def command():
    c=sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold=2
        audio=c.listen(source)
    try:
        query=c.recognize_google(audio,language='en')
        print("Tony Tèo: "+query)
    except sr.UnknownValueError:
        print ("Please repeat or typing the command")
        query=str(input('Your order is: '))
    return query


if __name__=="__main__":
    welcome()
    while True:
        query=command().lower()
        if 'google' in query:
            speak('What should I search boss?')
            search=command().lower()

            url=f'https://google.com/search?q={search}'
            wb.get().open(url)
            speak(f'Here is your {search} on Google')
        elif 'youtube' in query:
            speak('What should I search boss?')
            search=command().lower()
            url=f'https://youtube.com/search?q={search}'
            wb.get().open(url)
            speak(f'Here is your {search} on youtube')