
from flask import Blueprint, jsonify, abort, request
from ..models import Student, db
import hashlib
import secrets


def scramble(password: str):
    """Hash and salt the given password"""
    salt = secrets.token_hex(16)
    return hashlib.sha512((password + salt).encode('utf-8')).hexdigest()


bp = Blueprint('students', __name__, url_prefix='/students')


@bp.route('', methods=['GET'])
def index():
    students = Student.query.all()
    students = [s.serialize() for s in students]
    return jsonify(students)


@bp.route('', methods=['POST'])
def create():

    if len(request.json['username']) < 5 or len(request.json['password']) < 6:
        return abort(400)

    s = Student(
        stu_lname=request.json['stu_lname'],
        stu_fname=request.json['stu_fname'],
        stu_email=request.json['stu_email'],
        dept_id=request.json['dept_id'],
        username=request.json['username'],
        password=scramble(request.json['password'])
    )
    db.session.add(s)  # prepare CREATE statement
    db.session.commit()  # execute CREATE statement
    return jsonify(s.serialize())
