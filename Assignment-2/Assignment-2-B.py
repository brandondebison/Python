
from tkinter import ttk
from tkinter import *
import tkinter
from tkinter import messagebox
window = Tk()

window.geometry("600x600")
window.title("Assignment 2 - Question 2")


informationLabel = Label(
    window, text="Please choose a pizza size and your toppings", font='Helvetica 10 bold')
outputLabel = Label(window, text="", font='Helvetica 10 bold')


sizeOptions = ("Select your size", "Small", "Medium", "Large", "Extra-Large")
pizzaSize = ttk.Combobox(window, value=sizeOptions, width=20, justify=CENTER)
pizzaSize.current(0)


#  Toppings
pepperoniVar = IntVar()
pepperoni = Checkbutton(window, text='Pepperoni', variable=pepperoniVar,
                        onvalue=1, offvalue=0, height=1, width=20)

cheeseVar = IntVar()
cheese = Checkbutton(window, text='Cheese', variable=cheeseVar,
                     onvalue=1, offvalue=0, height=1, width=20)

oliveVar = IntVar()
olive = Checkbutton(window, text='Olive', variable=oliveVar,
                    onvalue=1, offvalue=0, height=1, width=20)

pinappleVar = IntVar()
pinapple = Checkbutton(window, text='Pinapple', variable=pinappleVar,
                       onvalue=1, offvalue=0, height=1, width=20)

hamVar = IntVar()
ham = Checkbutton(window, text='Ham', variable=hamVar,
                  onvalue=1, offvalue=0, height=1, width=20)


def hasClicked():
    pString = ""
    cString = ""
    oString = ""
    pinString = ""
    hString = ""
    total = 0.00
    size = pizzaSize.get()
    if size == "Small":
        total = total + 9.00
    elif size == "Medium":
        total = total + 12.50
    elif size == "Large":
        total = total + 15.00
    elif size == "Extra-Large":
        total = total + 17.50
    if pepperoniVar.get() == 1:
        total = total + 1.00
        pString = " - Pepperoni "
    if cheeseVar.get() == 1:
        cString = " - Cheese "
    if oliveVar.get() == 1:
        total = total + 1.00
        oString = " - Olive "
    if pinappleVar.get() == 1:
        total = total + 1.00
        pinString = " - Pinapple "
    if hamVar.get() == 1:
        total = total + 1.00
        hString = " - Ham "

    message = "Your Total is = " + \
        str(total) + " and your toppings are: \n" + \
        pString + cString + oString + pinString + hString
    messagebox.showinfo("Pizza Order", message)


submitButton = Button(window, text="Submit Order", font='Helvetica 10 bold',
                      highlightbackground='#1474a0', bg='#1474a0', command=hasClicked)

informationLabel.pack()
pizzaSize.pack()

pepperoni.pack()
cheese.pack()
olive.pack()
pinapple.pack()
ham.pack()


submitButton.pack()
outputLabel.pack()

window.lift()
window.attributes("-topmost", TRUE)
window.mainloop()
