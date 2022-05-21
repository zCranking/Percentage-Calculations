from tkinter import *
from tkinter import messagebox
import math as Math

root = Tk()
root.minsize(500, 500)
root.maxsize(1000, 800)
root.config(background="#AFA2FF")
root.title("Percentage Calculations")

grade3percent = Label(root, bg="#AFA2FF", foreground="#D8DAD3", font=("Comic Sans MS", "30", "bold"))
grade5percent = Label(root, bg="#AFA2FF", foreground="#D8DAD3", font=("Comic Sans MS", "30", "bold"))
grade10percent = Label(root, bg="#AFA2FF", foreground="#D8DAD3", font=("Comic Sans MS", "30", "bold"))

class grade3():
    def __init__(self, language, math):
        self.lan = language
        self.math = math
    def lan(self):
        return str(self.lan)
    
    def math(self):
        return str(self.math)
    
    def percentage(self):
        lanMarks = self.lan
        mathMarks = self.math    
        total = lanMarks + mathMarks
        total100 = total * 100
        grade3final = Math.floor(total100 / 200)
        grade3percent['text'] = str(grade3final) + "%"

class grade5():
    def __init__(self, language, math, history):
        self.lan = language
        self.math = math
        self.history = history
        
    def lan(self):
        return str(self.lan)
    
    def math(self):
        return str(self.math)
    
    def history(self):
        return str(self.history)
    
    def percentage(self):
        lanMarks = self.lan
        mathMarks = self.math    
        historyMarks = self.history
        total = lanMarks + mathMarks + historyMarks
        total100 = total * 100
        grade5final = Math.floor(total100 / 300)
        grade5percent['text'] = str(grade5final) + "%"

class grade10():
    def __init__(self, language, math, history, flanguage):
        self.lan = language
        self.math = math
        self.history = history
        self.flanguage = flanguage
        
    def lan(self):
        return str(self.lan)
    
    def math(self):
        return str(self.math)
    
    def history(self):
        return str(self.history)
    
    def flanguage(self):
        return str(self.flanguage)
    
    def percentage(self):
        lanMarks = self.lan
        mathMarks = self.math    
        historyMarks = self.history
        flanguageMarks = self.flanguage
        total = lanMarks + mathMarks + historyMarks + flanguageMarks
        total100 = total * 100
        grade10final = Math.floor(total100 / 400)
        grade10percent['text'] = str(grade10final) + "%"

lan = 100
math = 70
history = 30
flan = 50

grade3 = grade3(lan, math)
grade3button = Button(root, text="Grade 3 Percentage!", command=grade3.percentage)
grade3button.place(relx=0.2, rely=0.8, anchor=CENTER)
grade3percent.place(relx=0.2 , rely=0.6, anchor=CENTER)

grade5 = grade5(lan, math, history)
grade5button = Button(root, text="Grade 5 Percentage!", command = grade5.percentage)
grade5button.place(relx=0.5, rely=0.8, anchor=CENTER)
grade5percent.place(relx=0.5, rely=0.6, anchor=CENTER)

grade10 = grade10(lan, math, history, flan)
grade10button = Button(root, text="Grade 10 Percentage!", command = grade10.percentage)
grade10button.place(relx=0.8, rely=0.8, anchor=CENTER)
grade10percent.place(relx=0.8, rely=0.6, anchor=CENTER)
root.mainloop()