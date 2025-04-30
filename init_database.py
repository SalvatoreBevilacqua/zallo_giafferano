import os
from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_DBNAME"] = "zallo_giafferano"
app.config["MONGO_URI"] = "mongodb://localhost:27017/zallo_giafferano"
mongo = PyMongo(app)

def init_database():
    print("Initializing database for demonstration...")
    
    # Create collections if they don't exist
    collections = ["recipe", "users", "ingredients", "dish"]
    for collection in collections:
        if collection not in mongo.db.list_collection_names():
            mongo.db.create_collection(collection)
            print(f"Created '{collection}' collection")
    
    # Add sample dish categories
    if mongo.db.dish.count_documents({}) == 0:
        dish_categories = [
            {"dish_name": "Appetizers", "description": "Starters and small bites"},
            {"dish_name": "Main Course", "description": "Primary dishes"},
            {"dish_name": "Desserts", "description": "Sweet treats"},
            {"dish_name": "Soups", "description": "Warm and comforting soups"},
            {"dish_name": "Salads", "description": "Fresh and healthy salads"}
        ]
        mongo.db.dish.insert_many(dish_categories)
        print(f"Added {len(dish_categories)} dish categories")
    
    # Add sample ingredients
    if mongo.db.ingredients.count_documents({}) == 0:
        ingredients = [
            {"ingredient_name": "Salt", "category": "Spices"},
            {"ingredient_name": "Pepper", "category": "Spices"},
            {"ingredient_name": "Olive Oil", "category": "Oils"},
            {"ingredient_name": "Garlic", "category": "Vegetables"},
            {"ingredient_name": "Onion", "category": "Vegetables"},
            {"ingredient_name": "Tomato", "category": "Vegetables"},
            {"ingredient_name": "Basil", "category": "Herbs"},
            {"ingredient_name": "Flour", "category": "Grains"},
            {"ingredient_name": "Sugar", "category": "Sweeteners"},
            {"ingredient_name": "Chicken", "category": "Meat"}
        ]
        mongo.db.ingredients.insert_many(ingredients)
        print(f"Added {len(ingredients)} ingredients")
    
    # Create a demo admin user
    if mongo.db.users.count_documents({"username": "admin"}) == 0:
        from werkzeug.security import generate_password_hash
        admin_user = {
            "username": "admin",
            "password": generate_password_hash("admin"),
            "email": "admin@example.com",
            "bio": "Demo administrator account",
            "favorites": []
        }
        mongo.db.users.insert_one(admin_user)
        print("Created demo admin user (username: admin, password: admin)")
    
    print("Database initialization complete!")
    print("You can now run the application with: python app.py")

if __name__ == "__main__":
    init_database()