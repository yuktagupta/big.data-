import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mybigdata"]
mycol = mydb["student"]

myquery = { "name": "vai" }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)
 