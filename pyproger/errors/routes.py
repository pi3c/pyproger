from flask import render_template, url_for

from . import bp


@bp.app_errorhandler(404)
def handle_404(err):
    return (
        render_template(
            "errors/404.html",
            title="pyproger - Страница не найдена",
            menu_title="pyproger",
        ),
        404,
    )
