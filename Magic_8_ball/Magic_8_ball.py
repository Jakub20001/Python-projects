from tkinter import *
from tkinter import messagebox
import os
import random
from PIL import ImageTk, Image  # type: ignore


window = Tk()
window.title("Magic 8 ball game")
window.configure(bg = "green")
window.geometry("800x600")

L = Label(window, text = "Welcome to magic 8 ball game", font = ("Courier", 20))
L.pack()

magic_8_ball_images = []
folder_dir = "D:/Języki programowania/Python/Projekty/Magic_8_ball_game/8ball_images"

for images in os.listdir(folder_dir):
    if images.endswith(".jpg"):
        image = ImageTk.PhotoImage(Image.open(folder_dir + "/" + images).resize((400, 350)))
        magic_8_ball_images.append(image)
        
print("Total image available: ", len(magic_8_ball_images))

def AskQuestion(event):
    if len(E.get()) == 0:
        messagebox.showinfo("Ball says: ", "Enter a Question First ")
    else:
        ShowAnswer()

def ShowAnswer():
    num = random.randint(0, len(magic_8_ball_images) - 1)
    L2.config(image = magic_8_ball_images[num])
    E.delete(0, "end")
 
   
L2 = Label(window, image = magic_8_ball_images[4])
E = Entry(window, width = 30, font = ("Arial 18 bold"))
B = Button(window, text = "Ask the question from magic 8 ball", font = ("Arial 20 bold"), bg = "plum")


L2.pack()
E.pack(pady = 10)
B.pack(side = "bottom", pady = 30)

B.bind("<Button-1>", AskQuestion)
E.bind("<Return>", AskQuestion)


window.mainloop()
