#!/usr/local/bin/python3

import math


leave = 0

while (leave == 0):

    realNumber = input("Please enter a real number: \n")

    try:
        val = float(realNumber)
        print("You number is: ", val)

        ceilTemp = math.ceil(val)
        ceilMsg = "Ceil = " + str(ceilTemp)
        print(ceilMsg)

        floorTemp = math.floor(val)
        floorMsg = "Floor = " + str(floorTemp)
        print(floorMsg)

        roundTemp = round(val)
        roundMsg = "Round = " + str(roundTemp)
        print(roundMsg)

        break

    except ValueError:
        print("No.. input is not a number. It's a string\n")
