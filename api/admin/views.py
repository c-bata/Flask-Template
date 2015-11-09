import flask_admin
from flask.ext.admin.contrib.sqla import ModelView


class CustomAdminIndexView(flask_admin.AdminIndexView):
    @flask_admin.expose('/')
    def index(self):
        return 'Hello World'


class UserAdmin(ModelView):
    column_exclude_list = ['password_hash', ]
    column_labels = {
        "name": "ユーザ名",
        "email": "メールアドレス",
        "is_superuser": "管理者権限",
    }
    can_create = False


class RecordAdmin(ModelView):
    column_labels = {
        "day": "作業日",
        "begin_time": "開始時間",
        "finish_time": "終了時間",
        "contents": "作業内容",
    }
