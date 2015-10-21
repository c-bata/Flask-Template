from flask import Blueprint, current_app

cms = Blueprint('cms', __name__)


@cms.route('/')
def index():
    return 'Hello Flask!'


@cms.route('/mypage')
def mypage():
    return 'This is user page.'
