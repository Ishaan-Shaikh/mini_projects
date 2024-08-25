import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import subprocess
from datetime import datetime
import wikipedia

# engine
def main():
    user_logo_ka_guide = """
        1) To get quick meaning or info about a famous person give command: 'search {eg.   albert einstein}'.
        2) To launch an app give command somethin like: 'launch notepad'.
        3) Current time: 'what is cuurent time' """
    print(user_logo_ka_guide)
    while True:
        command = recognize_speech()
        if command:
            process_command(command)


# should recognize sound
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return None
    except sr.RequestError:
        print("Request failed; please check your internet connection.")
        return None

# Text-to-Speech code block
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# processor
def process_command(command):
    if 'time' in command:
        tell_time()
    elif 'open' in command and 'website' in command:
        open_website(command)
    elif 'launch' in command:
        launch_application(command)
    elif 'search' in command:
        search_wikipedia(command)
    else:
        speak("I'm sorry, I can't perform that action.")

# get current time
def tell_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    speak(f"The current time is {current_time}")

# browsing (still pending...)
def open_website(command):
    if 'google' in command:
        webbrowser.open('https://www.google.com')
        speak("Launching Google")
    elif 'youtube' in command:
        webbrowser.open('https://www.youtube.com')
        speak("Lanching YouTube")
    else:
        speak("Sorry, I can't open that website.")

# Application Launcher Function
def launch_application(command):
    if 'notepad' in command:
        os.system('notepad')
        speak("Launching Notepad")
    elif 'calculator' in command:
        os.system('calc')
        speak("Launching Calculator")
    elif 'google' in command:
        chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        if os.path.exists(chrome_path):
            subprocess.Popen([chrome_path])
            speak("Launching Google Chrome")
        else:
            speak("Google Chrome not found.")
    else:
        speak("Sorry, I can't launch that application.")

# Wikipedia Search Function
def search_wikipedia(command):
    try:
        query = command.replace('search', '').strip()
        result = wikipedia.summary(query, sentences=2)
        speak(f"According to Wikipedia, {result}")
    except wikipedia.exceptions.DisambiguationError as e:
        speak(f"Multiple results found: {e.options}")
    except wikipedia.exceptions.PageError:
        speak("Sorry, I couldn't find any results for that query.")


if __name__ == "__main__":
    main()
