from tkinter import *
import tkinter as tk
import math

window = Tk()
window.title("Scientific calculator")
window.geometry("1200x600")
window.configure(bg = "red")
Calculator = Frame(window)
Calculator.grid()

class Calculator():
    def __init__(self):
        self.total = 0
        self.current = ""
        self.input_value = True
        self.check_sum = False
        self.op = ''
        self.result = False


    def numberEnter(self, num):
        self.result = False
        self.firstnum = E.get()
        self.secondnum = str(num)
        if self.input_value:
            self.current = self.secondnum
            self.input_value = False
        else:
            if self.secondnum == '.':
                if self.secondnum in self.firstnum:
                    return
                self.current = self.firstnum + self.secondnum
        self.display(self.current)
        
        
    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)  
        if self.check_sum == True:
            self.valid_function()
        else:
            self.total = float(E.get())
          
    def display(self, value):
        E.delete(0, END)
        E.insert(0, value)
    
    def valid_function(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "sub":
            self.total -= self.current
        if self.op == "multi":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        if self.op == "mod":
            self.total %= self.current
        self.input_value = True 
        self.check_sum = False
        self.display(self.total)
        
    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function() 
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False
    
    def Clear_Entry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value = True
        
    def All_Clear_entry(self):
        self.Clear_Entry()
        self.total = 0
        
    def pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)
        
    def pi2(self):
        self.result = False
        self.current = math.tau
        self.display(self.current)
        
    def PM(self):
        self.result = False
        self.current = -(float(E.get()))
        self.display(self.current)
        
    def square(self):
        self.result = False
        self.current = math.sqrt(float(E.get()))
        self.display(self.current)
        
    def e(self):
        self.result = False
        self.current = math.e  
        self.display(self.current)
        
    def tan(self):
        self.result = False
        self.current = math.tan(math.radians(float(E.get())))
        self.display(self.current) 
        
    def cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(E.get())))
        self.display(self.current)
        
    def sin(self):
        self.result = False
        self.current = math.sin(math.radians(float(E.get())))
        self.display(self.current)
        
    def tanh(self):
        self.result = False
        self.current = math.tanh(math.radians(float(E.get())))
        self.display(self.current)
        
    def cosh(self):
        self.result = False
        self.current = math.cosh(math.radians(float(E.get())))
        self.display(self.current)
        
    def sinh(self):
        self.result = False
        self.current = math.sinh(math.radians(float(E.get())))
        self.display(self.current)
        
    def exp(self):
        self.result = False
        self.current = math.exp(float(E.get())) 
        self.display(self.current)

    def mod(self):
        self.result = False
        self.current = math.mod(float(E.get()))
        self.display(self.current)
        
    def log(self):
        self.result = False
        self.current = math.log(float(E.get()))
        self.display(self.current)

    def log10(self):
        self.result = False
        current = math.log10(float(E.get()))
        self.display(current)
        
    def log2(self):
        self.result = False
        self.current = math.log2(float(E.get()))
        self.display(self.current)

    def log1p(self):
        self.result = False
        self.current = math.log1p(float(E.get()))
        self.display(self.current)
        
    def deg(self):
        self.result = False
        self.current = math.degrees(float(E.get()))
        self.display(self.current)
        
    def expm1(self):
        self.result = False
        self.current = math.expm1(float(E.get()))
        self.display(self.current)
        
    def gamma(self):
        self.result = False
        self.current = math.gamma(float(E.get()))
        self.display(self.current)
        
    def acosh(self):
        self.result = False
        self.current = math.acosh(float(E.get()))
        self.display(self.current)
        
    def asinh(self):
        self.result = False
        self.current = math.asinh(float(E.get()))
        self.display(self.current)
        
    def atanh(self):
        self.result = False
        self.current = math.atanh(float(E.get()))
        self.display(self.current)
        
added_value = Calculator()



B = Button(window, text = "C", font = ("Arial", 30), command = added_value.All_Clear_entry, width = 11, height = 1)
B.place(x = 0, y = 235)

