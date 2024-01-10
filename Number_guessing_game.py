from tkinter import *
import random

window = Tk()

window.title("Number guessing game")

window.geometry("800x600")

window.configure(bg = "red")

L = Label(window, text = "Welcome to number guessing game!", font = ("Courier", 30))
L.pack()

random_number = random.randint(1, 11)
chances = 5
var = IntVar()
disp = StringVar()

def numberGuessing():
    global random_number
    global chances
    usr_ip = var.get()
    if chances > 0:
        if usr_ip == random_number:
            Label(window, text = "You won!", font = ("Courier", 15)).pack()
        elif usr_ip > random_number:
            Label(window, text = "Number is bigger than it should be!", font = ("Courier", 15)).pack()
            chances -= 1
        elif usr_ip < random_number:
            Label(window, text = "Number is smaller than it should be!", font = ("Courier", 15)).pack()
            chances -= 1
    elif chances == 0:
        Label(window, text = "You lose!", font = ("Courier", 15)).pack()

        
E = Entry(window, textvariable = var, font = ("Courier", 10))
E.pack()

B = Button(window, text = "Submit", font = ("Courier", 10), command = numberGuessing)
B.pack()

B2 = Button(window, text = "Quit", font = ("Courier", 10), command = window.destroy)
B2.pack()

window.mainloop()