from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.2evqo.mongodb.net/students?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE"
students = MongoClient(url)

db = students.module_5

docs = db.module_5.find()

for doc in docs:
     print(doc)
    
