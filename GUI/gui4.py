#!/usr/local/bin/python3

from tkinter import *

window = Tk()

window.geometry("400x400")
window.title("working with text feilds")


label1 = Label(window, text="Please Cick Button")

text1 = Entry(window, width=10)
text1.focus()



#define the fucntion to be clicked 
def hasClicked():
    msg = "something has happened to " + text1.get()
    label1.configure(text=msg)

button1 = Button(window, text="Submit", highlightbackground='#1474a0', bg='#1474a0', command=hasClicked)

label1.grid(column=0,row=0)
button1.grid(column=1,row=0)
text1.grid(column=0, row=1)







window.mainloop()
