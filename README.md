# Zallo Giafferano - Recipe Sharing Platform

Zallo Giafferano is a community-driven recipe sharing platform I built using Flask and MongoDB. This application allows users to create, share, and discover cooking recipes from around the world.

![Zallo Giafferano Screenshot](https://images.unsplash.com/photo-1495195134817-aeb325a55b65?ixlib=rb-1.2.1&auto=format&fit=crop&w=1500&q=80)

## Disclaimer

This project, "Zallo Giafferano," is a portfolio piece created solely for educational purposes and to demonstrate my web development skills. It is not a commercial product and is not affiliated with or endorsed by any existing recipe websites or brands. All content is fictional and created for demonstration purposes only. This application is not intended for commercial use.

## Features I Implemented

* **User Authentication**: Complete register, login, and logout system with secure password hashing
* **CRUD Operations**: Full create, read, update, and delete functionality for recipes
* **Recipe Management**: Browse recipes with pagination and filtering by category
* **Search Functionality**: Search recipes by name or ingredients
* **User Profiles**: Personalized profiles with user statistics and recipe collections
* **Like System**: Interactive like functionality for recipes
* **Admin Panel**: Administrative tools to manage ingredients and recipe categories
* **Responsive Design**: Mobile-first approach that works across all devices

## Technology Stack

As a full-stack developer, I utilized:

* **Backend**: Python with Flask framework for routing and request handling
* **Database**: MongoDB for a flexible, document-based data storage
* **Frontend**: HTML5, CSS3, and JavaScript for a responsive user interface
* **UI Framework**: Materialize CSS for modern, responsive components
* **Authentication**: Werkzeug Security for password hashing and verification
* **Additional Libraries**: jQuery for DOM manipulation, Font Awesome for icons

## Local Development Setup

### Prerequisites

* Python 3.6 or higher
* MongoDB running on localhost:27017
* Git

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/zallo-giafferano.git
   cd zallo-giafferano
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Initialize the database with sample data:
   ```bash
   python init_database.py
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Access the application at `http://localhost:5000`

### Demo Admin Account

* Username: admin  
* Password: admin

## Project Structure

```
zallo-giafferano/
├── app.py                # Main application file with routes and logic
├── init_database.py      # Database initialization script
├── requirements.txt      # Python dependencies
├── static/               # Static files (CSS, JS)
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
└── templates/            # HTML templates using Jinja2
    ├── add_category.html
    ├── add_ingredient.html
    ├── add_recipe.html
    ├── base.html
    ├── edit_recipe.html
    ├── home.html
    ├── login.html
    ├── manage_categories.html
    ├── manage_ingredients.html
    ├── profile.html
    ├── recipe.html
    └── register.html
```

## Features in Detail

### Recipe Management

Users can browse, search, and filter recipes by category. Each recipe displays:
- Recipe name and image
- Creator information
- Category and like count
- Ingredients list
- Preparation instructions

### User Profiles

Each user has a profile page that displays:
- Recipe count
- Total likes received
- Categories used
- All recipes created by the user

### Admin Features

Admin users (username: admin) can:
- Manage recipe categories (add, edit, delete)
- Manage ingredients (add, edit, delete)

## Future Enhancements

- Email confirmation for account registration  
- Password reset functionality  
- Recipe ratings and comments  
- User favorites and meal planning  
- More advanced search and filtering options  
- Image upload functionality

## Testing

The application has been tested on:

- **Desktop Browsers**: Chrome, Firefox, Safari  
- **Mobile Browsers**: Chrome (Android), Safari (iOS)  
- **Devices**: Various smartphones and tablets

## Deployment

For production deployment:

1. Update the MongoDB connection URI in `app.py`  
2. Set debug to False in `app.py`  
3. Deploy to your preferred hosting platform

## Credits

- Materialize CSS for the UI components  
- Unsplash for the sample images  
- Font Awesome for the icons  
- MongoDB for the database  
- Flask for the web framework

## License

MIT License

## Author

Salvatore Bevilacqua