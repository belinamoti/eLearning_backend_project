
E_learning Portfolio Project

Moti Belina

April 01, 2023

SQL with Python, Flask

For this project I used ORM (Object-Relational Mapping) to perform database operations by mapping to the database tables, and the SQLAlchemy ORM is being used to perform CRUD operations on these tables. I also directly executed raw SQL statements using the psycopg2 library to interact with a PostgreSQL database by creating sample values for my tables.

I used Flask-SQLAlchemy to build a database for an online learning platform. The tables include:

Enrollment: A join table that associates users with courses they are enrolled in during a specific semester and year.

User: A model representing users of the platform. It contains attributes for a user's name, email, password, and username, as well as relationships to discussions they have created and enrollments they have made.

Course: A model representing courses available on the platform. It contains attributes for a course's name, description, content, and price, as well as relationships to enrollments made for the course and instructors who teach it.

Instructor: A model representing instructors who teach courses on the platform. It contains attributes for an instructor's name and email, as well as a relationship to the course they teach.

Discussion: A model representing discussions that users create related to specific courses. It contains attributes for a discussion's title, content, creation date, and the user who created it, as well as a relationship to the course it is related to.


USER <> COURSE = many to many ENROLLMENT
COURSE <> INSTRUCTOR = ONE TO MANY/MANY TO ONE
USER <> DISCUSSION = ONE TO MANY/MANY TO ONE
USER <> INSTRUCTOR = ONE TO MANY/MANY TO ONE



# User api

Routes in courses:

GET /users: Returns a JSON list of all users in the system. Each user is represented by a dictionary of their attributes.

POST /users: Creates a new user account in the system. The new user's attributes are specified in the request body as a JSON object. If successful, returns a JSON representation of the new user's attributes.

I used the scramble function to hash and salt passwords before storing them in the database. To use scramble, I imported the required module at the top.

The abort function is used to generate a HTTP 400 (Bad Request) response if the username is less than 5 characters or the password is less than 6 characters.



# Course api

Routes in courses:

The index route handles HTTP GET requests to the URL '/courses' and returns a JSON response containing information about all courses.

The update_price_by_id route handles HTTP PATCH and PUT requests to the URL '/courses/<id>', where <id> is the ID of a specific course. It updates the price of the course with the specified ID and returns a JSON response containing information about the updated course.

The update_all_course_price route handles HTTP PATCH and PUT requests to the URL '/courses/apply_discount'. It applies a 50% discount to the price of all courses and returns a JSON response containing information about all the discounted courses.



# Enrollment api

Routes in enrollments:

GET /enrollments: Returns a list of all enrollments as JSON.

GET /enrollments/not_paid: Returns a list of unpaid enrollments as JSON.

GET /enrollments/amount_due/<int:user_id>: Returns the total amount due for the given user as JSON.





# Instructor api

Routes in instructors:

index route which returns a list of all instructors in the database.

show_instructor_by_id route which returns a single instructor based on the given id parameter.

get_instructor_courses route which returns a list of courses that are taught by the given instructor id

There is a different import statement from sqlalchemy.orm that I included for joinedload which I used to load related instructor data. I then modified the query to join the course table with the Instructor table using joinedload and filter by instructor using the contains method.



# Discussion api

Routes in discussions:

index route which returns a list of all discussions in the database.

show_by_id() : used to retrieve a single object of a certain type by its ID. For example, the courses/show_by_id route retrieves a single course by its ID.

create() :  used to create a new object of a certain type. For example, the discussions/create route creates a new discussion post. These functions use SQLAlchemy to create a new database record based on the data provided in the request payload.

update() : used to update an existing object of a certain type. For example, the courses/update_price_by_id route updates the price of a course by its ID. These functions use SQLAlchemy to retrieve the object to be updated, modify its attributes based on the data provided in the request payload, and then commit the changes to the database.

delete() : used to delete an existing object of a certain type. For example, the discussions/delete route deletes a discussion post by its ID. These functions use SQLAlchemy to retrieve the object to be deleted and then delete it from the database.
