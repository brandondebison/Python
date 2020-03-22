#!C:/Users/Brandon/AppData/Local/Programs/Python/Python38-32/python.exe
from tkinter import *

window = Tk()

window.geometry("400x400")
window.title("Assignment 2 - Question 1")


label1 = Label(window, text="Please enter a grade", font='Helvetica 10 bold')
outputLabel = Label(window, text="", font='Helvetica 10 bold')

inputBox = Entry(window, width=10)
inputBox.focus()



def hasClicked():
    string = inputBox.get()
    if (len(string) == 0) :
        outputLabel.configure(text="Text box is empty", font='Helvetica 10 bold', highlightbackground='#ff0000',bg='#ff0000')
    else :
        try:
            # outputLabel.configure(text="Before Grade")
            grade = float(string)
            if(grade > 100):
                outputLabel.configure(text="The Number is too high", font='Helvetica 10 bold')
            elif(grade < 0):
                outputLabel.configure(text="The number is too low", font='Helvetica 10 bold')
            elif(grade >= 85 and grade <= 100):
                outputLabel.configure(text="Your Grade is A", font='Helvetica 10 bold')
            elif (grade >=75 and grade <= 84.99): 
                outputLabel.configure(text="Your Grade is B", font='Helvetica 10 bold')
            elif (grade >=60 and grade <= 75.99): 
                outputLabel.configure(text="Your Grade is C", font='Helvetica 10 bold')
            else :
                outputLabel.configure(text="Your Grade is F", font='Helvetica 10 bold')

        except ValueError:
            try:
                if(len(string) > 1):
                    outputLabel.configure(text="Your entry is not valid, please enter a number or letter grade", font='Helvetica 10 bold')
                    
                if(string == "A" or string == "a"):
                    outputLabel.configure(text="Your Grade is between 85 - 100", font='Helvetica 10 bold')
                elif (string == "B" or string == "b"): 
                    outputLabel.configure(text="Your Grade is between 75 - 84.99", font='Helvetica 10 bold')
                elif (string == "C" or string == "c"): 
                    outputLabel.configure(text="Your Grade is between 60 - 74.99", font='Helvetica 10 bold')
                elif (string == "F" or string == "f"):
                    outputLabel.configure(text="Your Grade is between 0 - 59.99", font='Helvetica 10 bold')

            except ValueError:
                outputLabel.configure(text="Your entry is not valid, please enter a number or letter grade", font='Helvetica 10 bold')

        

button1 = Button(window, text="Submit", font='Helvetica 10 bold', highlightbackground='#1474a0', bg='#1474a0', command=hasClicked)

label1.grid(column=1,row=1)
button1.grid(column=1,row=3)
inputBox.grid(column=1, row=2)
outputLabel.grid(column=1,row=4)



window.mainloop()
