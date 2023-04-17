
import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Enrollment(db.Model):
    __tablename__ = 'enrollments'
    stu_id = db.Column(db.Integer, db.ForeignKey(
        'students.id'), primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey(
        'courses.id'), primary_key=True)
    semester = db.Column(db.String(10), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    paid = db.Column(db.Boolean, nullable=False)

    def __init__(self, stu_id: int, course_id: int, semester: str, year: int, paid: int):
        self.stu_id = stu_id
        self.course_id = course_id
        self.semester = semester
        self.year = year
        self.paid = paid

    def serialize(self):
        return {
            'stu_id': self.stu_id,
            'course_id': self.course_id,
            'semester': self.semester,
            'year': self.year,
            'paid': self.paid

        }


class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    stu_lname = db.Column(db.String(128), nullable=False)
    stu_fname = db.Column(db.String(128), nullable=False)
    stu_email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), unique=True, nullable=False)
    username = db.Column(db.String(128), unique=True, nullable=False)
    dept_id = db.Column(db.Integer, db.ForeignKey(
        'departments.id'), nullable=True)

    discussions = db.relationship(
        'Discussion', backref='students', cascade="all,delete")

    enrollments = db.relationship('Enrollment', backref='students', lazy=True)

    def __init__(self, stu_lname: str, stu_fname: str, stu_email: str, password: str, username: str, dept_id: int):
        self.stu_lname = stu_lname
        self.stu_fname = stu_fname
        self.stu_email = stu_email
        self.username = username
        self.password = password
        self.dept_id = dept_id

    def serialize(self):
        return {
            'id': self.id,
            'stu_lname': self.stu_lname,
            'stu_fname': self.stu_fname,
            'stu_email': self.stu_email,
            'username': self.username,
            'dept_id': self.dept_id


        }


class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    course_name = db.Column(db.String(128), unique=True, nullable=False)
    description = db.Column(db.String(280))
    content = db.Column(db.String(280), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    dept_id = db.Column(db.Integer, db.ForeignKey(
        'departments.id'), nullable=True)

    enrollments = db.relationship('Enrollment', backref='courses', lazy=True)

    course_instructors = db.relationship(
        'Instructor', backref='courses', cascade="all,delete")

    def __init__(self, course_name: str, description: str, content: str, price: int, dept_id: int):
        self.course_name = course_name
        self.description = description
        self.content = content
        self.price = price
        self.dept_id = dept_id

    def serialize(self):
        return {
            'id': self.id,
            'course_name': self.course_name,
            'description': self.description,
            'content': self.content,
            'price': self.price,
            'dept_id': self.dept_id


        }


class Department(db.Model):
    __tablename__ = 'departments'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    dept_name = db.Column(db.String(128), unique=True, nullable=False)

    instructors = db.relationship(
        'Instructor', backref='department', lazy=True)

    def __init__(self, dept_name: str):
        self.dept_name = dept_name

    def serialize(self):
        return {
            'id': self.id,
            'dept_name': self.dept_name

        }


class Instructor(db.Model):
    __tablename__ = 'instructors'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)

    dept_id = db.Column(db.Integer, db.ForeignKey(
        'departments.id'), nullable=True)

    is_chair = db.Column(db.Boolean, default=False, nullable=False)

    course_id = db.Column(db.Integer, db.ForeignKey(
        'courses.id'), nullable=True)

    instructor_courses = db.relationship(
        'Course', backref='instructors', cascade="all,delete")

    def __init__(self, first_name: str, last_name: str, email: str, course_id: int, dept_id: int, is_chair: bool = False):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.course_id = course_id
        self.dept_id = dept_id
        self.is_chair = is_chair

    def serialize(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'course_id': self.course_id,
            'dept_id': self.dept_id,
            'is_chair': self.is_chair


        }


class Discussion(db.Model):
    __tablename__ = 'discussions'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(280))
    content = db.Column(db.String(128), nullable=False, unique=True)
    created_at = db.Column(
        db.DateTime,
        default=datetime.datetime.utcnow,
        nullable=False
    )

    stu_id = db.Column(db.Integer, db.ForeignKey(
        'students.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey(
        'courses.id'), nullable=True)

    def __init__(self, title: str, content: str, stu_id: int, course_id: int):
        self.title = title
        self.content = content
        self.stu_id = stu_id
        self.course_id = course_id

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'created_at': self.created_at.isoformat(),
            'stu_id': self.stu_id,
            'course_id': self.course_id

        }
