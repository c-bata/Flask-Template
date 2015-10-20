from flask import Blueprint, jsonify, current_app
from flask.ext.sqlalchemy import get_debug_queries

from .. import db
from ..models import User

api = Blueprint('api', __name__)


@api.route('/')
def users():
    users = User.query.all()
    return jsonify(Users=[u.serialize for u in users])

