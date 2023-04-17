
from flask import Blueprint, jsonify, request, abort
from ..models import Discussion, Student, db


bp = Blueprint('discussions', __name__, url_prefix='/discussions')


@bp.route('', methods=['GET'])  # decorator takes path and list of HTTP verbs
def index():
    discussions = Discussion.query.all()  # ORM performs SELECT query
    result = []
    for d in discussions:
        # build list of discussions as dictionaries
        result.append(d.serialize())
    return jsonify(result)  # return JSON response


@bp.route('', methods=['POST'])
def create():
    if 'stu_id' not in request.json or 'content' not in request.json:
        return abort(400)
    Student.query.get_or_404(request.json['stu_id'])

    d = Discussion(
        title=request.json['title'],
        content=request.json['content'],
        stu_id=request.json['stu_id'],
        course_id=request.json['course_id'],
    )
    db.session.add(d)  # prepare CREATE statement
    db.session.commit()  # execute CREATE statement
    return jsonify(d.serialize())


@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    d = Discussion.query.get_or_404(id)
    try:
        db.session.delete(d)  # prepare DELETE statement
        db.session.commit()  # execute DELETE statement
        return jsonify(True)
    except:
        # something went wrong :(
        return jsonify(False)
