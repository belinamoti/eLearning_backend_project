
from flask import Blueprint, jsonify, request
from ..models import Enrollment, Course, db


bp = Blueprint('enrollments', __name__, url_prefix='/enrollments')


@bp.route('', methods=['GET'])  # decorator takes path and list of HTTP verbs
def index():
    enrollments = Enrollment.query.all()  # ORM performs SELECT query
    result = []
    for e in enrollments:
        result.append(e.serialize())
    return jsonify(result)  # return JSON response


@bp.route('/not_paid', methods=['GET'])
def unpaid_students():
    unpaid_enrollments = Enrollment.query.filter_by(paid=False).all()
    unpaid_students = [enrollment.serialize()
                       for enrollment in unpaid_enrollments]
    return jsonify(unpaid_students)


@bp.route('/amount_due/<int:stu_id>')
def amount_due(stu_id):
    unpaid_enrollments = Enrollment.query.filter_by(
        stu_id=stu_id, paid=False).all()
    amount_due = sum([Course.query.get(
        enrollment.course_id).price for enrollment in unpaid_enrollments])
    return jsonify({'amount_due': amount_due})
