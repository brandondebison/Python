#!/usr/local/bin/python3

from datetime import datetime

#import javax.swing.JOptionPane 
#from javax.swing import JOptionPane

presentTime = datetime.now()

print(presentTime)

shortTime = presentTime.strftime("%Y-%m-%d")
print(shortTime)


#there is no string to time in function in python
# you need to convert a string to datetime object and then manipulate

nowTime2 = datetime.strptime("2018-01-15 11:22:00", "%Y-%m-%d %h:%m:%s")
print(nowTime2)
