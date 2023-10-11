from .mongoDB import client
from flask_login import current_user

def cart_length():
    db = client["amazon"]
    collection_name="cart"
    collection= db[collection_name]
    cart = collection.find_one({"user_id": current_user.id})
    if cart:
        return len(cart["products"])
    else:
        return 0