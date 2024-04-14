from pipeless_agents_sdk.cloud import data_stream
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://miguel:md3IwUQKZg10fqNf@demo.ga9t9gq.mongodb.net/?retryWrites=true&w=majority&appName=yc-demo"
client = MongoClient(uri)
db = client["yc_demo"]
collection = db["yc_demo"]

for payload in data_stream:
  print(f"New data received: {payload.value}, sending to MongoDB")
  try:
    collection.insert_one(payload.value)
    print("Data stored in MongoDB!")
  except Exception as e:
    print(e)



