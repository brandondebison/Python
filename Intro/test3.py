#!/usr/local/bin/python3

myString = "Test"

myString2 = 'test'

#concatonate

#myString3 = myString + myString2

print(myString)

myString3 = " Hello everyone! "
myString3b = "Hello"

myString3a = "67"


print(myString3)



print(myString3.strip()) #this will take any extra spaces around the string

#will return true if u only have alphabetical, will return false

#if you have other thing slike spaces

print(myString3b.isalpha()) # this will check to see if there are nothing by letters (spaces are not alpha)

print(myString3.isnumeric())
print(myString3a.isnumeric())



myString4 = "Hello. I must be going!"
print(myString4[0])

#php equivalent => myString4.charAt(0) or substr(myString4,0,1)

print(myString4[1:5])
print(myString4.find("be"))
print(myString4.replace("!"," to school!"))


# $s1 = 'cat'; $s2 = 'dog'; $s3 = $s1.$s2; to concatinate you use the . to combine for php 

s1 = "cat"
s2 = "dog"
s3 = s1.join(s2)
print(s3) 
s3 = s1+s2
print(s3) 

myInput = "cat, dog, fish, panda, bieber"
print(myInput.split(", "))

#this is at min 20 min for the video 








