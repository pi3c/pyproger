import locale

from flask import (
    abort,
    current_app,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

from ..dbase.database import (
    get_all_posts_by_tag,
    get_menu_items,
    get_page,
    get_paginated_posts,
    get_post,
    get_tags,
)
from .blog import bp

locale.setlocale(locale.LC_ALL, "")


@bp.route("/", methods=["GET"], defaults={"page": 1})
@bp.route("/<int:page>")
def index(page=1):
    session["back_url"] = request.url
    per_page = current_app.config.get("POSTS_ON_PAGE")

    posts, total_pages = get_paginated_posts(page, per_page)
    list_pages = [
        x for x in range(1, total_pages + 1) if x >= page - 2 and x <= page + 2
    ]
    menu_items = get_menu_items()
    return render_template(
        "blog/index.html",
        title="pyproger - разговоры про питон",
        menu_title="pyproger",
        menu_items=menu_items,
        posts=posts,
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

        if current_post is None:
            return abort(404)
        menu_items = get_menu_items()

        return render_template(
            "blog/postview.html",
            title=f"pyproger - {current_post.Post.title}",
            menu_title="pyproger",
            menu_items=menu_items,
            post=current_post,
            back_url=back_url,
        )
    else:
        abort(404)


@bp.route("/tags/")
def get_all_tags():
    tags = get_tags()
    menu_items = get_menu_items()
    return render_template(
        "blog/tags.html",
        title="pyproger - поиск по тэгу",
        menu_title="pyproger",
        tags=tags,
        menu_items=menu_items,
    )


@bp.route("/tag/", methods=["GET"], defaults={"page": 1})
@bp.route("/tag/<path:tag>")
def get_posts_by_tag(page=1, tag=None):
    if tag is None:
        tag = request.args.get("tag")
        if tag is None:
            return redirect(url_for(".get_all_tags"))
    per_page = current_app.config.get("POSTS_ON_PAGE")

    posts, total_pages = get_all_posts_by_tag(tag, page, per_page)
    if posts is None:
        abort(404)
    list_pages = [
        x for x in range(1, total_pages + 1) if x >= page - 2 and x <= page + 2
    ]
    menu_items = get_menu_items()

    return render_template(
        "blog/index.html",
        title=f"pyproger - посты по {tag}",
        menu_title="pyproger",
        menu_items=menu_items,
        posts=posts,
        page=page,
        total_pages=total_pages,
        list_pages=list_pages,
    )


@bp.route("/<path:slug>")
def page(slug=None):
    page = get_page(slug)
    if page is None:
        abort(404)
    menu_items = get_menu_items()
    return render_template(
        "blog/page.html",
        title=f"pyproger - {page.name}",
        menu_title="pyproger",
        menu_items=menu_items,
        content_body=page.text,
    )
