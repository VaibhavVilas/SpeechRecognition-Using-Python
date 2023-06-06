import pyttsx3 
import datetime
import speech_recognition as sr 
import wikipedia
import webbrowser as wb
import os
import json
import requests
import math
import random
import pyaudio
import wave
import operator
from wikipedia import exceptions


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("This is Sam")


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)

def date():
    Year = int(datetime.datetime.now().year)
    Month = int(datetime.datetime.now().month)
    Date = int(datetime.datetime.now().day)
    speak("Todays date is ")
    speak(Date)
    speak(Month)
    speak(Year)

def wishme():
    speak("Welcome back sir!")
    time()
    date()
    Hour = datetime.datetime.now().hour 
    if Hour >= 6 and Hour <12:
        speak("Good Morning Sir")
    elif Hour >= 12 and Hour<18:
        speak("Good Afternoon Sir")
    elif Hour >= 18 and Hour<24:
        speak("Good Evening Sir")
    else:
        speak("Good Night Sir")
    speak("How can I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone(device_index=0) as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)
    except Exception as e:
        print(e)
        speak("I couldn't get it. Please try saying it again...")
        return "None"
    return query

if __name__ == "__main__":

    wishme()
    while True:
        query = takeCommand().lower()
        if 'time' in query:
            time()
        
        elif 'date' in query:
            date()
        
        elif 'on wikipedia' in query:
            speak("Searching...")
            query = query.replace("on wikipedia","")
            result = wikipedia.summary(query, sentences = 2)
            print(result)
            speak(result)

        elif 'open youtube' in query:
	        speak("Here you go to Youtube\n")
	        wb.open("youtube.com")

        elif 'open google' in query:
	        speak("Here you go to Google\n")
	        wb.open("google.com")

        elif 'open stack overflow' in query:
	        speak("Here you go to Stack Over flow.Happy coding")
	        wb.open("stackoverflow.com")
        
        elif 'open code' in query:
            speak("Here you go to VS Code")
            Path = "C:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(Path)
        
        elif 'joke' in query:
            res = requests.get(
                'https://icanhazdadjoke.com/',
                headers={"Accept":"application/json"})
            if res.status_code == requests.codes.ok:
                speak(str(res.json()['joke']))
            else:
                speak('oops!I ran out of jokes')
        
        elif 'guess the number' in query:
             x = random.randint(0, 101)
             count = 0
             speak("welcome to guess the number, try to guess the number in 10 tries to win. The number is between 0 to 100")
             print(x)
             while count < 7:
                 count += 1
                 party="not today"
                 speak("guess the number")
                 guess = (takeCommand())
                 if x == int(guess):
                     nice="Congratulations you did it in ",count," try"
                     speak(nice)
                     break
                 elif x > int(guess):
                     speak("You guessed too small!")
                 elif x<int(guess):
                     speak("You Guessed too high!")    
                 elif type(guess)==type(party):
                     speak("I coundn't understand you. PLease try again")    
             if count >= 7:
                print("\nThe number is %d" % x)
                print("\tBetter Luck Next time!")
        
        elif 'weather' in query:
            api_key="8c7f564ad57288c1ea4de926e6e16110"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("what is the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in celsius unit is " +
                      str(math.ceil(current_temperature-273)) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in celsius unit = " +
                      str(math.ceil(current_temperature-273)) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

        elif 'brave search' in query:
            speak("What should I search for ?")
            chromepath = 'C:\Program Files\BraveSoftware\Brave-Browser\Application %s'
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search)
            
        elif 'log out' in query:
            os.system("shutdown -1")
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        
            quit()
