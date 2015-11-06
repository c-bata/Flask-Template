from flask import Blueprint, jsonify, request, current_app, url_for
from urllib.parse import urljoin

from ..models import User

accounts = Blueprint('accounts', __name__)


@accounts.route('/')
def index():
    return jsonify(users=urljoin(request.host_url, url_for('.users')))


@accounts.route('/users')
def users():
    users = User.query.all()
    return jsonify(Users=[u.serialize for u in users])
