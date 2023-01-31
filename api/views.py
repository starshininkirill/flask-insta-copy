from flask import Blueprint, render_template, jsonify
from utils import *
import logging

api_blueprint = Blueprint("api_blueprint", __name__, url_prefix='/api')

logging.basicConfig(filename='api.log', level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")


@api_blueprint.route('/posts/')
def page_api_posts():
    posts = get_posts_all()
    logging.info("Query: /api/posts/")
    return jsonify(posts)


@api_blueprint.route("/posts/<int:post_id>")
def page_api_one_post(post_id):
    logging.info(f"Query: /api/posts/{post_id}")
    post = get_post_by_pk(post_id)
    return jsonify(post)
