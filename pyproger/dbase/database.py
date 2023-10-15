from . import db
from .models import FooterContactLinks, Page, Post, SiteHeaders, Tag, User


def get_paginated_posts(page, per_page):
    all_post_query = (
        db.session.query(Post, User)
        .join(User, Post.author == User.id)
        .filter(Post.published.is_(True))
        .order_by(Post.create_datetime.desc())
        .paginate(page=page, per_page=per_page, error_out=True)
    )
    return all_post_query, all_post_query.total


def get_post(slug):
    post_query = (
        db.session.query(Post, User)
        .join(User, Post.author == User.id)
        .filter(Post.published.is_(True))
        .filter(Post.slug == slug)
        .first()
    )
    return post_query


def get_tags():
    tags_query = db.session.query(Tag).order_by(Tag.tag)
    return tags_query


def get_all_posts_by_tag(tag, page, per_page):
    posts_query = (
        db.session.query(Post, User)
        .join(User, Post.author == User.id)
        .filter(Post.published.is_(True))
        .filter(Post.tags.any(Tag.tag == tag))
        .order_by(Post.create_datetime.desc())
        .paginate(page=page, per_page=per_page, error_out=True)
    )
    if posts_query.total == 0:
        return None, False
    print(posts_query.total)
    return posts_query, posts_query.total


def get_page(slug):
    page_query = db.session.query(Page).filter(Page.slug == slug).one_or_none()
    return page_query


def get_menu_items():
    menu_items = db.session.query(Page.name, Page.slug).all()
    return menu_items


def get_posts_for_sitemap():
    posts = (
        db.session.query(
            Post.slug,
            Post.update_datetime,
        )
        .filter(Post.published.is_(True))
        .all()
    )
    return posts


def get_headers():
    headers = (
        db.session.query(SiteHeaders.content)
        .filter(SiteHeaders.enabled.is_(True))
        .all()
    )
    return headers


def get_footer_links():
    links = db.session.query(
        FooterContactLinks.link,
        FooterContactLinks.bootstrap_ico,
    ).all()
    return links
