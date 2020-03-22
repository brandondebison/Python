#!/usr/local/bin/python3
import MySQLdb;
import MySQLdb.cursors;
db = MySQLdb.connect(host='localhost', port=3306, user='student', 
                        passwd='student', db='test_python', 
                        cursorclass=MySQLdb.cursors.DictCursor);
cursor = db.cursor( );



cursor.execute("SELECT * FROM TestPerson");
data = cursor.fetchall();
print(data);

for row in data:
    id = row["PersonID"];
    lastName = row["LastName"];
    firstName = row["FirstName"];
    address = row["Address"];
    city = row["City"];
    print(str(id) + " / " + firstName + " " + lastName);

cursor.close();
db.close();

import gc;

gc.collect();
