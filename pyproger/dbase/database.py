from . import db
from .models import Post, User


def get_paginated_posts(page, per_page):
    quer = (
        db.session.query(Post, User)
        .join(User, Post.author == User.id)
        .order_by(Post.create_datetime.desc())
        .paginate(page=page, per_page=per_page, error_out=False)
    )
    total_pages = quer.total // per_page + [0, 1][quer.total % per_page != 0]

    return quer, total_pages


def get_post(slug):
    post_query = (
        db.session.query(Post, User)
        .join(User, Post.author == User.id)
        .filter(Post.slug == slug)
        .first()
    )
    return post_query
