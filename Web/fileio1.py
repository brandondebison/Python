#!/usr/local/bin/python3

file = open('testfile.txt','w') # write will clear and write the input
file.write('hello there\n')
file.write('how are you\n')
file.close()

file = open('testfile.txt','a') #use this to add to file
file.write('I am fine\n')
file.close()

file = open('testfile.txt','r')
myLine = file.readline()
print('My line is: %s' % myLine)
file.close()


file = open('testfile.txt','r')
lines = file.readlines()
myLines=""
for line in lines:
    myLines += line
print(myLines)
file.close()