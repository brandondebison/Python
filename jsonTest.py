#!/usr/local/bin/python3
import json 

json_students = '''
{
    "students": [
        {
            "first_name":"Student 1 FN",
            "last_name":"Student 1 LN"
        },
        {
            "first_name":"Student 2 FN",
            "last_name":"Student 2 LN"
        }
    ]


}'''

decoded_students = json.loads(json_students)
for student in decoded_students["students"]:
    print(student["first_name"])
    print(student["last_name"])