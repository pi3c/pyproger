from flask import current_app, render_template

from . import bp


@bp.app_errorhandler(404)
def handle_404(err):
    return (
        render_template(
            "errors/404.html",
            title=f'{current_app.config.get("BRAND")} - поиск по тэгу',
            headers=current_app.config.get("SITE_HEADERS"),
            menu_title=current_app.config.get("BRAND"),
            menu_items=current_app.config.get("MENU_ITEMS"),
            mylinks=current_app.config.get("MYLINKS"),
            copyright=current_app.config.get("MYCOPYRIGHT"),
        ),
        404,
    )
