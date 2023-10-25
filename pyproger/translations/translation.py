from flask import Blueprint, current_app, request
from flask_babel import Babel


def get_locale():
    translations = current_app.config.get("LANGUAGES")
    return request.accept_languages.best_match(translations)


babel = Babel()

bp = Blueprint(
    "bp_translation",
    __name__,
)
