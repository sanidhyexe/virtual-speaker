import tkinter as tk
import pyttsx3

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def speak_text():
    text = entry.get()
    say(text)

root = tk.Tk()
root.title("Virtual Speaker")

label = tk.Label(root, text="Type the statement or word you want me to say")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Speak", command=speak_text)
button.pack()

root.mainloop()