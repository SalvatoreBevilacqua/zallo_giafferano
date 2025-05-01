import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
# Set up MongoDB connection

# Simple configuration for demonstration purposes
app.config["MONGO_DBNAME"] = "zallo_giafferano"
app.config["MONGO_URI"] = "mongodb://localhost:27017/zallo_giafferano"
app.secret_key = "demo_secret_key"  # Adequate for demonstration

mongo = PyMongo(app)


# Custom decorator to ensure user is logged in
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Check if user is logged in
        if "user" not in session:
            flash("Please log in to access this page")
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated_function


@app.route("/")
def home():
    """
    Render the homepage with featured recipes
    """
    # Get 3 latest recipes for the featured section
    featured_recipes = list(mongo.db.recipe.find().sort("_id", -1).limit(3))
    # Get top categories
    categories = list(mongo.db.dish.find().limit(4))
    
    return render_template(
        "home.html", 
        featured_recipes=featured_recipes,
        categories=categories
    )


@app.route("/edit_profile/<username>", methods=["GET", "POST"])
@login_required
def edit_profile(username):
    """
    Edit user profile information
    """
    # Check if user matches profile being edited
    if username != session["user"] and session["user"] != "admin":
        flash("You can only edit your own profile")
        return redirect(url_for("profile", username=session["user"]))
    
    if request.method == "POST":
        # Update user document
        submit = {
            "bio": request.form.get("bio"),
            "email": request.form.get("email")
        }
        
        # Update user in database
        mongo.db.users.update_one({"username": username}, {"$set": submit})
        flash("Profile Successfully Updated")
        
        return redirect(url_for("profile", username=username))

    return redirect(url_for("profile", username=username))


