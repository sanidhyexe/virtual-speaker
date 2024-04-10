import pyttsx3
import speech_recognition as sr

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        query = r.recognize_google_cloud(audio, language="en-IN" )
        print (f"user said {query}")
        return query

if __name__ == "__main__":
    print("Jarvis Ai")
    say("Hello I am Jarvis A.I.")
    while True:
        print("Listening...")
        query = take_command()
        #say(query)
