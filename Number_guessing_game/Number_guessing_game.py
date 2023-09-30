# %%
# Import modules
import random
from tkinter import *
import tkinter.messagebox as tmsg

# Define parameters for window: title, height and width of window, backgorund
window = Tk()
window.title("Number guessing game!")
window.geometry("900x600")
window.configure(bg = "red")

# Defining basic parameters of game
ranNum = random.randint(0, 100)
chance = 10
var = IntVar()
disp = StringVar()

# Function responsible for guessing the number
def check_guess():
    global ranNum
    global chance
    usr_ip = var.get()
    if chance > 0:
        if usr_ip == ranNum:
            msg = f'You won! {ranNum} is the right answer'
        elif usr_ip > ranNum:
            chance -= 1
            msg = f'{usr_ip} is greater. You have {chance} attempt left.'
        elif usr_ip < ranNum:
            chance -= 1
            msg = f'{usr_ip} is smaller. You have {chance} attempt left.'
        else:
            msg = 'Something went wrong!'
    else: 
        msg = f'You lost! you have {chance} attempt left.'
        
    disp.set(msg)

# Label "Welcome to Number guessing game"
L =  Label(window, text = "Welcome to Number guessing game!", font = ("Courier", 30))
L.pack()

# Entry to guess number from range 1-100
E = Entry(window, textvariable = var, bd = 5)
E.pack()

# Button with label "Guess the number"
B = Button(window, text = "Guess the number", bd = 5, command = check_guess)
B.pack()

# Button with label "Quit"
B2 = Button(window, text = "Quit", bd = 7, command = window.destroy)
B2.pack()

# Message with result of guessing
Label(window, textvariable = disp, bg = "red", font = ("sans-serif", 14)).pack(pady = (20, 0))

# Execute window
window.mainloop()

# %%
