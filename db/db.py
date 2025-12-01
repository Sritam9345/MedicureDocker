from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri =  "mongodb+srv://situnandananda_db_user:smTjhMrSC3wUqcK3@cluster0.qasb1vx.mongodb.net/?appName=Cluster0"

client = MongoClient(uri, server_api=ServerApi('1'))

db = client.medicure_db

collection_user = db["user"]
collection_disease = db["disease"]