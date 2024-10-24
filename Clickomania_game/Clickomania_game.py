from tkinter import *
import tkinter as tk
import random
from functools import partial

window = Tk()
window.title("Clickomania game")
window.geometry("500x500")
   
Nav = Frame(master = window, pady = 5, padx = 16)
Main = Frame(master = window, pady = 16, padx = 16)
Footer = Frame(master = window, pady = 16, padx = 16)
Nav.pack(expand = True)
Main.pack(expand = True)
Footer.pack(expand = True)

Buttons = []
Score = 25
Match_btn = []
Guesses = 0

Label_Score = Label(master = Nav, text = f'Score: {Score}', font = ("Times new roman", 30))   
Label_Score.pack() 
Reset_btn = Button(master = Footer, text = "Reset", font = ("Times new roman", 30), padx = 10, pady = 3)
Reset_btn.pack()
    
def Activate(btn: object, color: str):
    global Match_btn
    global Score
    global Match_btn
    global Label_Score
    global Label_Lost
    global Guesses
            
    if btn['background'] == color:
        btn['background'] = 'grey'
        Match_btn.pop()
    else:
        btn['background'] = color 
        Match_btn.append(btn)
                
    if len(Match_btn) == 2:
        if Match_btn[0]['background'] == Match_btn[1]['background']:
            Match_btn[0].config(command='')
            Match_btn[1].config(command='')
            Match_btn[0]['text'] = color 
            Match_btn[1]['text'] = color
            Guesses += 1
        else:
            Match_btn[0]['background'] = 'grey'
            Match_btn[1]['background'] = 'grey'
            Score -= 1
            Score_Update(Score)
                    
            if Score == 0:
                for btn in Buttons:
                    btn.destroy()    
                        
                Label_Lost.pack(side = TOP, expand = True, fill = BOTH)
                
        if Guesses == 8:
            for btn in Buttons:
                btn.destroy()        
                
            Label_Won.pack(side = TOP, expand = True, fill = BOTH) 
        Match_btn.clear()
                
def Game():
    global Score
    global Guesses
    global Label_Score
    global Buttons
    global Match_btn
    global Label_Lost
    global Label_Won
    global Nav    
            
    Match_btn = []
    Guesses = 0
    Score = 25
    Colors = ['white', 'black', 'red', 'green', 'blue', 'cyan', 'yellow', 'magenta'] * 2
    Score_Update(Score)
        
            
    if len(Buttons):
        Label_Won.destroy()
        Label_Lost.destroy()
        for btn in Buttons:
            btn.destroy()
            
    Label_Won = tk.Label(master = Main, text = "You won!", font = ("Times new roman", 35))
    Label_Lost = tk.Label(master = Main, text = "You lost, try again!", font = ("Times New Roman", 35), )
    
            
    for i in range(4):
        for j in range(4):
            Random_Color = random.randint(0, len(Colors) - 1)
            color = Colors[Random_Color]   
            Square_btn = Button(master = Main, text = f"????", width = 10, height = 3, background = "grey", activebackground = color)
            Buttons.append(Square_btn)
            Square_btn.grid(row = i, column = j, padx = 10, pady = 10)
            Buttons[-1]['command'] = partial(Activate, Square_btn, color)
            Colors.pop(Random_Color)
                    
def Score_Update(Score: int):
    Label_Score['text'] = f"Score: {Score}"
        
Reset_btn['command'] = Game
Game()
window.mainloop()
