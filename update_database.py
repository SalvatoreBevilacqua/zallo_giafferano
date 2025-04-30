import os
from flask import Flask
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env

# Simplified Flask app configuration
app = Flask(__name__)
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
mongo = PyMongo(app)

# Function to update the recipes collection
def update_recipes():
    print("Updating 'recipe' collection...")
    # Add 'likes' field to all recipes that don't have it
    result = mongo.db.recipe.update_many(
        {"likes": {"$exists": False}},
        {"$set": {"likes": 0}}
    )
    print(f"Updated {result.modified_count} recipes with 'likes' field")

# Function to update the users collection
def update_users():
    print("Updating 'users' collection...")
    # Add 'email', 'bio', and 'favorites' fields to all users that don't have them
    result = mongo.db.users.update_many(
        {"$or": [
            {"email": {"$exists": False}},
            {"bio": {"$exists": False}},
            {"favorites": {"$exists": False}}
        ]},
        {"$set": {
            "email": "",
            "bio": "",
            "favorites": []
        }}
    )
    print(f"Updated {result.modified_count} users with 'email', 'bio', and 'favorites' fields")

# Function to update the ingredients collection
def update_ingredients():
    print("Updating 'ingredients' collection...")
    # Add 'category' field to all ingredients that don't have it
    result = mongo.db.ingredients.update_many(
        {"category": {"$exists": False}},
        {"$set": {"category": "Other"}}
    )
    print(f"Updated {result.modified_count} ingredients with 'category' field")

# Function to update the dish (categories) collection
def update_categories():
    print("Updating 'dish' collection...")
    # Add 'description' field to all categories that don't have it
    result = mongo.db.dish.update_many(
        {"description": {"$exists": False}},
        {"$set": {"description": ""}}
    )
    print(f"Updated {result.modified_count} categories with 'description' field")

if __name__ == "__main__":
    print("Starting database migration...")
    update_recipes()
    update_users()
    update_ingredients()
    update_categories()
    print("Migration completed successfully!")