import os
from pymongo import MongoClient

client = MongoClient(os.getenv("MONGODB_URI"))
db = client["telegram_bot"]
users = db["users"]

def get_or_create_user(user_id):
    user = users.find_one({"user_id": user_id})
    if not user:
        users.insert_one({"user_id": user_id, "coins": 0})
    return users.find_one({"user_id": user_id})

def get_user(user_id):
    return users.find_one({"user_id": user_id}) or {"coins": 0}

def update_user_balance(user_id, coins):
    users.update_one({"user_id": user_id}, {"$inc": {"coins": coins}})