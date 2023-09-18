import datetime

from flask_security.models import fsqla
from sqlalchemy import Boolean, Column, DateTime, Integer, String, Text
from sqlalchemy.util import unique_list

from . import db


class Role(db.Model, fsqla.FsRoleMixin):
    def __str__(self) -> str:
        return self.name


class User(db.Model, fsqla.FsUserMixin):
    first_name = Column(String(255))
    last_name = Column(String(255))
    posts = db.relationship("Post", backref="user", lazy="dynamic")

    def __str__(self) -> str:
        return self.email


tag_post = db.Table(
    "tag_post",
    db.Column("tag_id", db.Integer, db.ForeignKey("tag.id")),
    db.Column("post_id", db.Integer, db.ForeignKey("post.id")),
)


class Tag(db.Model):
    __tablename__ = "tag"

    id = Column(Integer, primary_key=True)
    tag = Column(String(20))

    def __str__(self) -> str:
        return self.tag


class Post(db.Model):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    author = Column(Integer, db.ForeignKey("user.id"))
    slug = Column(String(30), primary_key=True, nullable=True)
    title = Column(String(50), nullable=False)
    published = Column(Boolean, default=False)
    tags = db.relationship("Tag", secondary=tag_post)

    create_datetime = Column(
        DateTime(), nullable=True, default=datetime.datetime.utcnow()
    )
    update_datetime = Column(
        DateTime(),
        nullable=True,
    )
    text = Column(Text)
