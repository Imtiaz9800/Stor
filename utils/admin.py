import os

def is_admin(user_id):
    admin_ids = os.getenv("ADMIN_IDS", "6474779115").split(",")
    return str(user_id) in admin_ids
