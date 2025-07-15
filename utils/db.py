from pymongo import MongoClient
import os

MONGO_DB_URI = os.getenv("MONGO_DB_URI")
client = MongoClient(MONGO_DB_URI)
db = client.files
collection = db.file_data

def insert_file(message):
    file_info = {
        "msg_id": message.id,
        "chat_id": message.chat.id,
        "file_name": message.document.file_name if message.document else None,
        "mime": message.document.mime_type if message.document else None,
        "size": message.document.file_size if message.document else None
    }
    collection.insert_one(file_info)

def get_file(msg_id):
    return collection.find_one({"msg_id": int(msg_id)})