@app.route("/recipe", methods=["GET", "POST"])
def recipe():
    """
    Display all recipes with pagination
    """
    # Get page number from request args, default to 1
    page = request.args.get('page', 1, type=int)
    per_page = 6  # Number of recipes per page
    skip = (page - 1) * per_page
    
    # Get total number of recipes
    total = mongo.db.recipe.count_documents({})
    
    # Calculate total pages
    total_pages = (total // per_page) + (1 if total % per_page > 0 else 0)
    
    # Get recipes for current page
    recipes = list(mongo.db.recipe.find().sort("_id", -1).skip(skip).limit(per_page))
    
    # Get all dish categories for filtering
    dishes = list(mongo.db.dish.find().sort("dish_name", 1))
    
    return render_template(
        "recipe.html", 
        recipe=recipes, 
        dishes=dishes,
        current_page=page, 
        total_pages=total_pages
    )


@app.route("/search", methods=["GET", "POST"])
def search():
    """
    Search recipes by keyword
    """
    query = request.form.get("query")
    
    if not query:
        return redirect(url_for("recipe"))
    
    # Use text search with MongoDB
    recipe = list(mongo.db.recipe.find(
        {"$text": {"$search": query}}).sort("_id", -1))
    
    return render_template(
        "recipe.html", 
        recipe=recipe, 
        search_query=query
    )


@app.route("/filter/<category>")
def filter_recipes(category):
    """
    Filter recipes by category
    """
    recipes = list(mongo.db.recipe.find({"dish_name": category}).sort("_id", -1))
    
    return render_template(
        "recipe.html", 
        recipe=recipes, 
        category=category
    )


@app.route("/add_recipe", methods=["GET", "POST"])
@login_required
def add_recipe():
    """
    Add a new recipe to the database
    """
    if request.method == "POST":
        # Create recipe document
        recipe = {
            "dish_name": request.form.get("dish_name"),
            "ingredients": request.form.getlist("ingredients"),
            "image": request.form.get("image"),
            "plate_name": request.form.get("plate_name"),
            "preparation": request.form.get("preparation"),
            "created_by": session["user"],
            "likes": 0
        }
        
        # Insert recipe into database
        mongo.db.recipe.insert_one(recipe)
        flash("Recipe Successfully Added")
        return redirect(url_for("recipe"))

    # Get dishes and ingredients for form dropdowns
    dish = mongo.db.dish.find().sort("dish_name", 1)
    ingredients = mongo.db.ingredients.find().sort("ingredient_name", 1)
    
    return render_template(
        "add_recipe.html", 
        ingredients=ingredients, 
        dish=dish
    )


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
@login_required
def edit_recipe(recipe_id):
    """
    Edit an existing recipe
    """
    recipe = mongo.db.recipe.find_one({"_id": ObjectId(recipe_id)})
    
    # Check if user is the creator of the recipe or admin
    if recipe["created_by"] != session["user"] and session["user"] != "admin":
        flash("You can only edit your own recipes")
        return redirect(url_for("recipe"))
    
    if request.method == "POST":
        # Update recipe document
        submit = {
            "dish_name": request.form.get("dish_name"),
            "ingredients": request.form.getlist("ingredients"),
            "image": request.form.get("image"),
            "plate_name": request.form.get("plate_name"),
            "preparation": request.form.get("preparation"),
            "created_by": recipe["created_by"],  # Keep original creator
            "likes": recipe.get("likes", 0)  # Keep existing likes
        }
        
        # Update recipe in database
        mongo.db.recipe.update_one({"_id": ObjectId(recipe_id)}, {"$set": submit})
        flash("Recipe Successfully Updated")
        return redirect(url_for("recipe"))

    # Get dishes and ingredients for form dropdowns
    dish = mongo.db.dish.find().sort("dish_name", 1)
    ingredients = mongo.db.ingredients.find().sort("ingredient_name", 1)
    
    return render_template(
        "edit_recipe.html", 
        recipe=recipe, 
        ingredients=ingredients, 
        dish=dish
    )


@app.route("/delete_recipe/<recipe_id>")
@login_required
def delete_recipe(recipe_id):
    """
    Delete a recipe from the database
    """
    recipe = mongo.db.recipe.find_one({"_id": ObjectId(recipe_id)})
    
    # Check if user is the creator of the recipe or admin
    if recipe["created_by"] != session["user"] and session["user"] != "admin":
        flash("You can only delete your own recipes")
        return redirect(url_for("recipe"))
    
    # Delete recipe from database
    mongo.db.recipe.delete_one({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")
    
    return redirect(url_for("profile", username=session["user"]))


@app.route("/like_recipe/<recipe_id>")
@login_required
def like_recipe(recipe_id):
    """
    Like a recipe
    """
    # Increment the likes count
    mongo.db.recipe.update_one(
        {"_id": ObjectId(recipe_id)},
        {"$inc": {"likes": 1}}
    )
    
    # Redirect to referring page or recipes page
    return redirect(request.referrer or url_for("recipe"))


@app.route("/profile/<username>")
@login_required
def profile(username):
    """
    Display user profile with their recipes
    """
    # Check if the accessed profile belongs to current user
    if username != session["user"] and session["user"] != "admin":
        flash("You can only view your own profile")
        return redirect(url_for("profile", username=session["user"]))
    
    # Get user information
    user = mongo.db.users.find_one({"username": username})
    
    # Get user's recipes
    recipes = list(mongo.db.recipe.find({"created_by": username}).sort("_id", -1))
    
    return render_template(
        "profile.html", 
        username=username, 
        profile=recipes, 
        user=user
    )


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Register a new user
    """
    if request.method == "POST":
        # Check if username already exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        # Create user document
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "email": request.form.get("email"),
            "bio": "",
            "favorites": []
        }
        
        # Insert user into database
        mongo.db.users.insert_one(register)

        # Put user into session
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Log in an existing user
    """
    if request.method == "POST":
        # Check if username exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # Check password
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    # Put user into session
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(request.form.get("username")))
                    
                    return redirect(url_for("profile", username=session["user"]))
            else:
                # Invalid password
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
        else:
            # Username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    """
    Log out user
    """
    # Remove user from session
    flash("You have been logged out")
    session.pop("user")
    
    return redirect(url_for("login"))


# Ingredients Management Routes
@app.route("/manage_ingredients")
@login_required
def manage_ingredients():
    """
    Manage ingredients (admin only)
    """
    # Check if user is admin
    if session["user"] != "admin":
        flash("Only admin can manage ingredients")
        return redirect(url_for("recipe"))
    
    # Get all ingredients
    ingredients = list(mongo.db.ingredients.find().sort("ingredient_name", 1))
    
    return render_template("manage_ingredients.html", ingredients=ingredients)


@app.route("/add_ingredient", methods=["GET", "POST"])
@login_required
def add_ingredient():
    """
    Add a new ingredient (admin only)
    """
    # Check if user is admin
    if session["user"] != "admin":
        flash("Only admin can add ingredients")
        return redirect(url_for("recipe"))
    
    if request.method == "POST":
        # Create ingredient document
        ingredient = {
            "ingredient_name": request.form.get("ingredient_name"),
            "category": request.form.get("category")
        }
        
        # Insert ingredient into database
        mongo.db.ingredients.insert_one(ingredient)
        flash("Ingredient Successfully Added")
        
        return redirect(url_for("manage_ingredients"))
    
    # Get categories for form dropdown
    categories = ["Vegetables", "Fruits", "Meat", "Fish", "Dairy", "Grains", "Spices", "Other"]
    
    return render_template("add_ingredient.html", categories=categories)


@app.route("/edit_ingredient/<ingredient_id>", methods=["GET", "POST"])
@login_required
def edit_ingredient(ingredient_id):
    """
    Edit an existing ingredient (admin only)
    """
    # Check if user is admin
    if session["user"] != "admin":
        flash("Only admin can edit ingredients")
        return redirect(url_for("recipe"))
    
    if request.method == "POST":
        # Update ingredient document
        submit = {
            "ingredient_name": request.form.get("ingredient_name"),
            "category": request.form.get("category")
        }
        
        # Update ingredient in database
        mongo.db.ingredients.update_one({"_id": ObjectId(ingredient_id)}, {"$set": submit})
        flash("Ingredient Successfully Updated")
        
        return redirect(url_for("manage_ingredients"))

    # Get ingredient
    ingredient = mongo.db.ingredients.find_one({"_id": ObjectId(ingredient_id)})
    
    # Get categories for form dropdown
    categories = ["Vegetables", "Fruits", "Meat", "Fish", "Dairy", "Grains", "Spices", "Other"]
    
    return render_template(
        "edit_ingredient.html", 
        ingredient=ingredient, 
        categories=categories
    )


@app.route("/delete_ingredient/<ingredient_id>")
@login_required
def delete_ingredient(ingredient_id):
    """
    Delete an ingredient (admin only)
    """
    # Check if user is admin
    if session["user"] != "admin":
        flash("Only admin can delete ingredients")
        return redirect(url_for("recipe"))
    
    # Delete ingredient from database
    mongo.db.ingredients.delete_one({"_id": ObjectId(ingredient_id)})
    flash("Ingredient Successfully Deleted")
    
    return redirect(url_for("manage_ingredients"))


# Category Management Routes
@app.route("/manage_categories")
@login_required
def manage_categories():
    """
    Manage categories (admin only)
    """
    # Check if user is admin
    if session["user"] != "admin":
        flash("Only admin can manage categories")
        return redirect(url_for("recipe"))
    
    # Get all categories
    categories = list(mongo.db.dish.find().sort("dish_name", 1))
    
    return render_template("manage_categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
@login_required
def add_category():
    """
    Add a new category (admin only)
    """
    # Check if user is admin
    if session["user"] != "admin":
        flash("Only admin can add categories")
        return redirect(url_for("recipe"))
    
    if request.method == "POST":
        # Create category document
        category = {
            "dish_name": request.form.get("dish_name"),
            "description": request.form.get("description")
        }
        
        # Insert category into database
        mongo.db.dish.insert_one(category)
        flash("Category Successfully Added")
        
        return redirect(url_for("manage_categories"))
    
    return render_template("add_category.html")


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
@login_required
def edit_category(category_id):
    """
    Edit an existing category (admin only)
    """
    # Check if user is admin
    if session["user"] != "admin":
        flash("Only admin can edit categories")
        return redirect(url_for("recipe"))
    
    if request.method == "POST":
        # Update category document
        submit = {
            "dish_name": request.form.get("dish_name"),
            "description": request.form.get("description")
        }
        
        # Update category in database
        mongo.db.dish.update_one({"_id": ObjectId(category_id)}, {"$set": submit})
        flash("Category Successfully Updated")
        
        return redirect(url_for("manage_categories"))

    # Get category
    category = mongo.db.dish.find_one({"_id": ObjectId(category_id)})
    
    return render_template("edit_category.html", category=category)


@app.route("/delete_category/<category_id>")
@login_required
def delete_category(category_id):
    """
    Delete a category (admin only)
    """
    # Check if user is admin
    if session["user"] != "admin":
        flash("Only admin can delete categories")
        return redirect(url_for("recipe"))
    
    # Delete category from database
    mongo.db.dish.delete_one({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted")
    
    return redirect(url_for("manage_categories"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP", "0.0.0.0"),
            port=int(os.environ.get("PORT", "5000")),
            debug=True)  # Imposta a True per lo sviluppo, False per la produzione