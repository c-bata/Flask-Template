from flask import Blueprint, jsonify, request, current_app, url_for

from ..models import User

api = Blueprint('api', __name__)


@api.route('/users')
def users():
    users = User.query.all()
    return jsonify(Users=[u.serialize for u in users])
