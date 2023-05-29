# Restaurent-booking-system

![restaurent_management](https://github.com/saifhosari/Restaurent-booking-system/assets/88719461/7d9238dc-cbf2-4815-bb4c-ab5388129bf2)

(Special Thanks to Kepwing for GIF)

Welcome to our Restaurant Booking System! Easily register, login, and reserve tables for a hassle-free dining experience. Discover a diverse range of restaurants, explore their cuisines, and make informed decisions with detailed descriptions and reviews. Our user-friendly platform ensures personalized and tailored experiences, while eliminating the need for manual reservations. Whether you're planning ahead or seeking last-minute availability, our advanced system guarantees a seamless process. Join our community of food lovers and savor every moment at your favorite restaurants. Start exploring and booking today!
## User End
* User will be able to surf the website as guest as well.
* User can login/register to the restauron to book a table.
* User will be emailed if table has been reserverd successfully.
* User will be getting alert for if table has already been booked by other users.
## Booking 
* User will need to login if not then register onto the rastauron to make the booking.
## UI Stories
* As a user, I can see the relavant information about the restauron restaurent.
* As a user, I am able to check their opening and closing.
* As a user, I am able to check the menu that it provides.
* As a user, I can see the reservation i made.
* As a user, I can see the client testimonials regarding the restaurent.

#DataBase Design
### User Table
<img width="338" alt="Screenshot 2023-05-25 at 12 54 46 am" src="https://github.com/saifhosari/Restaurent-booking-system/assets/88719461/4cf7dc8a-8796-4142-8434-c78bdc16c46e">

User table is used for storing user information.

### Table 
<img width="336" alt="Screenshot 2023-05-25 at 12 55 29 am" src="https://github.com/saifhosari/Restaurent-booking-system/assets/88719461/0036ebb3-ed16-4c9b-8d70-ba76f8eb2feb">


This Table in this project is used for storing table information against the user.
* User can book multiple tables that is the reason profile column is foreign key for user.
## Booking 
<img width="356" alt="Screenshot 2023-05-25 at 12 55 01 am" src="https://github.com/saifhosari/Restaurent-booking-system/assets/88719461/52ba78db-c8f1-4c3e-91ec-bd4d22cd865e">

* This is the table for booking to store reservation for the user.
* Single user can do multiple bookings. 
* User can not do reservation if it is already occupied.
* Table has many-to-many relationship with table. so that user can do multiple bookings.

Adding many-to-many relationship does not causes redundacy and also the normalization is achieved.

<img width="294" alt="Screenshot 2023-05-25 at 12 55 10 am" src="https://github.com/saifhosari/Restaurent-booking-system/assets/88719461/5033a1db-d5fa-46cd-985f-d0d847004818">

This is table between table and booking with their respective ids. The only reason for separate is to not have redundancy in the data.

However, there are few other tables for relationships.
## DataBase General Diagram 

<img width="1085" alt="Screenshot 2023-05-25 at 1 50 20 am" src="https://github.com/saifhosari/Restaurent-booking-system/assets/88719461/94fbdae1-7322-4440-8052-9d1e3781fc42">

### Summary for all the tables 

#### Table Model:
* Represents a table in the restaurant.
* It has fields for the table number and its capacity.
#### User Model:
* Extends Django's built-in AbstractUser model.
* Allows you to customize the user model if needed.
* You can add any additional fields or customizations required for your user model.
#### Guest Model:

* Represents a guest who wants to make a booking.
* It has fields for the guest's name, email, and phone number.
#### Booking Model:

* Represents a booking made by a guest for a specific table.
* It has fields for the table (ForeignKey to the Table model), the guest (ForeignKey to the Guest model), the booking date, start time, and end time.
* The booking date field is set to the current date by default.
* The start time and end time represent the time slot for the booking.
* These models allow you to manage tables, users, guests, and bookings in your restaurant booking system. You can customize and add additional functionality to suit your specific requirements.


# Agile Workflow 
Agile Workflow
An approximation of the agile workflow was used in the development of this project. The key ideas adopted were:

* focus on the essential features first
* work in small iterations
* add extra features as time permitted
* using GitHub's kanban board, issues, labels, and project features to organize these iterations.

* the simplest authentication system built-in django is used - username and password
* creating the simplest database models and relationships that would give a minimally functioning product. This included:
  Adding a basic table info: ( table_name, profile(foreign key), date_created )
  Adding a basic booking info: (registered_with(foreign key), from_time, to_time, tables (Many to Many with table)
  Filtering for booking status will be implemented later.

* Once these features were implemented, a minimum front-end was built. Attention was first paid to basic styling and layout with Bootstrap
  Adding a navbar and footer
  Adding responsive layout to the login, logout, animation for restaurent.
  Displaying the essential information of a book in a Bootstrap card.
  Placing those cards in responsive rows and columns.
  Adding menu for restaurent.
  Making the whole layout with SCSS, Boostrap, and JQuery for animation.

Work was done on same branch as it is done by single person.

<img width="1207" alt="Screenshot 2023-05-25 at 2 07 52 am" src="https://github.com/saifhosari/Restaurent-booking-system/assets/88719461/02386a89-a007-42b3-9889-c357ec56da5b">

With the help detailed discription of commits will help and other contributors to know what commit does and why code has been changed.
* It helped break the task down into smaller chunks which helped me organize my workday productively - I was able to dedicate time and effort to completing each task rather than planning over and over again.
* It is very satisfying to move tasks from the Todo, to In Progress, to Done. It gave me a sense of accomplishment - even if the issue is not entirely solved, progress was made in its resolution.

# FEATURES 

## Admin Panel

* Admin panel is used by a superuser that can customize the bookings, tables, guests however needed.
* Admin has all the access rights.

### LOG-IN SCREEN

<img width="801" alt="Screenshot 2023-05-25 at 2 12 48 am" src="https://github.com/saifhosari/Restaurent-booking-system/assets/88719461/90794afc-a40f-4188-bd05-86452313248d">

#### ADD USER 

<img width="1180" alt="Screenshot 2023-05-25 at 2 13 56 am" src="https://github.com/saifhosari/Restaurent-booking-system/assets/88719461/c945e969-9803-4e82-9a59-7f3c6d99fa55">

Admin can add the user manually.
#### BOOKINGS 

<img width="1180" alt="Screenshot 2023-05-25 at 2 13 56 am" src="https://github.com/saifhosari/Restaurent-booking-system/assets/88719461/c5a1e422-71fd-47f1-b6b6-7d2c1c994181">

Admin can fully customize bookings and manage them accordingly.

* if there are multiple admin that have access over the restauren admin panel.For this user has logout option to login with other accounts 

<img width="1440" alt="Screenshot 2023-05-25 at 7 13 59 pm" src="https://github.com/saifhosari/Restaurent-booking-system/assets/88719461/3d6edf60-ee6f-4c5e-b891-7a8fd952e63c">

#### ADD GUESTS 

<img width="1440" alt="image" src="https://github.com/saifhosari/Restaurent-booking-system/assets/88719461/c13b1615-2a20-4835-966a-1754af62f8ff">


User has the ability to add guests.

###### NOTE: SuperAdmin/Admin will have all the permissions.

# Website Front-End

#### HOME PAGE 

<img width="1439" alt="Screenshot 2023-05-25 at 7 50 26 pm" src="https://github.com/saifhosari/Restaurent-booking-system/assets/88719461/19f52dcd-5543-4dc7-8530-f19d927ee170">

#### Contact Page ( This page is static just for restaurent contacts ) 

<img width="1440" alt="Screenshot 2023-05-25 at 8 17 07 pm" src="https://github.com/saifhosari/Restaurent-booking-system/assets/88719461/ec4bff2c-34a0-42f2-9e0c-6330fb1f2d4a">

This is information page for restaurent. 

#### Booking Page 

![image](https://github.com/saifhosari/Restaurent-booking-system/assets/88719461/c16c8511-54cf-4311-b42c-9c5e473ee926)

This is booking page where user will do it's booking/reservation.
### Bookings List 

<img width="1440" alt="image" src="https://github.com/saifhosari/Restaurent-booking-system/assets/88719461/c0cec412-571a-483a-92d7-b7bd74a79199">

User can easily see their recent bookings that he has made and interact with. User can delete the reservation by clicking delete button against the record.

#### Footer 

![restaurent_management](https://github.com/saifhosari/Restaurent-booking-system/assets/88719461/475b1231-8f38-4f12-99ac-63f7b0870b10)


This is footer page for restaurent management system.

#### ALERTS 
Whenenever user tries to do the booking. it shows the alert wether the booking has been reserved or not.

<img width="1331" alt="image" src="https://github.com/saifhosari/Restaurent-booking-system/assets/88719461/6c1a15f4-2441-497d-ac31-6af203b9c702">

# Testing 

### Code Validation
The files models.py, settings.py,  views.py, and urls.py were validated using the python linter that was included with Gitpod's default settings from Code Institute's template. These problems were reported in the PROBLEMS tab in GitPod's output panel. No errors were found in these files except the following:

`Too many blank lines Flake8(E303)`

which simply meant that these lines of code were too long. This does not mean the code is invalid - it is more a style. Therefore, these warnings were ignored. The following is an example of the output:

<img width="504" alt="Screenshot 2023-05-25 at 8 32 45 pm" src="https://github.com/saifhosari/Restaurent-booking-system/assets/88719461/a47b7271-64f1-45b4-b8a8-ccf30f2b028a">


# Unfixed Bugs

An uncaught TypeError is thrown when the pages load. This does not seem to cause any performance issues. The reason that it is unfixed is that it is triggered by the jQuery method having to do with not loading at once.

The Project uses some of JQuery althought for CDN for jquery works really fine and there is not performance issue.

<img width="1425" alt="Screenshot 2023-05-25 at 8 37 49 pm" src="https://github.com/saifhosari/Restaurent-booking-system/assets/88719461/d4ab6603-7958-4188-80b0-dc982f0b7fde">

# Features to Improve and to Add
The following features could be added to BookShelf in future development cycles:

* About Page - Right now, About page has not been implemented that it needs to be in future.
* Notification - As notifications feature needs to be improved with the sms as well.
* Adding sign in with Google, GitHub, and other providers would be a convenient for user.
* Adding email password recovery. This is a feature people expect in modern web applications if they forget their password.


# Deployment

## Technology used
* gunicorn - Server to run django on heroku
* dj3-cloudinary-storage - Allows use of Cloudinary storage to serve static files and media. This is important since django is not really designed to serve static files itself.
* Cloudinary - Media cloud storage service to serve static files
* Bootstrap 5 - A CSS/JavaScript library to make responsive websites.
* JQuery - to make website dynamic.
* Ajax - to make live POST request.
* jazzmin - Package to build admin panel.

# Project Creation 
* Develop Project Environment 
``` pip3 install virtualenv ```
* Create and activate environment and run the reqquirement.txt file
``` $ pip3 install -r requirements.txt  ```

* create restaurent_app and authenticantion app; add it to settings.py
``` 
INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'restaurent_app',
    'authentication',
    
] 
``` 
* Makemigrations and Migrate the models.
``` python manage.py makemigrations 
    python manage.py migrate
```

# Deployment to Heroku

* Create heroku app

  Gave it a name of restuarent_management_system
  Added config vars
  DATABASE_URL
  SECRET_KEY
  PORT
  
* Add Procfile to project root directory

web: gunicorn bookshelf.wsgi
before final deployment, the debug setting in settings.py was set to false for security

# SECURITY WARNING: 
#### don't run with debug turned on in production!

* The idea and code for using the Bootstrap modals and django messages was from this YouTube video by DjangoMastery.
* The HTML code for the Modals was taken from the Bootstrap website and modified accordingly.
* The Table of Contents was created with markdown-toc.
* Big Credits to Chatgpt to help in understanding the concepts of Ajax and How post/get requests works.

#### BIG THANKS TO dribbble.com for code snippets
* These snippets then were modified.


