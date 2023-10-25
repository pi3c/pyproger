from flask import make_response, render_template

from pyproger.dbase.database import get_posts_for_sitemap

from .robots import bp


@bp.route("/sitemap.xml", methods=["GET"])
def sitemap_xml():
    sm_posts = get_posts_for_sitemap()
    sm_render = render_template(
        "robots/sitemap.xml",
        sm_posts=sm_posts,
    )
    response = make_response(sm_render)
    response.headers["Content-Type"] = "application/rss+xml"
    response.mimetype = "application/xml"
    return response


@bp.route("/robots.txt", methods=["GET"])
def robots_txt():
    rt_render = render_template("robots/robots.txt")
    response = make_response(rt_render)
    response.headers["Content-Type"] = "text/plain; charset=utf-8"
    response.mimetype = "text/plain"
    return response
