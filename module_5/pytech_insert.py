#Michael Lohr
#21310937
#pytech_insert.py
#6/20/21


from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.2evqo.mongodb.net/students?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE"
students = MongoClient(url)

db = students.pytech

collection = db.students

mike = {
"student_id": "1007",
"first_name": "Michael",
"last_name": "Lohr",
"enrollments": [
    {
    "term": "Cohort 2",
    "gpa": "May 25, 2021",
    "end_date": "July 24th, 2021",
    "courses": [
        {
        "course_id": "CSD",
        "description": "Database Development",
        "instructor": "Professor Sampson",
        "grade": "A"

        }
    ]
    }
]
}

student_1 = collection.insert_one(mike).inserted_id
jade = {
"student_id": "1008",
"first_name": "Jade",
"last_name": "Lohr",
"enrollments": [
    {
    "term": "Cohort 2",
    "gpa": "May 25, 2021",
    "end_date": "July 24th, 2021",
    "courses": [
        {
        "course_id": "CSD",
        "description": "Database Development",
        "instructor": "Professor Sampson",
        "grade": "B"

        }
    ]
    }
]
}

student_2 = collection.insert_one(jade).inserted_id
colin = {
"student_id": "1009",
"first_name": "Colin",
"last_name": "Lohr",
"enrollments": [
    {
    "term": "Cohort 2",
    "gpa": "May 25, 2021",
    "end_date": "July 24th, 2021",
    "courses": [
        {
        "course_id": "CSD",
        "description": "Database Development",
        "instructor": "Professor Sampson",
        "grade": "A"

        }
    ]
    }
]
}
student_3 = collection.insert_one(colin).inserted_id

print("Inserted student record Michael Lohr into student collections with document_id " + student_1)
print("Inserted student record Jade Lohr into student collections with document_id " + student_2)
print("Inserted student record Colin Lohr into student collections with document_id " + student_3)


