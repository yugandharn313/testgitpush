import pymongo
client = pymongo.MongoClient("mongodb+srv://Yugandhar:Yesh1456@cluster.0lweolz.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
d={
    "name":"Yugandhar",
    "email":"good@gmail.com",
    "nature":"good"
}
database=client["mongotest"]
collection=database['test']
collection.insert_one(d)