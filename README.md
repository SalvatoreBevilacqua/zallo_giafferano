# Data Centric Development Milestone Project
# Zallo Giafferano

This Website has been developed for Code Institute's Data Centric Development Milestone Project and represents a recipe site. Is a multi-page site with which the User can interact to add, modify and delete cooking recipes.

## UX

This Project is to demonstrate lessons learned in this section Python Fundamentals and Data Centric Development.
The idea of the project is inspired by the various sites born on the web.
The realization was born to apply the notions learned in the Python fundamentals and Data Centric modules.

## Scenario

As mentioned above, I have created a basic website using, as much as I could, all the notions that I have received during this period. My aim is to continue building my website and develop, in particular, my projects page as that will be my business card for whoever would like to contact me and know more about my services and what I can, eventually, do for them.

## Features

The basic structure of the page is to allow the User a simple navigation.

* **Navbar**: Composed by on the webpage logo on the left corner and at the opposite end the communication buttons for the navigation links to various pages.

* **Mobile Sidenav**: Which shows the webpage logo at the top and under the communication buttons for the navigation links to various pages.

* **Section**: The body of the pages have been applied, where possible, the reuse of the codes according to the spirit of programming. Making navigation between sections homogeneous.

* **Register/Login/Logout**: User interaction begins with registration or via the login page providing Username and password. Once the actions have been completed on the web page, the User is able to use the logout button to disconnect from the session.

* **CRUD**: Within the web page the User is able Create, Read, Update, Delete the Cooking Recipes.

### Existing Features

The first function that the User can do is interact with the web page through the Home, where he has access to all the recipes loaded into the database. It is also possible to carry out a search using the search function.
The User can register, log in and log out of the web page through the links button provided.
The User is able to complete all requests for CRUD (Create, Read, Update and Delete) the recipes. Furthermore, a limitation to this function has been added, only to the creators of the same recipes and to the admin page can have access to Edit and Delete functions.

### Features Left to Implement

In particular, for this project I would like to increase:
 - The functionality and the possibility for the User to manage the database of Ingredients through Python funciont, as was done for the add the recipes. 
 - To a calendar with meals of the day organized according to the dishes chosen by the User.
 - Update the security of the web page both by requesting a confermation email on registration and providing to the User a double confirmation while requesting to delete one or more recipes.

## Technologies Used

For this project I used:

- [HTML5]( https://en.wikipedia.org/wiki/HTML5)
    - The project uses **HTML5** to structure the content in line with modern semantic html5.

- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets#CSS_3)
    - The project uses **CSS3** to style the html content.

- [PYTHON](https://it.wikipedia.org/wiki/Python)
    - The project uses **PYTHON** to create functions.

- [Jquery](https://it.wikipedia.org/wiki/JQuery)
    - I used **Jquery** to manage, manipulate animations and simplify the use of AJAX functionality.

- [Materialize](https://materializecss.com/)
    - I used **Materialize** as a front-end framework for for styling the progect, icons, navbar.

- [Randomkeygen](https://randomkeygen.com/)
    - I used **Randomkeygen** to generate passes for SECRET_KEY in Herokuto generate passes for SECRET_KEY in Heroku.

- [MongoDB](https://it.wikipedia.org/wiki/MongoDB)
    - I used **MongoDB** as a database for the project.

- [Heroku](https://it.wikipedia.org/wiki/Heroku)
    - I used **Heroku** as a Cloud to develop, distribute and manage apps directly online.

- [Werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/)
    - I used **Werkzeug** this library for generate_password_hash / check_password_hash. 

- [Google Images](https://www.google.com/imghp?hl=en)
    - I used **Google Images** to find the Images for my user`s review.

## Testing

To test this project I used various browsers and devices:

#### Mobile Browsers
* Chrome
* Safari

#### Desktop Browsers
* Chrome

#### Devices
* ThinkPad X1 Carbon
* Samsung S8
* Huawei p20 pro
* Iphone X

During testing i used Chrome Developer tools to test the responsive design on different size and the features of the page on different width.

The site was developed following the Bootstrap Grid System and the same was tested to ensure that all the elements are responsive on the following resolutions on each page:

- Width ≥1200px
- Width ≤ 600px

### Validation Testings

For HTML validation testing I used ["W3 Validator"](https://validator.w3.org/nu/?doc=https%3A%2F%2Fgello94.github.io%2Ffirst-milestone-antonio%2F) which shows the html documents to be valid.

For CSS validation testing I used ["W3 CSS Validator"](http://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fgello94.github.io%2Ffirst-milestone-antonio%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=it) which shows the stylesheet to be valid CSS3.

## Deployment

This page has been deployed to ["Heroku Pages"](https://dashboard.heroku.com/apps/milestone-project-salvatore-b).

Heroku is used to host the code and publish the pages.

After a final Git Add and Git commit

`$git add .`

`$git commit -m "Final commit"`

The pages were pushed to the GitHub repository

`$ git push -u origin master`

## Credits

For this project I had ispiration by the Example Idea 1 Project of Code Institute's Data Centric Development Milestone Project.

