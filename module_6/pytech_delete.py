#Michael Lohr
#21310937
#pytech_query.py
#6/20/21

from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.2evqo.mongodb.net/students?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE"
students = MongoClient(url)

db = students.pytech

collection = db.students

docs = collection.find({})

print("Displaying student documents from find() Query")

for doc in docs:
     print(doc)

jake = {
"student_id": "1010",
"first_name": "Jacob",
"last_name": "Rowland",
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

student_4 = collection.insert_one(jake).inserted_id
print("Inserted student record Jacob Rowland into student collections with document_id " + str(student_4))
print("Displaying Student test doc")
print(jake)

delete = {"student_id": "1010"}

deleted =  collection.delete_one(delete)

docs = collection.find({})

print("Displaying student documents from find() Query")

for doc in docs:
     print(doc)