import os

from dotenv import load_dotenv
from flask import Flask, render_template_string, request, send_from_directory, url_for
from flask_admin import helpers
from flask_ckeditor import CKEditor, upload_fail, upload_success
from flask_migrate import Migrate
from flask_security.core import Security

from pyproger.admin.views import FooterLinksView
from pyproger.dbase import Role, User, db, user_datastore
from pyproger.dbase.database import get_footer_links, get_headers, get_menu_items
from pyproger.dbase.models import FooterContactLinks, Page, Post, SiteHeaders, Tag


def create_app(test_config=None):
    app = Flask(__name__)

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
        dotenv_path = os.path.join(os.path.abspath(os.curdir), ".env")
        if os.path.exists(dotenv_path):
            load_dotenv(dotenv_path)
            app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
            app.config["SECURITY_PASSWORD_SALT"] = os.getenv("SECURITY_PASSWORD_SALT")
            app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
            app.config["MYCOPYRIGHT"] = {
                "year": os.getenv("COPYRIGHT_YEAR"),
                "name": os.getenv("COPYRIGHT_NAME"),
                "link": os.getenv("COPYRIGHT_LINK"),
                "city": os.getenv("COPYRIGHT_CITY"),
            }
            app.config["BRAND"] = os.getenv("BRAND")
    else:
        app.config.from_mapping(test_config)

    from .translations import babel
    from .translations import bp as bp_translate
    from .translations import get_locale

    babel.init_app(app, locale_selector=get_locale)
    app.register_blueprint(bp_translate)

    db.init_app(app)

    ckeditor = CKEditor()
    ckeditor.init_app(app)

    security = Security(app, user_datastore)

    migrate = Migrate(db=db)
    migrate.init_app(app)

    from .admin import admin

    admin.init_app(app)

    from pyproger.admin.views import (
        HeadersView,
        PageView,
        PostView,
        RoleView,
        TagView,
        UserView,
    )

    admin.add_view(
        RoleView(
            Role,
            db.session,
            category="Пользователи",
            name="Роли",
        )
    )
    admin.add_view(
        UserView(
            User,
            db.session,
            category="Пользователи",
            name="Юзеры",
        )
    )
    admin.add_view(
        TagView(
            Tag,
            db.session,
            category="Посты",
            name="Тэги постов",
        )
    )
    admin.add_view(
        PostView(
            Post,
            db.session,
            category="Посты",
            name="Посты",
        )
    )
    admin.add_view(
        PageView(
            Page,
            db.session,
            category="Страницы",
            name="Статические страницы блога",
        )
    )
    admin.add_view(
        HeadersView(
            SiteHeaders,
            db.session,
            category="Страницы",
            name="Включаемые в html заголовки",
        )
    )
    admin.add_view(
        FooterLinksView(
            FooterContactLinks,
            db.session,
            category="Страницы",
            name="Иконки-ссылки футера",
        )
    )

    from pyproger.blog.blog import bp as bp_blog
    from pyproger.cli.commands import bp_cli
    from pyproger.errors import bp as bp_errors
    from pyproger.robots.robots import bp as bp_robots

    app.register_blueprint(bp_cli)
    app.register_blueprint(bp_blog)
    app.register_blueprint(bp_errors)
    app.register_blueprint(bp_robots)

    with app.app_context():
        try:
            site_headers = get_headers()
        except Exception as e:
            print(e)
            site_headers = None
        app.config["SITE_HEADERS"] = site_headers

        try:
            menu_items = get_menu_items()
        except Exception as e:
            print(e)
            menu_items = None
        app.config["MENU_ITEMS"] = menu_items

        try:
            links = get_footer_links()
        except Exception as e:
            print(e)
            links = None
        app.config["MYLINKS"] = links

    @security.context_processor
    def security_context_processor():
        return dict(
            admin_base_template=admin.base_template,
            admin_view=admin.index_view,
            h=helpers,
            get_url=url_for,
        )

    @app.context_processor
    def utility_processor():
        return dict(
            page_lang=get_locale(),
        )

    @app.route("/ping")
    def hello():
        return render_template_string("pong")

    @app.route("/files/<filename>")
    def uploaded_files(filename):
        path = app.config["UPLOADED_PATH"]
        return send_from_directory(path, filename)

    @app.route("/upload", methods=["POST"])
    def upload():
        f = request.files.get("upload")
        extension = f.filename.split(".")[-1].lower()
        if extension not in ["jpg", "gif", "png", "jpeg"]:
            return upload_fail(message="Image only!")
        f.save(os.path.join(app.config["UPLOADED_PATH"], f.filename))
        url = url_for("uploaded_files", filename=f.filename)
        return upload_success(url=url)

    @app.route("/favicon.ico")
    def favicon():
        return send_from_directory(
            os.path.join(app.root_path, "static"),
            "favicon.ico",
            mimetype="image/vnd.microsoft.icon",
        )

    return app
