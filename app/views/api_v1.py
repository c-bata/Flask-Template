from flask import Blueprint, jsonify, request, current_app, url_for
from urllib.parse import urljoin

from ..models import User

api = Blueprint('api', __name__)


@api.route('/')
def index():
    return jsonify(users=urljoin(request.host_url, url_for('.users')))


@api.route('/users')
def users():
    users = User.query.all()
    return jsonify(Users=[u.serialize for u in users])
