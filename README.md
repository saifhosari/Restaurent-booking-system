# Restaurent-booking-system
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


