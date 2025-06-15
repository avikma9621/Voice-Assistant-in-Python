import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import pyjokes
import wikipedia

# Initialize the engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning!")
    elif hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am your assistant. How can I help you?")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
    except Exception:
        speak("Sorry, I didn't catch that. Can you repeat?")
        return "None"
    return query.lower()

def run_assistant():
    greet()
    while True:
        query = take_command()

        if 'time' in query:
            time = datetime.datetime.now().strftime('%H:%M')
            speak(f"The time is {time}")

        elif 'date' in query:
            date = datetime.datetime.now().strftime('%d %B %Y')
            speak(f"Today's date is {date}")

        elif 'open youtube' in query:
            speak("Opening YouTube")
            webbrowser.open("https://youtube.com")

        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("https://google.com")

        elif 'search' in query:
            speak("What should I search?")
            search_query = take_command()
            webbrowser.open(f"https://www.google.com/search?q={search_query}")

        elif 'joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif 'who is' in query:
            person = query.replace('who is', '')
            info = wikipedia.summary(person, sentences=1)
            speak(info)

        elif 'exit' in query or 'bye' in query:
            speak("Goodbye! Have a nice day.")
            break

if __name__ == "__main__":
    run_assistant()