B2 = Button(window, text = "CE",  font = ("Arial", 30), command = added_value.Clear_Entry, width = 11, height = 1)       
B2.place(x = 263, y = 235)

B3 = Button(window, text = "√", font = ("Arial", 30), command = added_value.square, width = 11, height = 1)
B3.place(x = 526, y = 235)

B4 = Button(window, text = "+", font = ("Arial", 30), command=lambda: added_value.operation("add"), width = 11, height = 1)
B4.place(x = 789, y = 235)

B5 = Button(window, text = "-", font = ("Arial", 30), command=lambda: added_value.operation("sub"), width = 11, height = 1)
B5.place(x = 1052, y = 235)

B6 = Button(window, text = "X", font = ("Arial", 30), command=lambda: added_value.operation("multi"), width = 11, height = 1)
B6.place(x = 1315, y = 235)

B7 = Button(window, text = "/", font = ("Arial", 30), command=lambda: added_value.operation("divide"), width = 11, height = 1)
B7.place(x = 1578, y = 235)

B8 = Button(window, text = "=", font = ("Arial", 30), command = added_value.sum_of_total, width = 11, height = 1)
B8.place(x = 0, y = 313)

B9 = Button(window, text = "+-", font = ("Arial", 30), command = added_value.PM, width = 11, height = 1)
B9.place(x = 263, y = 313)

B10 = Button(window, text = ".", font = ("Arial", 30), command= lambda: added_value.numberEnter('.'), width = 11, height = 1)
B10.place(x = 526, y = 313)

B11 = Button(window, text = "0", font = ("Arial", 30), command=lambda: added_value.numberEnter(0), bg = 'orange', width = 11, height = 1)
B11.place(x = 789, y = 313)

B12 = Button(window, text = "1", font = ("Arial", 30), command=lambda: added_value.numberEnter(1), bg = 'orange', width = 11, height = 1)
B12.place(x = 1052, y = 313)

B13 = Button(window, text = "2", font = ("Arial", 30), command=lambda: added_value.numberEnter(2), bg = 'orange', width = 11, height = 1)
B13.place(x = 1315, y = 313)

B14 = Button(window, text = "3", font = ("Arial", 30), command=lambda: added_value.numberEnter(3), bg = "orange", width = 11, height = 1)
B14.place(x = 1578, y = 313)

B15 = Button(window, text = "4", font = ("Arial", 30), command=lambda: added_value.numberEnter(4), bg = "orange", width = 11, height = 1)
B15.place(x = 0, y = 391)

B16 = Button(window, text = "5",  font = ("Arial", 30), command=lambda: added_value.numberEnter(5), bg = "orange", width = 11, height = 1)
B16.place(x = 263, y = 391)

B17 = Button(window, text = "6",  font = ("Arial", 30), command=lambda: added_value.numberEnter(6), bg = "orange", width = 11, height = 1)
B17.place(x = 526, y = 391)

B18 = Button(window, text = "7", font = ("Arial", 30), command=lambda: added_value.numberEnter(7), bg = "orange", width = 11, height = 1)
B18.place(x = 789, y = 391)

B19 = Button(window, text = "8", font = ("Arial", 30), command=lambda: added_value.numberEnter(8), bg = "orange", width = 11, height = 1)
B19.place(x = 1052, y = 391)

B20 = tk.Button(window, text = "9", font = ("Arial", 30), command=lambda: added_value.numberEnter(9), bg = "orange", width = 11, height = 1)
B20.place(x = 1315, y = 391)

B21 = tk.Button(window, text = "pi", font = ("Arial", 30), command= added_value.pi, bg = 'light green', width = 11, height = 1)
B21.place(x = 1578, y = 391)

B22 = tk.Button(window, text = "2pi", font = ("Arial", 30), command = added_value.pi2, bg = "light green", width = 11, height = 1)
B22.place(x = 0, y = 469)

