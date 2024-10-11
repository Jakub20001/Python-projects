from tkinter import *
import random

window = Tk()

window.title("Dice rolling simulator")

window.geometry("1200x800")

window.configure(bg = "blue")

def roll_dices():
    dice_dots = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    L2.configure(text = f'{random.choice(dice_dots)}{random.choice(dice_dots)}')
  
B = Button(window, text = "Roll the dice", font = ("Courier", 30),  command = roll_dices)
B.pack()

L2 = Label(window, font = ("Courier", 120), fg = "red")
L2.pack()
