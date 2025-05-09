from utils.database import db

def deduct_coins(user_id, amount):
    """
    Deducts a specified amount of coins from a user's balance.
    
    Args:
        user_id (int): The Telegram user ID.
        amount (int): The number of coins to deduct.
    
    Returns:
        bool: True if the deduction was successful, False otherwise.
    """
    user = db.users.find_one({'user_id': user_id})
    if user and user['coins'] >= amount:
        db.users.update_one({'user_id': user_id}, {'$inc': {'coins': -amount}})
        return True
    return False

def get_user_coins(user_id):
    """
    Retrieves the current coin balance for a user.
    
    Args:
        user_id (int): The Telegram user ID.
    
    Returns:
        int: The number of coins the user has, or 0 if the user is not found.
    """
    user = db.users.find_one({'user_id': user_id})
    if user:
        return user.get('coins', 0)
    return 0

def add_coins(user_id, amount):
    """
    Adds a specified amount of coins to a user's balance.
    
    Args:
        user_id (int): The Telegram user ID.
        amount (int): The number of coins to add.
    """
    db.users.update_one({'user_id': user_id}, {'$inc': {'coins': amount}}, upsert=True)
  
