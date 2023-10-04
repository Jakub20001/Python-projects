# Import modules
from tkinter import *
from tkinter import messagebox
import random

# Define parameters of window
window = Tk()
window.title("Hangman game")
window.geometry("600x600")
window.configure(bg="red")

Label(window, text = "Welcome to Hangman game!", font = ("Courier", 30)).pack()

# Making frames
frame1 = Frame(window, width = 600, height = 50, bd = 2, bg = "blue", relief = 'raise')
frame1.pack(side = TOP, fill = BOTH)
frame2 = Frame(window, width = 600, height = 200, relief = 'raise')
frame2.pack(side = TOP, fill = BOTH)
frame3 = LabelFrame(window, text = 'keys', width = 600, height = 250, bd = 2, relief = "raise")
frame3.pack(side = TOP, fill = BOTH)

# Two more frames in frame 2 to display character and some few informations
lchar_frame = LabelFrame(frame2, width = 300, height = 200, relief = "raise")
lchar_frame.pack(side = LEFT)
rchar_frame = LabelFrame(frame2, text = "Hangman", width = 300, height = 200, bd = 2, relief = 'raise')
rchar_frame.pack(side = RIGHT)

# 3 frames more in lcharframes for status word and enter key
l1char_frame = LabelFrame(lchar_frame, text = "status", width = 300, height = 60, relief = 'raise')
l1char_frame.pack(side=TOP)
l2char_frame = LabelFrame(lchar_frame, text = "word", width = 300, height = 60, relief = 'raise')
l2char_frame.pack(side=TOP)
l3char_frame = LabelFrame(lchar_frame, text = "enter key", width = 300, height = 60, relief = 'raise')
l3char_frame.pack(side=TOP)

def select(value):
    if value == 'Space':
        Entry.insert(END, '')
    else:
        Entry.insert(END,value)
        
Entry = Text(l3char_frame, width = 35, height = 2)
Entry.grid(row=1, columnspan = 40)
        
# almost done now let's make keyboard
buttons=[
'q','w','e','r','t','y','u','i','o','p',
'a','s','d','f','g','h','j','k','l',
'z','x','c','v','b','n','m'
]
varRow = 2
varcolumn = 0
for button in buttons:
    command=lambda x=button: select(x)
    if button != 'Space':
        Button(frame3, text=button, width = 5, font = ('arial', 10, 'bold'), bg = "yellow", command=command, padx = 3, pady = 3, bd = 5).grid(row=varRow, column = varcolumn)
    if button == 'Space':
        Button(frame3, text=button, command=command).grid(row=5, column = varcolumn)
    varcolumn += 1
    if varcolumn > 11 and varRow == 2:
        varcolumn = 0
        varRow += 1
    if varcolumn > 11 and varRow == 3:
        varcolumn = 0
        varRow += 1
        
# play again function and main game body       
def play_again():
    answer = messagebox.askyesno("play again", "Do you want to play again?")
    if answer == "True" or "true":
        play_game() # body of program
    else:
        pass 
def get_word():
    words = ['Palpatine', 'Anakin', 'Luke', 'Dooku', 'Windu', 'Kenobi', 'Padme', 'Ahsoka', 'Leia']         
    return random.choice(words)
def play_game():
    alphabet = "abcdefghijklmnopqrstuwvxyz"
    word = get_word()
    letter_guessed = []
    tries = 10
    guessed = False
    l1 = Label(l2char_frame, text = "The word contain "+ str(len(word)) + " Letters")
    l1.grid(row=0, column = 0)
    l2 = Label(l2char_frame,text='The Word ' + str(len(word)*'*'))
    l2.grid(row = 1, column = 0)
    while guessed == False and tries > 0:
        tries_left = Label(l1char_frame, text = "Tries left: " + str(tries))
        tries_left.grid(row=0, column=0)
        global entry
        guess = input("Enter a letter").lower()
        if len(guess) == 1:
            if guess not in alphabet:
                el = Label(l2char_frame, text = "You have not entered a letter")
                el.grid(row=2, column=0, sticky=W)
            elif guess in letter_guessed:
                el = Label(l2char_frame, text = "You have all guesse a letter")
                el.grid(row=2, column = 0, sticky=W)
            elif guess not in word:
                el = Label(l2char_frame, text = "Sorry, letter not part in word")
                el.grid(row=2, column=0, sticky=W)
                letter_guessed.append(guess)
                tries-=1
            elif guess in word:
                el = Label(l2char_frame, text = "Well done, letter exist in word")
                el.grid(row=2, column = 0, sticky = W)
            else:
                el = Label(l2char_frame, text = "No idea why this message appeared")
                el.grid(row=2, column=0, sticky=W)
        elif len(guess) == len(word):
            if guess == word:
                el = Label(l2char_frame, text = "Well done, you have guessed words")
                el.grid(row=2, column = 0, sticky = W)
                guessed = True 
            else:
                el = Label(l2char_frame, text = "Sorry, that was not in word oop")
                el.grid(row = 2, column = 0, sticky = W)
                tries -= 1
        else:
            el = Label(l2char_frame, text = "The length of guessed word is diff")
            el.grid(row = 2, column = 0, sticky = W)
    status = ""
    if guessed == False:
        for letter in word:
            if letter in letter_guessed:
                status += letter
            else:
                status += '*'
        sl = Label(l1char_frame, text = status)
        sl.grid(row=2, column=0)
    if status == word:
        el = Label(l2char_frame, text = "Well done you guessed the word")
        el.grid(row = 2, column = 0, sticky = W)
        guessed = True
    elif tries == 0:
        el = Label(l2char_frame, text = "You run out of life!")
        el.grid(row = 2, column = 0, sticky = W)    
    
Button(frame1, text='play game', command=play_game).pack()

window.mainloop()



# %%
