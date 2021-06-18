from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.2evqo.mongodb.net/students?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE"

client = MongoClient(url)

db = client.module_5

print(db.list_collection_names())