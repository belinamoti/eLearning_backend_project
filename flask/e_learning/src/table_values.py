
import psycopg2

# Connect to your postgres DB
conn = psycopg2.connect(
    """
    dbname=e_learning user=postgres host=localhost port=5432
    """
)

conn.set_session(autocommit=True)
cur = conn.cursor()


# ENROLLMENTS TABLE

cur.execute(
    """
    TRUNCATE TABLE enrollments CASCADE

    """
)

cur.execute(
    """
    INSERT INTO enrollments VALUES
    (3, 4, 'spring', 2022, true),
    (5,  2,'fall', 2023, false),
    (1,  3,'autumn', 2021, true),
    (6,  1, 'spring',2023, true),
    (2,  5, 'fall',2022, false),
    (5,  5, 'spring',2023, false)


     """
)


# # STUDENTS TABLE

# cur.execute(
#     """
#     TRUNCATE TABLE students CASCADE

#     """
# )

# cur.execute(
#     """
#     INSERT INTO students VALUES
#     (1, 'leo', 'davis',  'davis@gmail.com', 'jhskjdfhjsa$','leodavis44', 2),
#     (2,'kei', 'loes',  'loeskei@bmail.com', 'kdsksjds$','keiloes23', 3),
#     (3, 'teil', 'laio',  'kdur@bmail.com', 'poeieud$','teillaio34', 3),
#     (4,'feiuyr', 'derye',  'lewop@gmail.com', 'oudert$', 'feiuyrderye123', 1),
#     (5, 'zeoirp', 'aweer', 'awert@gmail.com', 'swere$','zeoirpaweer32', 2),
#     (6, 'qiosa', 'dawro', 'gert@gmail.com', 'fert$','qiosadawro768', 1)
#     """
# )


# # #  print and test psycopg code

# # print all users first and last name where last name bigins with l
# cur.execute(
#     """
#     SELECT first_name, last_name FROM users WHERE last_name Like 'l%';
#     """
# )
# users = cur.fetchall()
# for user in users:
#     print(user)


# # def a function where you can add values to a table
# def add_new_user(id, first_name, last_name, email, password, username):
#     cur.execute(
#         """
#     INSERT INTO users (id, first_name, last_name, email, password, username)
#     VALUES(%(id)s, %(first_name)s, %(last_name)s, %(email)s, %(password)s, %(username)s)
#     """,
#         {
#             'id': id,
#             'first_name': first_name,
#             'last_name': last_name,
#             'email': email,
#             'password': password,
#             'username': username


#         }

#     )


# # new user with an id of 7 will be added like this
# add_new_user(7, 'leonard', 'linavis', 'linadavis@gmail.com',
#              'dfhjsadsf$', 'leonardlinavis434')


# # DEPARTMENTS TABEL

# cur.execute(
#     """
#     TRUNCATE TABLE departments CASCADE

#     """
# )

# cur.execute(
#     """
#     INSERT INTO departments VALUES
#     (3, 'Mathematics'),
#     (1,  'Physics'),
#     (2,  'IT')


#      """
# )


# # COURSES TABLE

# cur.execute(
#     """
#     TRUNCATE TABLE courses CASCADE

#     """
# )

# cur.execute(
#     """
#     INSERT INTO courses VALUES
#     ('1', 'Python for Beginners', 'Beginner',
#      'Python is a computer programming language often used to build websites and software', 20.44, 3),
#     ('2', 'JavaScript for Beginners', 'Beginner',
#      'JavaScript (JS) is a lightweight, interpreted, or just-in-time compiled programming language with first-class functions.', 18.78, 1),
#     ('3', 'React', 'Advanced',
#      'React is a declarative, efficient, and flexible JavaScript library for building user interfaces.', 45.32, 3),
#     ('4','Flask', 'Intermediate', 'Flask is a micro web framework written in Python', 24.20, 2),
#     ('5', 'SQL', 'Advanced',
#      'SQL stands for Structured Query Language which is basically a language used by databases.', 32.15, 1)

#     """
# )


# # INSTRUCTORS TABLE

# cur.execute(
#     """
#     TRUNCATE TABLE instructors CASCADE

#     """
# )

# cur.execute(
#     """
#     INSERT INTO instructors VALUES
#     (1, 'patric', 'davis', 'dvis@gmail.com', 3, 2, False),
#     (2, 'kevin', 'loe', 'eskei@bmail.com', 5, 1, False),
#     (3, 'deteil', 'lai', 'kur@bmail.com', 1, 3, False),
#     (4, 'feir', 'erye', 'wop@gmail.com', 4, 1, False),
#     (5, 'eoir', 'aweer', 'wer@gmail.com', 2, 2, False),
#     (6, 'iosa', 'awro', 'ert@gmail.com', 5, 3, False)

#     """
# )


# # DISCUSSIONS TABLE

# cur.execute(
#     """
#     TRUNCATE TABLE discussions CASCADE

#     """
# )


# cur.execute(
#     """
#     INSERT INTO discussions VALUES
#     ('1', 'Why do we use recursion?',
#      'SQLALCHEMY_DATABASE_URI configuration value', 6, '2022-08-14', 2),
#     ('2', 'Which data type is used for price?',
#      'Flask API, you set up a way for people to talk to ', 5, '2021-05-24', 3),
#     ('3', 'Explain OOP in Python.',
#      'Then your computer gets the request and looks at what the', 4, '2020-04-18', 1),
#     ('4', 'What happens next?',
#      'Finally, your computer sends the information or thing that', 1, '2019-06-13', 5),
#     ('5', 'Why do people use...', 'people to talk to your computer and get information',
#      2, '2023-11-25', 4)


#      """
# )


# # get a users discussion by their user id

# def get_users_discussions(user_id):
#     cur.execute(
#         """
#         SELECT title, content FROM discussions
#         WHERE user_id = %(user_id)s

#         """,
#         {
#             'user_id': user_id
#         }

#     )

#     results = cur.fetchall()
#     return results


# print(get_users_discussions(2))


# # change course_id for a specific discussion
# def change_course_for_discussion(discussion_id, new_course_id):
#     cur.execute(
#         """
#         UPDATE discussions SET course_id = %(new_course_id)s
#         WHERE id = %(discussion_id)s

#         """,
#         {
#             'discussion_id': discussion_id,
#             'new_course_id': new_course_id
#         }
#     )


# change_course_for_discussion(5, 3)
