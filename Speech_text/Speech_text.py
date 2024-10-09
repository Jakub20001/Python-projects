# Importing modules
from tkinter import *
from tkinter.messagebox import showinfo
from gtts import gTTS
import speech_recognition as sr
import os


# Turning on the GUI window
window = Tk()
window.title("Text to speech")
window.geometry("1200x800")
window.configure(background = "red")

# Title of app
L = Label(window, text = "Text-To-Speech", font = ("Courier", 20))
L.pack()
 
def say(text1):
    language = 'en'
    speech = gTTS(text = text1, lang = language, slow = False)
    speech.save('text.mp3')
    os.system('start text.mp3')

def recordvoice():
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            try:
                text1 = r.recognize_google(audio, language="en-IN")
            except:
                pass
            return text1
        
def TextToSpeech():
    newWindow = Toplevel(window)
    newWindow.title("Text-to-Speech")
    newWindow.geometry("1200x800")
    newWindow.configure(bg = "red")
    
    L = Label(newWindow, text = "Text-to-Speech", font = ("Courier", 15), bg = "red")
    L.pack()
    
    text = Text(newWindow)
    text.pack()
    
    speakButton = Button(newWindow, text = 'Listen', bg = 'blue', command=lambda: say(str(text.get(1.0, END))))
    speakButton.pack()
    
# Two buttons
B = Button(window, text = "Text-To-Speech-Conversion", font = ("Courier", 20), command = TextToSpeech)
B.pack()
         
window.update()
window.mainloop()
