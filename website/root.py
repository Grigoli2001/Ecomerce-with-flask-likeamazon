import os
from flask import Blueprint, render_template,url_for, jsonify,g, request, redirect, flash, current_app
import sqlite3
from flask_login import login_required,current_user,logout_user
from .APIs.mongoDB import client
from datetime import datetime
from werkzeug.utils import secure_filename
from .APIs.forms import TweetForm, PostForm
from bson import ObjectId

# from .login import User
root = Blueprint('root',__name__)


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
    return render_template('home.html')
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
    print(products)
    print(category)
    return render_template('products.html',products=products, category=category)

@root.route("/products/<category>/<product_id>")
@login_required
def product(category,product_id):
    product = collection.find_one({"_id":ObjectId(product_id)})
    return render_template('product.html',product=product, category=category)

@root.route("/products/<category>/<product_id>/add_to_cart")
@login_required
def add_to_cart(category,product_id):
    product = collection.find_one({"_id":ObjectId(product_id)})
    current_user.cart.append(product)
    current_user.save()
    return redirect(url_for("root.product",category=category,product_id=product_id))
