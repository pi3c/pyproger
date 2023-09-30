from . import db
from .models import Post, Tag, User


def get_paginated_posts(page, per_page):
    all_post_query = (
        db.session.query(Post, User)
        .join(User, Post.author == User.id)
        .order_by(Post.create_datetime.desc())
        .paginate(page=page, per_page=per_page, error_out=True)
    )
    total_pages = (
        all_post_query.total // per_page + [0, 1][all_post_query.total % per_page != 0]
    )

    return all_post_query, total_pages


def get_post(slug):
    post_query = (
        db.session.query(Post, User)
        .join(User, Post.author == User.id)
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
        .filter(Post.tags.any(Tag.tag == tag))
        .order_by(Post.create_datetime.desc())
        .paginate(page=page, per_page=per_page, error_out=True)
    )
    total_pages = (
        posts_query.total // per_page + [0, 1][posts_query.total % per_page != 0]
    )
    if posts_query.total == 0:
        return None, None
    return posts_query, total_pages
