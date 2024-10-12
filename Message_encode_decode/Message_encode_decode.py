from tkinter import *
import base64

window = Tk()
window.title("Message encode decode")
window.configure(bg = "green")
window.geometry("800x600")


Text = StringVar()
private_key = StringVar()
mode = StringVar()
Result = StringVar()

def Encode(key, message):
    enc = []
    
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def Decode(key, message):
    dec = []
    message = base64.urlsafe_b64decode(message).decode()
    
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i]) - ord(key_c)) % 256))
    return "".join(dec)

def Mode():
    if(mode.get() == "e"):
        Result.set(Encode(private_key.get(), Text.get()))
    elif(mode.get() == "d"):
        Result.set(Decode(private_key.get(), Text.get()))
    else:
        Result.set('Invalid mode')
        
def Reset():
    Text.set("")
    private_key.set("")
    mode.set("")
    Result.set("")
    
L = Label(window, text = "Welcome to encode-decode app", font = ("Courier", 20))
L.pack()

B1 = Button(window, text = "Reset", font = ("Courier", 20), command = Reset)
B1.pack()

B2 = Button(window, text = "Exit", font = ("Courier", 20), command = window.destroy)
B2.pack()

L2 = Label(window, text = "Message", font = ("Courier", 30))
L2.place(relx = 0.0, rely = 0.5, anchor = "w")

E = Entry(window, textvariable = Text, font = ("Courier", 30))
E.place(relx = 0.4, rely = 0.5, anchor = "w")

L3 = Label(window, text = "Key", font = ("Courier", 30))
L3.place(relx = 0.0, rely = 0.6, anchor = "w")

E2 = Entry(window, textvariable = private_key, font = ("Courier", 30))
E2.place(relx = 0.4, rely = 0.6, anchor = "w")

L4 = Label(window, text = "Mode(e-encode, d-decode)", font = ("Courier", 30))
L4.place(relx = 0.0, rely = 0.7, anchor = "w")

E3 = Entry(window, textvariable = mode, font = ("Courier", 30))
E3.place(relx = 0.4, rely = 0.7, anchor = "w")

B = Button(window, text = "Result", font = ("Courier", 30), command = Mode)
B.place(relx = 0.0, rely = 0.8, anchor = "w")

E4 = Entry(window, textvariable = Result, font = ("Courier", 30))
E4.place(relx = 0.4, rely = 0.8, anchor = "w")



window.mainloop()
