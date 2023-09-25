from flask import Blueprint

bp = Blueprint(
    "bp_blog",
    __name__,
    template_folder="templates/blog",
    static_folder="static",
)

from . import urls
