from flask import Blueprint

bp = Blueprint(
    "bp_blog",
    __name__,
    template_folder="templates/blog",
)

from . import urls
