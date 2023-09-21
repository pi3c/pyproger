import os

from flask import Blueprint, request
from flask_babel import Babel


def get_locale():
    translations = ["en", "ru"]
    return request.accept_languages.best_match(translations)


babel = Babel()

bp = Blueprint(
    "bp_translation",
    __name__,
    cli_group="translate",
)


@bp.cli.command("update")
def update():
    """Update all languages."""
    if os.system("pybabel extract -F babel.cfg -k _l -o messages.pot ."):
        raise RuntimeError("extract command failed")
    if os.system("pybabel update -i messages.pot -d pi3code/translations"):
        raise RuntimeError("update command failed")
    os.remove("messages.pot")


@bp.cli.command("compile")
def compile():
    """Compile all languages."""
    if os.system("pybabel compile -d pi3code/translations"):
        raise RuntimeError("compile command failed")
