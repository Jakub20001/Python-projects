from tkinter import *

window = Tk()
window.title("Mad Libs generator")
window.configure(bg = "yellow")
window.geometry("800x600")

L = Label(window, text = "Welcome to mad libs generator", font = ("Courier", 20))
L.pack()

L2 = Label(window, text = "Click any one", font = ("Courier", 20))
L2.pack()

def madLibs1():
    movie = input("Enter the best polish movie in 1970s")
    director = input("Enter the director of this movie")
    actor_playing_main_role = input("Enter the name of actor playing the main role")
    name_of_character = input("Enter the name of character played by actor")
    print("In the movie ", movie, "in the directory of ", director, "popular actor: ", actor_playing_main_role, "played ", name_of_character, ". ")

def madLibs2():
    name_of_company = input("Enter the name of company")
    name_of_owner_of_company = input("Enter the name of owner")
    area_of_company = input("Enter the area of company")
    effect_of_company = input("Enter the information what product has been made")
    print("Company named ", name_of_company, "was made by ", name_of_owner_of_company, "in area named ", area_of_company, "effect of this company was ", effect_of_company, ". ")


def madLibs3():
    area_of_science = input("Enter the area of science")
    name_of_scientist = input("Enter the name of a scientist")
    product_of_work = input("Enter the product of work")
    print("Scientist named", name_of_scientist, "in area of science called", area_of_science, "discovered", product_of_work, ". ")
    
B = Button(window, text = "Cinematography", font = ("Courier", 15), command = madLibs1)
B.pack()

B2 = Button(window, text = "Business", font = ("Courier", 15), command = madLibs2)
B2.pack()

B3 = Button(window, text = "Science", font = ("Courier", 15), command = madLibs3)
B3.pack()
    
B4 = Button(window, text = "Quit", font = ("Courier", 15), command = window.destroy)
B4.pack()

window.mainloop()
