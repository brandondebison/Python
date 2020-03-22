#!/usr/local/bin/python3

from datetime import datetime


inputTime = input("Please enter a timestamp in YYYY-MM-DD format \n")

tempTime = datetime.strptime(inputTime, "%Y-%m-%d")
compTime = datetime.strptime("2018-06-30", "%Y-%m-%d")

calTime = (tempTime-compTime).days

output = "Number of days are: " + str(calTime)
print(output)

