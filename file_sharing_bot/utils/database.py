from pymongo import MongoClient
import config

client = MongoClient(config.DATABASE_URL)
db = client['file_sharing_bot']

def initialize_user(user_id):
    user = db.users.find_one({'user_id': user_id})
    if not user:
        db.users.insert_one({'user_id': user_id, 'coins': 0})

def update_coins(user_id, coins):
    db.users.update_one({'user_id': user_id}, {'$inc': {'coins': coins}})
  
