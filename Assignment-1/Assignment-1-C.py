#!/usr/local/bin/python3

#require "custom_library.py"

# def addThem(num1, num2):
#     return (num1 + num2)

# def subtractThem(num1, num2):
#     return (num1 - num2)
    
# def multiplyThem(num1, num2):
#     return (num1 * num2)
    
# def divideThem(num1, num2):
#     return (num1 / num2)

from custom_library import *


temp1 = input("Please enter a number: \n")

temp2 = input("Please enter another number: \n")

num1 = float(temp1)
num2 = float(temp2)

added = addThem( num1, num2 )
subbed = subtractThem( num1, num2 )
multi = multiplyThem( num1, num2 )
divi = divideThem( num1, num2 )

addMsg = str(num1) +" plus "+ str(num2)+ " is " +str(added)
print(addMsg)

subMsg = str(num1) +" minus "+ str(num2)+ " is " +str(subbed)
print(subMsg)

multiMsg = str(num1) +" times "+ str(num2)+ " is " +str(multi)
print(multiMsg)

diviMsg = str(num1) +" divided "+ str(num2)+ " is " +str(divi)
print(diviMsg)

