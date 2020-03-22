#!/usr/local/bin/python3

list1 = ["cat", "dog", "panda", "orange"]
print(list1)

list1[3] = "harry"
print(list1)

list2 = ["barbie" , "ken", "elmo", "ernie", "fozzy", "dave"]

list2[5] =  "kermit"
# list2[6] =  "janice" does not work 

list2.append("Janice") # this allows you to add things to the array aka a list 
# array_push is what you would use in php 

print(list2)

print(list2.index("fozzy"))

list2.remove("fozzy")
print(list2)

sesame = list2.pop(2) # this removes out a part that you need removed in the middle of the list 
print(sesame)
print(list2)

list2.reverse()
print(list2)

list2.sort() 
print(list2)

myTuple = ("Hello" , "goodbye", 1, 2, 44.4)
myTuple2 = ("olleh" , "eybdoog", -1, -2, -44.4)
myTuple3 = ("Hello" , "goodbye", 1, 2, 44.4)


#not finished, took phone call 