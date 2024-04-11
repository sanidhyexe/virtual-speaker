import pyttsx3
import tkinter as tk



print()
intro = pyttsx3.init()

print("I am a virtual speaker. ")
intro.say("I am a virtual speaker ")

print()

print("Developed My Sanidhy Srivastava.")
intro.say("Developed by Sanidhy Srivastava")

print()
intro.runAndWait()

print("Type the statement or word you want me to say")
intro.say("Type the statement or word you want me to say")
intro.runAndWait()

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

print()

while True:
    print("Continue typing : ")
    a = input()
    say(a)
