# Zallo Giafferano - Recipe Sharing Platform

Zallo Giafferano is a community-driven recipe sharing platform built with Flask and MongoDB. It allows users to create, share, and discover cooking recipes from around the world.

![Zallo Giafferano Screenshot](https://images.unsplash.com/photo-1495195134817-aeb325a55b65?ixlib=rb-1.2.1&auto=format&fit=crop&w=1500&q=80)

## Features

* **User Authentication**: Register, login, and logout functionality  
* **CRUD Operations**: Create, read, update, and delete recipes  
* **Recipe Management**: Browse recipes with pagination and filtering  
* **Search Functionality**: Search recipes by name or ingredients  
* **User Profiles**: Personalized profiles with user statistics  
* **Like System**: Users can like recipes  
* **Admin Panel**: Manage ingredients and recipe categories  
* **Responsive Design**: Works on mobile and desktop devices

## Technology Stack

* **Backend**: Python, Flask  
* **Database**: MongoDB  
* **Frontend**: HTML, CSS, JavaScript  
* **UI Framework**: Materialize CSS  
* **Authentication**: Werkzeug Security  
* **Additional Libraries**: jQuery, Font Awesome

## Local Development Setup

### Prerequisites

* Python 3.6 or higher  
* MongoDB running on localhost:27017  
* Git

### Installation

1. Clone the repository:
   ```bash
   git clone <your-repository-url>
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
├── app.py                # Main application file
├── init_database.py      # Database initialization script
├── requirements.txt      # Python dependencies
├── static/               # Static files (CSS, JS)
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
└── templates/            # HTML templates
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