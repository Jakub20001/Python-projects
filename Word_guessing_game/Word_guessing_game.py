from tkinter import *
import random

window = Tk()

window.title("Word guessing game")

window.geometry("800x600")

window.configure(bg = "red")

words = ["Psychology", "Biology", "Chemistry", "Maths", "Physics", "Medicine", "Geography"]

L = Label(window, text = "Welcome to word guessing game!", font = ("Courier", 30))
L.pack()

word = random.choice(words)
chances = 6
var = StringVar()

def wordGuessing():
    global word
    global chances
    usr_disp = var.get()
    if chances > 0:
        if usr_disp != word:
            Label(window, text = "Answer is not correct! Try again", font = ("Courier", 15)).pack()
            chances -= 1
        elif usr_disp == word:
            Label(window, text = "Answer is correct! You won!", font = ("Courier", 15)).pack()
    elif chances == 0:
        Label(window, text = "You lose!", font = ("Courier", 15)).pack()
        
E = Entry(window, textvariable = var, font = ("Courier", 10))
E.pack()
            
B = Button(window, text = "Submit", font = ("Courier", 10), command = wordGuessing)
B.pack()

B2 = Button(window, text = "Quit", font = ("Courier", 10), command = window.destroy)
B2.pack()

window.mainloop()
