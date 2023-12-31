import locale
import re

from flask import abort, current_app, render_template

from ..dbase.database import (
    get_all_posts_by_tag,
    get_page,
    get_paginated_posts,
    get_post,
    get_tags,
)
from .blog import bp

locale.setlocale(locale.LC_ALL, ("ru", "utf-8"))


@bp.route("/")
@bp.route("/<int:page>")
def index(page=1):
    per_page = current_app.config.get("POSTS_ON_PAGE")

    posts, total = get_paginated_posts(page, per_page)
    total_pages = total // per_page + [0, 1][total % per_page != 0]

    list_pages = [
        x for x in range(1, total_pages + 1) if x >= page - 2 and x <= page + 2
    ]
    return render_template(
        "blog/index.html",
        title=f'{current_app.config.get("BRAND")} - разговоры про питон',
        header_description="Про изучение python, веб разработку и прочие вещи",
        headers=current_app.config.get("SITE_HEADERS"),
        menu_title=current_app.config.get("BRAND"),
        menu_items=current_app.config.get("MENU_ITEMS"),
        posts=posts,
        page=page,
        total_pages=total_pages,
        list_pages=list_pages,
        mylinks=current_app.config.get("MYLINKS"),
        copyright=current_app.config.get("MYCOPYRIGHT"),
    )


@bp.route("/post/")
@bp.route("/post/<path:slug>")
def post(slug=None):
    if slug is not None:
        current_post = get_post(slug)

        if current_post is None:
            return abort(404)

        TAG_RE = re.compile(r"<[^>]+>")

        def remove_tags(text):
            return TAG_RE.sub("", text)

        title = remove_tags(current_post.Post.title)

        return render_template(
            "blog/postview.html",
            title=f'{current_app.config.get("BRAND")} - {title}',
            headers=current_app.config.get("SITE_HEADERS"),
            menu_title=current_app.config.get("BRAND"),
            menu_items=current_app.config.get("MENU_ITEMS"),
            post=current_post,
            mylinks=current_app.config.get("MYLINKS"),
            copyright=current_app.config.get("MYCOPYRIGHT"),
        )
    else:
        abort(404)


@bp.route("/tags/")
def get_all_tags():
    tags = get_tags()
    return render_template(
        "blog/tags.html",
        title=f'{current_app.config.get("BRAND")} - поиск по тэгу',
        header_description="Выбор статей по тематике",
        headers=current_app.config.get("SITE_HEADERS"),
        menu_title=current_app.config.get("BRAND"),
        tags=tags,
        menu_items=current_app.config.get("MENU_ITEMS"),
        mylinks=current_app.config.get("MYLINKS"),
        copyright=current_app.config.get("MYCOPYRIGHT"),
    )


@bp.route("/tag/")
@bp.route("/tag/<path:tag>/<int:page>")
def get_posts_by_tag(page=1, tag=None):
    per_page = current_app.config.get("POSTS_ON_PAGE")
    posts, total = get_all_posts_by_tag(tag, page, per_page)
    if posts is None:
        abort(404)

    total_pages = total // per_page + [0, 1][total % per_page != 0]

    list_pages = [
        x for x in range(1, total_pages + 1) if x >= page - 2 and x <= page + 2
    ]

    return render_template(
        "blog/tagget_posts.html",
        title=f'{current_app.config.get("BRAND")} - посты по {tag}',
        header_description=f"Статьи по теме {tag}",
        headers=current_app.config.get("SITE_HEADERS"),
        menu_title=current_app.config.get("BRAND"),
        menu_items=current_app.config.get("MENU_ITEMS"),
        posts=posts,
        page=page,
        tag=tag,
        total_pages=total_pages,
        list_pages=list_pages,
        mylinks=current_app.config.get("MYLINKS"),
        copyright=current_app.config.get("MYCOPYRIGHT"),
    )


@bp.route("/<path:slug>")
def page(slug=None):
    page = get_page(slug)
    if page is None:
        abort(404)
    return render_template(
        "blog/page.html",
        title=f'{current_app.config.get("BRAND")} - {page.name}',
        header_description=page.header_description,
        headers=current_app.config.get("SITE_HEADERS"),
        menu_title=current_app.config.get("BRAND"),
        menu_items=current_app.config.get("MENU_ITEMS"),
        content_body=page.text,
        mylinks=current_app.config.get("MYLINKS"),
        copyright=current_app.config.get("MYCOPYRIGHT"),
    )
