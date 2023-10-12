import os
from flask import Blueprint, render_template,url_for, jsonify,g, request, redirect, flash, current_app
import sqlite3
from flask_login import login_required,current_user,logout_user
from .APIs.mongoDB import client
from bson import ObjectId

# from .login import User
root = Blueprint('root',__name__)

def cart_length(id):
    db = client["amazon"]
    collection_name="cart"
    collection= db[collection_name]
    cart = collection.find_one({"user_id": id})
    if cart:
        return len(cart["products"])
    else:
        return 0


@root.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for("root.home"))
    return render_template('welcome.html')
def conn_db():
    db = getattr(g,'_database',None)
    if db is None:
        db = g._database = sqlite3.connect('user_data.db')
        create_user_table(db)
    
    return db
        
def close_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# Create a table if it doesn't exist
def create_user_table(db):
    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password text NOT NULL,
            fullname text
        )
    ''')
    db.commit()

@root.route('/users')
def show_users():
    # Fetch all user data from the database
    db = conn_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()

    # Pass the user data to the template
    return jsonify(users)

@root.route('/home')
@login_required
def home():
    cart_len = cart_length(current_user.id)
    return render_template('home.html', cart_len=cart_len)
@root.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('root.index'))

db = client["amazon"]
collection_name="products"
collection= db[collection_name]
@root.route("/products/<category>")
@login_required
def productsByCategory(category):
    products = list(collection.find({"category":category}))
    cart_len = cart_length(current_user.id)
    return render_template('products.html',products=products, category=category, cart_len=cart_len)

@root.route("/products/<category>/<product_id>")
@login_required
def product(category,product_id):
    product = collection.find_one({"_id":ObjectId(product_id)})
    cart_len = cart_length(current_user.id)
    return render_template('product.html',product=product, category=category, cart_len=cart_len)

@root.route("/products/<category>/<product_id>/add_to_cart", methods=["POST"])
@login_required
def add_to_cart(category,product_id):
    quantity = int(request.form.get("quantity"))
    cart_collection = db["cart"]
    product = collection.find_one({"_id":ObjectId(product_id)})
    product["quantity"] = quantity
    amount_available = product["amount_available"]
    if quantity > amount_available:
        quantity = amount_available
        flash(f"Quantity exceeded the available amount. Maximum quantity added to cart is {amount_available}.", "warning")
    cart = cart_collection.find_one({"user_id": current_user.id})
    if cart:
        # Check if the product already exists in the cart
        for p in cart["products"]:
            if p["_id"] == product["_id"]:
                # If it does, increment the quantity
                if int(p["quantity"]) + int(quantity) > amount_available:
                    p["quantity"] = amount_available
                    flash(f"Quantity exceeded the available amount. Maximum quantity added to cart is {amount_available}.", "warning")
                else:
                    p["quantity"] = int(p["quantity"]) + int(quantity)
                cart_collection.update_one({"_id": cart["_id"]}, {"$set": {"products": cart["products"]}})
                return redirect(url_for("root.product",category=category,product_id=product_id))
        # If the product does not exist in the cart, add it
        cart_collection.update_one({"_id": cart["_id"]}, {"$push": {"products": product}})
    else:
        cart_collection.insert_one({"user_id": current_user.id, "products": [product]})
    return redirect(url_for("root.product",category=category,product_id=product_id))

@root.route("/cart/<product_id>/remove_from_cart", methods=["POST", "GET"])
@login_required
def remove_from_cart(product_id):
    cart_collection = db["cart"]
    product = collection.find_one({"_id":ObjectId(product_id)})
    cart = cart_collection.find_one({"user_id": current_user.id})
    if cart:
        # Check if the product already exists in the cart
        for p in cart["products"]:
            if p["_id"] == product["_id"]:
                # If it does, remove it
                cart_collection.update_one({"_id": cart["_id"]}, {"$pull": {"products": {"_id": product["_id"]}}})
                return redirect(url_for("root.cart"))
    return redirect(url_for("root.cart"))


@root.route("/cart")
@login_required
def cart():
    cart_collection = db["cart"]
    cart = cart_collection.find_one({"user_id": current_user.id})
    if cart is None:
        cart_collection.insert_one({"user_id": current_user.id, "products": []})
    total_price = 0
    for product in cart["products"]:
        total_price += product["price"] * product["quantity"] *0.8
    return render_template('cart.html',cart=cart, total_price=total_price)

@root.route("/cart/<product_id>/update_quantity", methods=["POST"])
@login_required
def update_quantity(product_id):
    quantity = int(request.form.get("quantity"))
    cart_collection = db["cart"]
    product = collection.find_one({"_id":ObjectId(product_id)})
    cart = cart_collection.find_one({"user_id": current_user.id})
    if cart:
        for p in cart["products"]:
            if p["_id"] == product["_id"]:
                p["quantity"] = quantity
                cart_collection.update_one({"_id": cart["_id"]}, {"$set": {"products": cart["products"]}})
                return redirect(url_for("root.cart"))
    return redirect(url_for("root.cart"))


@root.route("/orders")
@login_required
def orders():
    orders_collection = db["orders"]
    orders = list(orders_collection.find({"user_id": current_user.id}))
    return render_template('orders.html',orders=orders)


# @root.route("/cart/<product_id>/checkout")
# @login_required
# def checkout(product_id):
#     cart_collection = db["cart"]
#     orders_collection = db["orders"]
#     product_collection = db["products"]
#     product = collection.find_one({"_id":ObjectId(product_id)})
#     cart = cart_collection.find_one({"user_id": current_user.id})
#     if cart:
#         # Check if the product already exists in the cart
#         for p in cart["products"]:
#             if p["_id"] == product["_id"]:
#                 # If it does, remove it
#                 cart_collection.update_one({"_id": cart["_id"]}, {"$pull": {"products": {"_id": product["_id"]}}})
#                 orders_collection.insert_one({"user_id": current_user.id, "products": [product]})
#                 product_collection.update_one({"_id": product["_id"]}, {"$set": {"amount_available": product["amount_available"] - product["quantity"]}})
#                 return redirect(url_for("root.cart"))
#     return redirect(url_for("root.cart"))

@root.route("/cart/checkout")
@login_required
def checkout():
    cart_collection = db["cart"]
    orders_collection = db["orders"]
    product_collection = db["products"]
    cart = cart_collection.find_one({"user_id": current_user.id})
    if cart:
        for product in cart["products"]:
            product_collection.update_one({"_id": product["_id"]}, {"$set": {"amount_available": product["amount_available"] - product["quantity"]}})
        orders_collection.insert_one({"user_id": current_user.id, "products": cart["products"]})
        cart_collection.update_one({"user_id": current_user.id}, {"$set": {"products": []}})
        
    return redirect(url_for("root.home"))