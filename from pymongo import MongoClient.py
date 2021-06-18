from pymongo import MongoClient

url = ""

client = MongoClient(mongodb+srv://admin:<password>@cluster0.2evqo.mongodb.net/myFirstDatabase?retryWrites=true&w=majority)

db = client.pytech

print(db.list_collection_names)
