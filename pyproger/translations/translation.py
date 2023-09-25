import os

from flask import Blueprint, request
from flask_babel import Babel


def get_locale():
    translations = ["ru"]
    return request.accept_languages.best_match(translations)


babel = Babel()

bp = Blueprint(
    "bp_translation",
    __name__,
)
