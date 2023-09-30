# %%
# Import modules
import random
from tkinter import *
import tkinter.messagebox as tmsg

# Define the parameters for window: title, height, and width of window, background
window = Tk()
window.title("Word guessing game")
window.geometry("900x600")
window.configure(bg = "red")

# Defining basic parameters of game
list_of_words = ['Palpatine', 'Mace Windu', 'Obi-Wan Kenobi', 'Anakin Skywalker', 'Ahsoka Tano', 'Luke Skywalker', 'Han Solo', 'Leia Organa', 'Lando Carlissian', 'General Grievous']
guess = random.choice(list_of_words)
chance = 5
var = StringVar()
guess = StringVar()

# Function responsible for guessing the world
def word_guess():
    global guess
    global chance
    usr_ip = var.get()
    if chance > 0:
        if usr_ip == guess:
            msg = f'You won! {guess} is the right answer'
        elif usr_ip != guess:
            chance -= 1
            msg = f'Bad answer. You have {chance} attempt left'
        else:
            msg = 'Something went wrong!'
    else:
        msg = f'You lost! you have {chance} attempt left'
        
    guess.set(msg)
    
# Label "Welcome to Word guessing game!"
L = Label(window, text = "Welcome to Word guessing game!", font = ("Courier", 30))
L.pack()

# Entry to guess word from the list
E = Entry(window, textvariable = var, bd = 5)
E.pack()

# Button with label "Guess the word"
B = Button(window, text = "Guess the word", bd = 5, command = word_guess)
B.pack()

# Button with label "Quit"
B2 = Button(window, text = "Quit", bd = 7, command = window.destroy)
B2.pack()

# Message with result of guessing
Label(window, textvariable = guess, bg = "red", font = ("sans-serif", 14)).pack(pady = (20, 0))

# Execute window
window.mainloop()
            

# %%
