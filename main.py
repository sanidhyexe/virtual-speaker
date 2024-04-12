import pyttsx3
import tkinter as tk


def intro( rate=175):
    intro = pyttsx3.init()
    intro.setProperty('rate', rate)
    print("I am a virtual speaker. version : 1.1")
    intro.say("I am a virtual speaker 1.1")
    print("Developed My Sanidhy Srivastava.")
    intro.say("Developed by Sanidhy Srivastava")
    print("Type the statement or word you want me to say")
    intro.say("Type the statement or word you want me to say")
    intro.runAndWait()

def say(text, rate=150):
    engine = pyttsx3.init()
    engine.say(text)
    engine.setProperty('rate',rate)
    engine.runAndWait()

print()
intro()
while True:
    print()
    print("Continue typing : ")
    a = input()
    if a == "amit":
        print("I hate this Name, I am leaving this chat, Bye!")
        say("I hate this Name, I am leaving this chat, bye!")
        break
    say(a,rate=150)
