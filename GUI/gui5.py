#!/usr/local/bin/python3

from tkinter import *

window = Tk()

window.geometry("400x400")
window.title("working with text fields")


label1 = Label(window, text="Please Cick Button")



from tkinter import ttk

numbers = ("Choose numbers", 1, 2, "Three", "four", 5)

select1 = ttk.Combobox(window, value=numbers, width = 20)

select1.current(0)


def hasClicked():
    msg = "I Selected " + select1.get()
    label1.configure(text=msg)

button1 = Button(window, text="Submit", highlightbackground='#1474a0', bg='#1474a0', command=hasClicked)

label1.grid(column=0,row=0)
button1.grid(column=1,row=0)
select1.grid(column=0, row=1)





window.mainloop()
