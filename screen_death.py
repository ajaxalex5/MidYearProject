from tkinter import *


class Deathscreen(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        Canvas(self, bg="#cc7130", width=550, height=300, bd=0, highlightthickness=0).grid(row=0, column=0,columnspan=6, rowspan=6)
        Label(self,
              text = "You are dead :(",
              bg = "#cc7130",
              fg = "Black",
              font = ("Fixedsys 40"),
             ). grid(row=0, column=1, columnspan = 4)
        Button(self,
               text = "Play Again",
               font = ("Fixedsys 16"),
               bg ="#8B4513",
               command= quit
               ).grid(row=2,column=1,sticky=W)
        Button(self,
               text="Main Menu",
               font=("Fixedsys 16"),
               bg="#8B4513",
               command=quit
               ).grid(row=2, column=2, sticky=W)
        Button(self,
               text="Exit",
               font=("Fixedsys 16"),
               bg="#8B4513",
               command = quit
               ).grid(row=2, column=3, sticky=W)
    def test(self):
        print(" ")