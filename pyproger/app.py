from flask import Flask, render_template_string, url_for
from flask_admin import helpers
from flask_ckeditor import CKEditor
from flask_migrate import Migrate
from flask_security.core import Security

from pyproger.dbase import Role, User, db, user_datastore
from pyproger.dbase.models import Post, Tag


def create_app(test_config=None):
    app = Flask(__name__)

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    db.init_app(app)

    ckeditor = CKEditor()
    ckeditor.init_app(app)

    security = Security(app, user_datastore)

    migrate = Migrate(db=db)
    migrate.init_app(app)

    from .admin import admin

    admin.init_app(app)

    from pyproger.admin.views import PostView, RoleView, TagView, UserView

    admin.add_view(RoleView(Role, db.session, category="Пользователи"))
    admin.add_view(UserView(User, db.session, category="Пользователи"))
    admin.add_view(TagView(Tag, db.session, category="Посты"))
    admin.add_view(PostView(Post, db.session, category="Посты"))

    from pyproger.cli.commands import bp_cli

    app.register_blueprint(bp_cli)

    @security.context_processor
    def security_context_processor():
        return dict(
            admin_base_template=admin.base_template,
            admin_view=admin.index_view,
            h=helpers,
            get_url=url_for,
        )

    @app.route("/ping")
    def hello():
        return render_template_string("pong")

    return app
