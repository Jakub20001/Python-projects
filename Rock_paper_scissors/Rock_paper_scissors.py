from tkinter import *
import random

window = Tk()
window.geometry("800x600")
window.title("Rock paper scissors")
window.config(bg = "red")

L = Label(window, text = 'Welcome to Rock, paper, scissors game!', font = 'arial 20 bold')
L.pack()

user_take = StringVar()

Label(window, text = "Choose any one: Rock, paper, scissors", font = "Arial 15 bold", bg = "red").pack()
Entry(window, font = "Arial 15", textvariable = user_take).pack()

comp_pick = random.randint(1, 3)
if comp_pick == 1:
    comp_pick = "rock"
elif comp_pick == 2:
    comp_pick = "paper"
else:
    comp_pick = "scissors"

Result = StringVar()

def play():
    user_pick = user_take.get()
    if user_pick == comp_pick:
        Result.set('Tie, you both select same')
    elif user_pick == 'rock' and comp_pick == 'paper':
        Result.set("You lost! Computer chose paper!")
    elif user_pick == 'rock' and comp_pick == 'scissors':
        Result.set("You won! Computer chose scissors!")
    elif user_pick == 'paper' and comp_pick == "rock":
        Result.set("You won! Computer chose rock!")
    elif user_pick == 'paper' and comp_pick == 'scissors':
        Result.set("You lost! Computer chose scissors!")
    elif user_pick == 'scissors' and comp_pick == 'rock':
        Result.set("You lost! computer chose rock!")
    elif user_pick == "scissors" and comp_pick == "paper":
        Result.set("You win! Computer chose paper!")
    else:
        Result.set('Invalid: choose any one --rock, paper, scissors')
        
def Reset():
    Result.set("")
    user_take.set("")
    
def Exit():
    window.destroy()
    
Entry(window, font = "arial 10 bold", textvariable = Result, bg = "antiquewhite2").pack()

Button(window, font = "arial 13 bold", text = "Play", command = play).pack()

Button(window, font = "arial 13 bold", text = "Reset", command = Reset).pack()

Button(window, font = "arial 13 bold", text = "Exit", command = Exit).pack()

window.mainloop()
