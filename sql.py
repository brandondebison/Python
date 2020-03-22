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

cursor.close()
db.close()

import gc
gc.collect()
