from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.2evqo.mongodb.net/students?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE"
students = MongoClient(url)

db = students.module_5

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

mike_student_id = students.insert_one(mike).inserted_id

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

jade_student_id = students.insert_many(jade).inserted_id

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
colin_student_id = students.insert_many(colin).inserted_id
print(mike_student_id)
print(jade_student_id)
print(colin_student_id)
