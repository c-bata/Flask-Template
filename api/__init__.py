from flask import Flask
from flask.ext.sqlalchemy import get_debug_queries
from flask.ext.migrate import Migrate
from flask_admin import Admin

from .admin.views import CustomAdminIndexView, UserAdmin, RecordAdmin
from .models import db, User, Record


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    db.init_app(app)
    Migrate(app, db)

    # Register the blueprint applications
    from .v1 import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/v1')

    # Flask-Admin
    admin = Admin(app, name='研究時間記録', index_view=CustomAdminIndexView(),
                  template_mode='bootstrap3')
    admin.add_view(UserAdmin(User, db.session, name='ユーザ'))
    admin.add_view(RecordAdmin(Record, db.session, name='研究記録'))

    # Define special routes
    @app.after_request
    def after_request(response):
        for query in get_debug_queries():
            if query.duration >= app.config['SLOW_DB_QUERY_TIME']:
                app.logger.warning(
                    'Slow query: %s\nParameters: %s\n'
                    'Duration: %fs\nContext: %s\n'
                    % (query.statement, query.parameters,
                       query.duration, query.context)
                )
        return response

    @app.errorhandler(404)
    def page_not_found(e):
        """Return a custom 404 error."""
        return 'Sorry, Nothing at this URL.', 404

    @app.errorhandler(500)
    def page_not_found(e):
        """Return a custom 500 error."""
        return 'Sorry, unexpected error: {}'.format(e), 500

    return app

