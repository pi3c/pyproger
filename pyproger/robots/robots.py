from flask import Blueprint

bp = Blueprint(
    "bp_robots",
    __name__,
    template_folder="templates/robots",
    static_folder="static",
)

from . import urls
