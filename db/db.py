from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from config.config import setting

url =  setting.mongo_url

client = MongoClient(url, server_api=ServerApi('1'))

db = client.medicure_db

collection_user = db["user"]
collection_disease = db["disease"]