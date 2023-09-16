from flask import Flask, render_template_string


def create_app():
    app = Flask(__name__)

    @app.route("/index")
    @app.route("/")
    def index() -> str:
        return render_template_string("pyproger temporary page")

    return app
