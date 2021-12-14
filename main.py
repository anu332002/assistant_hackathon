import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pywhatkit
import os
import sys
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
   engine.say(audio)
   engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour) #returns value b/w 0-24
    if hour>=0 and hour<12:
        speak("Good Morning Anushka Ma'am")
    elif hour>=12 and hour<16:
        speak("Good Afternoon Anushka Ma'am")
    else :
        speak("Good Evening Anushka Ma'am")

    speak("i am emma, how may i help you")

def takeCommand():
        listner = sr.Recognizer()
        print("listening...")
        with sr.Microphone() as source:
            audio = listner.listen(source)
        try:
            print("Recognizing...")
            query = listner.recognize_google(audio,language='en-in')
            print(f"user said: {query}\n")

        except Exception as e:
            print(e)
            print("say that again please...")
            return "None"
        return query

if __name__=="__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        if 'send message to' in query:
            d1 = {"mummy": "+91 9911735527", "papa": "+91 9891273597", "rishika": "+91 8546063336"}
            name=query.replace("send message to ","")
            speak('whats the message maam')
            message=takeCommand()
            speak('at what time you want to send the message maam speak hour and minutes consecutively')
            hour=takeCommand()
            min=takeCommand()
            pywhatkit.sendwhatmsg(str(d1.get(name)), str(message), int(hour), int(min))
        elif 'wikipedia' in query:
            speak('searching wikipedia')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)
        elif 'play' in query:
            song=query.replace('play','')
            speak(f"playing {song}")
            pywhatkit.playonyt(song)
        elif 'what is your name' in query:
            speak("I am Emma, nice to meet you")
        elif 'the time' in query:
           current_time=datetime.datetime.now().strftime("%H:%M:%S")
           speak(f"ma'am the time is {current_time}")
        elif 'open code blocks' in query:
            target = "C:\\Program Files\\CodeBlocks\\codeblocks.exe"
            os.startfile(target)
        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")
        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com/")
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")
        elif 'open google' in query:
            webbrowser.open("https://www.google.com/")
        elif 'open classroom' in query:
            webbrowser.open("https://classroom.google.com/u/1/h")
        elif 'thank you' in query:
            speak('pleasure helping you')
            sys.exit(0)



