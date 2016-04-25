from flask import Blueprint, jsonify, url_for

api = Blueprint('api', __name__)


@api.route('/')
def index():
    return jsonify(link=[
        {
            "uri": url_for('.users'),
            "rel": "users"
        }
    ])


# do this last to avoid circular dependencies
from . import records, users
