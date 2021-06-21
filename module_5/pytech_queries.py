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

doc = collection.find_one({"student_id": "1007"})

print("Displaying student documents from find_one() Query")
print(doc)

