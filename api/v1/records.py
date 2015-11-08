from flask import Blueprint, jsonify, request, current_app, url_for

from . import api
from ..models import User, Record


@api.route('users/<int:user_id>/records', methods=['GET', 'POST'])
def records(user_id):
    """
    GET: Get record list
    POST: Create record
    """
    if request.method == 'POST':
        pass
    else:
        return jsonify(records=[
            record.serialize for record in Record.query.get(user_id=user_id)
        ])


@api.route('users/<int:user_id>/records/<int:record_id>',
           methods=['GET', 'PUT', 'DELETE'])
def record_detail(user_id, record_id):
    """
    GET: GET record detail
    PUT: Update record info
    DELETE: Remove record
    """
    record = Record.query.filter(user_id=user_id).get(record_id)

    if request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass
    else:
        return jsonify(
            record=record.serialize
        )
