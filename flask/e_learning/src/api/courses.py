

from flask import Blueprint, jsonify, request, abort
from ..models import Course, db


bp = Blueprint('courses', __name__, url_prefix='/courses')


@bp.route('', methods=['GET'])  # decorator takes path and list of HTTP verbs
def index():
    courses = Course.query.all()  # ORM performs SELECT query
    result = []
    for c in courses:
        result.append(c.serialize())
    return jsonify(result)  # return JSON response


# Update course prices
@bp.route('/<int:id>', methods=['PATCH', 'PUT'])
def update_price_by_id(id: int):

    c = Course.query.get_or_404(id)

    c.price = request.json['price']

    try:
        db.session.commit()
        return jsonify(c.serialize())
    except:
        return jsonify(False)


# Applyin 25% discount to all course prices
@bp.route('/apply_discount', methods=['PATCH', 'PUT'])
def update_all_course_price():

    courses = Course.query.all()

    discounted_courses = []

    for c in courses:
        c.price = round(c.price * 0.5)
        discounted_courses.append(c)

    try:
        db.session.commit()
        return jsonify([c.serialize() for c in discounted_courses])
    except:
        # something went wrong :(
        return jsonify(False)
