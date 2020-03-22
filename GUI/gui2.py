#!/usr/local/bin/python3

from tkinter import *

window = Tk()

window.geometry("400x400")
window.title("working with labels")

# JLabel = new jlabel("Text for label")

lbl_name = Label(window,text="Hello World",font=("Arial Bold",20))
lbl_name.grid(column=0,row=0)

lbl_name2 = Label(window,text=" ")
lbl_name3 = Label(window,text="Over There")
lbl_name4 = Label(window,text=" ")
lbl_name5 = Label(window,text="Test Me")
lbl_name6 = Label(window,text="Why oh why...")

lbl_name2.grid(column=1,row=0)
lbl_name3.grid(column=2,row=0)
lbl_name4.grid(column=0,row=1)
lbl_name5.grid(column=1,row=1)
lbl_name6.grid(column=2,row=1)





window.mainloop()
