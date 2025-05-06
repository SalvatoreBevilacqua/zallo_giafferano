# 📚 Zallo Giafferano - Recipe Sharing Platform

> A community-driven Flask application where cooking enthusiasts can share and discover recipes from around the world.

![License](https://img.shields.io/badge/license-MIT-blue)
![Python Version](https://img.shields.io/badge/Python-3.6+-blue)
![Flask Version](https://img.shields.io/badge/Flask-2.2.0+-green)
![MongoDB](https://img.shields.io/badge/MongoDB-4.3.0+-green)
![Deployment](https://img.shields.io/badge/Deployment-Heroku-purple?logo=heroku)

![Screenshot](https://images.unsplash.com/photo-1495195134817-aeb325a55b65?ixlib=rb-1.2.1&auto=format&fit=crop&w=1500&q=80)

---

## 🚀 Features

- **User Authentication**: Secure register, login, and logout system with password hashing
- **Recipe Management**: Create, read, update, and delete functionality for recipes with image support
- **Browsing & Filtering**: Browse recipes with pagination and filter by category
- **Search Functionality**: Search recipes by name or ingredients
- **User Profiles**: Personalized profiles with statistics and recipe collections
- **Like System**: Interactive like functionality for recipes
- **Admin Panel**: Administrative tools to manage ingredients and recipe categories
- **Responsive Design**: Mobile-first approach that works across all devices

---

## 🛠️ Tech Stack

| Layer       | Technologies                                |
|-------------|---------------------------------------------|
| **Backend** | Python, Flask, Werkzeug Security            |
| **Frontend**| HTML5, CSS3, JavaScript, Materialize CSS    |
| **Database**| MongoDB with PyMongo                        |
| **Auth**    | Session-based with password hashing         |
| **Tools**   | jQuery, Materialize CSS, Font Awesome       |

---

## 📦 Installation & Setup

```bash
# Clone the repository
git clone https://github.com/your-username/zallo-giafferano.git
cd zallo-giafferano

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Initialize the database with sample data
python init_database.py

# Run the application
python app.py
```

### 🔐 Environment Variables

Create an `env.py` file in the root directory (this file is gitignored):

```python
import os

# Flask config
os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "your_secret_key")

# Database config
os.environ.setdefault("MONGO_URI", "mongodb://localhost:27017/zallo_giafferano")
```

---

## 🔄 Database Initialization

The `init_database.py` script creates the necessary collections and adds sample data:

- Dish categories (Appetizers, Main Course, Desserts, etc.)
- Common ingredients
- Admin user account

Run the script to initialize your database:

```bash
python init_database.py
```

---

## 👤 User Roles & Credentials

| Role   | Username | Password |
|--------|----------|----------|
| Admin  | admin    | admin    |

---

## 📁 Project Structure

```
zallo-giafferano/
├── app.py                 # Main application file with routes and logic
├── init_database.py       # Database initialization script
├── requirements.txt       # Python dependencies
├── Procfile               # Heroku deployment configuration
├── static/                # Static files (CSS, JS)
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
└── templates/             # HTML templates using Jinja2
    ├── add_category.html
    ├── add_ingredient.html
    ├── add_recipe.html
    ├── base.html
    ├── edit_category.html
    ├── edit_ingredient.html
    ├── edit_recipe.html
    ├── home.html
    ├── login.html
    ├── manage_categories.html
    ├── manage_ingredients.html
    ├── profile.html
    ├── recipe.html
    └── register.html
```

---

## 🧪 Testing

Tested on:

- ✅ Desktop: Chrome, Firefox, Safari
- ✅ Mobile: Chrome (Android), Safari (iOS)
- ✅ Devices: Various smartphones and tablets

---

## 🌍 Deployment

### Local Deployment

1. Follow the Installation & Setup instructions above
2. Access the application at `http://localhost:5000`

### Heroku Deployment

1. Create a Heroku account and install the Heroku CLI
2. Create a new Heroku app
3. Set the following Config Vars in Heroku:
   - IP: 0.0.0.0
   - PORT: 5000
   - SECRET_KEY: your_secret_key
   - MONGO_URI: your_production_mongodb_uri
4. Connect your GitHub repository or deploy using Heroku Git
5. Ensure the Procfile contains: `web: python app.py`
6. Deploy the application

---

## 🔮 Future Enhancements

- Email confirmation for account registration
- Password reset functionality
- Recipe ratings and comments system
- User favorites and meal planning features
- More advanced search and filtering options
- Image upload functionality
- Social sharing integration
- Nutritional information calculator

---

## 🙏 Credits

- [Flask](https://flask.palletsprojects.com/) - Web framework
- [MongoDB](https://www.mongodb.com/) - Database
- [Materialize CSS](https://materializecss.com/) - UI components
- [Font Awesome](https://fontawesome.com/) - Icons
- [Unsplash](https://unsplash.com/) - Sample images

---

## 📜 License

MIT License

---

## 👨‍💻 Author

**Salvatore Bevilacqua**

## Disclaimer

This project, "Zallo Giafferano," is a portfolio piece created solely for educational purposes and to demonstrate web development skills. It is not a commercial product and is not affiliated with or endorsed by any existing recipe websites or brands. All content is fictional and created for demonstration purposes only. This application is not intended for commercial use.
