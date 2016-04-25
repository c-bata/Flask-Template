from flask import Blueprint, jsonify, request, current_app, url_for

from . import api
from ..models import User


@api.route('/users', methods=['GET', 'POST'])
def users():
    """
    GET: Get user list
    POST: Create user
    """
    if request.method == 'POST':
        pass
    else:
        return jsonify(
            users=[user.serialize for user in User.query.all()],
        )


@api.route('/users/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
def user_detail(user_id):
    """
    GET: GET user detail
    PUT: Update user profile
    DELETE: Remove user account
    """
    user = User.query.get(user_id)

    if request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass
    else:
        return jsonify(
            user=user.serialize,
            records=[record.serialize for record in user.records]
        )
