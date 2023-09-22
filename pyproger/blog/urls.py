import locale

from flask import render_template, render_template_string, request

from ..dbase.database import get_paginated_posts, get_post
from .blog import bp

locale.setlocale(locale.LC_ALL, "")


@bp.route("/", methods=["GET"], defaults={"page": 1})
@bp.route("/<int:page>", methods=["GET"])
def index(page=1):
    per_page = 3
    posts, total_pages = get_paginated_posts(page, per_page)
    list_pages = [
        x for x in range(1, total_pages + 1) if x >= page - 2 and x <= page + 2
    ]
    return render_template(
        "blog/index.html",
        request=request,
        posts=posts,
        title="pyproger - разговоры про питон",
        menu_title="pyproger",
        page=page,
        total_pages=total_pages,
        list_pages=list_pages,
    )


@bp.route("/post/")
@bp.route("/post/<path:slug>")
def post(slug=None):
    if slug:
        current_post = get_post(slug)
        return render_template(
            "blog/postview.html",
            title=f"pyproger - {current_post.Post.title}",
            menu_title="pyproger",
            post=current_post,
        )
    else:
        return render_template_string("noup")
