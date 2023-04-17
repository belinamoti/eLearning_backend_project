

from flask import Blueprint, jsonify, request
from sqlalchemy.orm import joinedload
from ..models import Instructor, Course, Department, db


bp = Blueprint('instructors', __name__, url_prefix='/instructors')


@bp.route('', methods=['GET'])  # decorator takes path and list of HTTP verbs
def index():
    instructors = Instructor.query.all()  # ORM performs SELECT query
    result = []
    for i in instructors:
        result.append(i.serialize())
    return jsonify(result)  # return JSON response


# decorator takes path and list of HTTP verbs
@bp.route('/<int:id>', methods=['GET'])
def show_instructor_by_id(id: int):
    instructor = Instructor.query.get_or_404(id)
    return jsonify(instructor.serialize())

# Assign a chair for a department by seting the is_chair attribute to True


@bp.route('/assign_chair/<int:id>', methods=['PUT', 'PATCH'])
def update_instructor(id: int):
    instructor = Instructor.query.get_or_404(id)

    if 'dept_id' in request.json:
        dept_id = request.json['dept_id']
        department = Department.query.get(dept_id)
        if not department:
            return jsonify({'error': 'Department not found'}), 404

        instructor.dept_id = dept_id
        instructor.is_chair = True

    try:
        db.session.commit()
        return jsonify(instructor.serialize())
    except:
        return jsonify(False)


@bp.route('/<int:id>/courses', methods=['GET'])
def get_instructor_courses(id):
    # checks if the instructor exists in the intructors table, and if not, return a 404 error status message

    instructor = Instructor.query.get_or_404(id)

    courses = Course.query.options(joinedload('instructors')).filter(
        Course.instructors.contains(instructor)).all()

    # return a list of dictionaries containing the id and course_name of each course in the response
    result = []
    for course in courses:
        course_data = {'course_id': course.id,
                       'course_name': course.course_name}
        result.append(course_data)
    return jsonify(result)


# added an import statement for joinedload from sqlalchemy.orm,
# which is used to eagerly load the related instructors data.
# I then modified the query to join the Course table with the
# Instructor table using joinedload and filter by the instructor
# using the contains method.
