#!/usr/local/bin/python3

from tkinter import *

window = Tk()

window.geometry("400x400")
window.title("working with buttons")


label1 = Label(window, text="Please Cick Button")

#define the fucntion to be clicked 
def hasClicked():
    ßlabel1.configure(text="something happened")

button1 = Button(window, text="Submit", highlightbackground='#3E4129', bg='#3E4149', command=hasClicked)

label1.grid(column=0,row=0)
button1.grid(column=1,row=0)






window.mainloop()
