#!/usr/local/bin/python3

sum = 0

for i in range (0,10) :
    # print(sum)
    sum += i 
    if (i == 5) : break

print(sum)


sum2 = 0

for i in range (0,10) :
    # print(sum2)
    if (i == 5) : continue # this will exclude 5 for the addition 
    sum2 += i 


print(sum2)

list2 = ["barbie", "ken", "elmo", "ernie", "fozzy", "dave"]

#foreach ($list2 as $list) in php there is none for python 

for person in list2 : 
    print(person) 

i = 0 
sum = 0 
while (sum < 100) :
    if (sum + i > 100): break
    sum += i
    i += 1

print(sum) 


