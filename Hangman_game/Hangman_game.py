from tkinter import *
import random
import tkinter.messagebox as msg


window = Tk()

window.title("Hangman game!")

window.geometry("800x600")

window.configure(bg="red")

L = Label(window, text = "Welcome to Hangman game!", font = ("Courier", 30))
L.pack()

canvas = Canvas(window, width = 800, height = 300)
canvas.pack(pady = 30)
canvas.create_line(150, 260, 250, 260, width = 3)
canvas.create_line(200, 260, 200, 40, width = 3)
canvas.create_line(200, 90, 250, 40, width = 3)
canvas.create_line(200, 40, 300, 40, width = 3)
canvas.create_line(300, 40, 300, 70, width = 3)
canvas.create_oval(280, 70, 320, 100, width = 3)
c5 = canvas.create_line(300, 100, 300, 180, width = 3)
c4 = canvas.create_line(300, 105, 270, 155, width = 3)
c3 = canvas.create_line(300, 105, 330, 155, width = 3)
c2 = canvas.create_line(300, 180, 270, 230, width = 3)
c1 = canvas.create_line(300, 180, 330, 230, width = 3)

def choose():
    with open("quest.txt", "r") as file:
        words = file.read().split(", ")
    pick = random.choice(words)
    return pick

def scramble(word):
    random_word = random.sample(word, len(word))
    scrambled = ''.join(random_word)
    return scrambled

def validate():
    global count, picked_word, c1, c2, c3, c4, c5, show
    if check.get() == picked_word:
        picked_word = choose()
        show = scramble(picked_word)
        check.set("")
        lbl.config(text = show)
    else:
        if count == 1 and check.get() != picked_word:
            count += 1
            canvas.delete(c1)
        elif count == 2 and check.get() != picked_word:
            count += 1
            canvas.delete(c2)
        elif count == 3 and check.get() != picked_word:
            count += 1
            canvas.delete(c3)
        elif count == 4 and check.get() != picked_word:
            count += 1
            canvas.delete(c4)
        elif count == 5 and check.get() != picked_word:
            count += 1
            canvas.delete(c5)
            msg.showwarning("Game Over", "Please Try Again...")
            c1 = canvas.create_line(300, 180, 330, 230, width = 3)
            c2 = canvas.create_line(300, 180, 270, 230, width = 3)
            c3 = canvas.create_line(300, 105, 330, 155, width = 3)
            c4 = canvas.create_line(300, 105, 270, 155, width = 3)
            c5 = canvas.create_line(300, 100, 300, 180, width = 3)
        if count == 6:
            count = 1
        check.set("")


def process(event=""):
    global correct
    if check.get().isalpha():
        correct = TRUE
        validate()
    else:
        correct = FALSE
        msg.showerror('Error', 'Please make use of only Alphabets')
        
count = 1
picked_word = choose()
check = StringVar()
show = scramble(picked_word)
correct = NONE

lbl = Label(window, text = show, font = ("Candara", 25, "bold"))
lbl.pack()

txt = Entry(window, textvariable = check, font = ("Candara", 25, "bold"), justify = CENTER, relief = GROOVE, bd = 2)
txt.pack(pady = 10)

btn = Button(window, text = "SUBMIT", font = ("Candara", 25, "bold"), relief = GROOVE, bg = "#E3FFDC", command=process)
btn.pack(pady=20)
window.bind('<Return>', process)

window.mainloop()