B23 = tk.Button(window, text = "log", font = ("Arial", 30), command = added_value.log, bg = "light green", width = 11, height = 1)
B23.place(x = 263, y = 469)

B24 = tk.Button(window, text = "log10", font = ("Arial", 30), command = added_value.log10, bg = "light green", width = 11, height = 1)
B24.place(x = 526, y = 469)

B25 = tk.Button(window, text = "log2", font = ("Arial", 30), command = added_value.log2, bg = "light green", width = 11, height = 1)
B25.place(x = 789, y = 469)

B26 = tk.Button(window, text = "Cos", font = ("Arial", 30), command = added_value.cos, bg = "light green", width = 11, height = 1)
B26.place(x = 1052, y = 469)

B27 = tk.Button(window, text = "tan", font = ("Arial", 30), command = added_value.tan, bg = "light green", width = 11, height = 1)
B27.place(x = 1315, y = 469)

B28 = tk.Button(window, text = "sin", font = ("Arial", 30), command = added_value.sin, bg = "light green", width = 11, height = 1)
B28.place(x = 1578, y = 469)

B29 = tk.Button(window, text = "Cosh", font = ("Arial", 30), command = added_value.cosh, bg = "light green", width = 11, height = 1)
B29.place(x = 0, y = 547)

B30 = tk.Button(window, text = "tanh", font = ("Arial", 30), command = added_value.tanh, bg = 'light green', width = 11, height = 1)
B30.place(x = 263, y = 547)

B31 = tk.Button(window, text = "sinh", font = ("Arial", 30), command = added_value.sinh, bg = 'light green', width = 11, height = 1)
B31.place(x = 526, y = 547)

B32 = tk.Button(window, text = "exp", font = ("Arial", 30), command = added_value.exp, bg = "light green", width = 11, height = 1)
B32.place(x = 789, y = 547)

B33 = tk.Button(window, text = "Mod", font = ("Arial", 30), command=lambda:  added_value.operation("mod"), bg = "light green", width = 11, height = 1)
B33.place(x = 1052, y = 547)

B34 = tk.Button(window, text = "e", font = ("Arial", 30), command = added_value.e, bg = "light green", width = 11, height = 1)
B34.place(x = 1315, y = 547)

B35 = tk.Button(window, text = "log1p", font = ("Arial", 30), command= added_value.log1p, bg = "light green", width = 11, height = 1)
B35.place(x = 1578, y = 547)

B36 = tk.Button(window, text = "expm1", font = ("Arial", 30), command= added_value.expm1, bg = "light green", width = 11, height = 1)
B36.place(x = 0, y = 625)

B37 = tk.Button(window, text = "gamma", font = ("Arial", 30), command= added_value.gamma, bg = "light green", width = 11, height = 1)
B37.place(x = 263, y = 625)

B38 = tk.Button(window, text = "deg", font = ("Arial", 30), command= added_value.deg, bg = "light green", width = 11, height = 1)
B38.place(x = 526, y = 625)

B39 = tk.Button(window, text = "acosh", font = ("Arial", 30), command= added_value.acosh, bg = "light green", width = 11, height = 1)
B39.place(x = 789, y = 625)

B40 = tk.Button(window, text = "asinh", font = ("Arial", 30), command= added_value.asinh, bg = "light green", width = 11, height = 1)
B40.place(x = 1052, y = 625)

B41 = tk.Button(window, text = "atanh", font = ("Arial", 30), command= added_value.atanh, bg = "light green", width = 11, height = 1)
B41.place(x = 1315, y = 625)

L = Label(window, text = "Scientific calculator",
          font = ("Courier", 30, 'bold'),
          bg = 'black', fg = 'white')
L.grid(row = 0, column = 30, columnspan = 4)

E = Entry(window, font = ("Courier", 30, "bold"),
          bg = 'white', fg = 'black', justify = RIGHT)
E.grid(row = 6, column = 30, columnspan = 4)
E.insert(0, "0")


window.mainloop()
