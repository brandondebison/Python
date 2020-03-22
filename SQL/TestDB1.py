#!/usr/local/bin/python3

import MySQLdb

db = MySQLdb.connect(
    host='localhost',
    port=3306,
    user='student',
    passwd='student',
    db='testpython'
) 

cursor = db.cursor()

sql = """INSERT INTO testPerson ( LastName, FirstName, Address, City) VALUES (%s,%s,%s,%s)"""

values = ['Darren7', 'Me7', 'Her7', ' Ther7']

cursor.execute(sql,values)
db.commit()

cursor.execute("SELECT * FROM TestPerson")
data = cursor.fetchall()
print(data)

for row in data:
    id = row[0]
    firstName = row[1]
    lastName = row[2]
    address = row[3]
    city = row[4]
    print( str(id) + " / " + firstName + " " + lastName )

    

cursor.close()
db.close()

import gc
gc.collect()