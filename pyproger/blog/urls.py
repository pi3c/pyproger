import locale

from flask import (redirect, render_template, render_template_string, request,
                   session, url_for)

from ..dbase.database import (get_all_posts_by_tag, get_paginated_posts,
                              get_post, get_tags)
from .blog import bp

locale.setlocale(locale.LC_ALL, "")


@bp.route("/", methods=["GET"], defaults={"page": 1})
@bp.route("/<int:page>", methods=["GET"])
def index(page=1):
    session["back_url"] = request.url
    per_page = 2
    posts, total_pages = get_paginated_posts(page, per_page)
    list_pages = [
        x for x in range(1, total_pages + 1) if x >= page - 2 and x <= page + 2
    ]
    return render_template(
        "blog/index.html",
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
    back_url = session.get("back_url")
    if slug is not None:
        current_post = get_post(slug)
        return render_template(
            "blog/postview.html",
            title=f"pyproger - {current_post.Post.title}",
            menu_title="pyproger",
            post=current_post,
            back_url=back_url,
        )
    else:
        return render_template_string("noup")


@bp.route("/tags/")
def get_all_tags():
    tags = get_tags()
    return render_template(
        "blog/tags.html",
        tags=tags,
        title="pyproger - поиск по тэгу",
        menu_title="pyproger",
    )


@bp.route("/tag/", methods=["GET"], defaults={"page": 1})
@bp.route("/tag/<path:tag>", methods=["GET"])
def get_posts_by_tag(page=1):
    tag = request.args.get("tag")
    if tag is None:
        return redirect(url_for(".get_all_tags"))
    per_page = 2
    posts, total_pages = get_all_posts_by_tag(tag, page, per_page)
    list_pages = [
        x for x in range(1, total_pages + 1) if x >= page - 2 and x <= page + 2
    ]
    return render_template(
        "blog/index.html",
        posts=posts,
        title=f"pyproger - посты по {tag}",
        menu_title="pyproger",
        page=page,
        total_pages=total_pages,
        list_pages=list_pages,
    )
