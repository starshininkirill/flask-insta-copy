from flask import Blueprint, render_template, request
from utils import *

user_blueprint = Blueprint("user_blueprint", __name__, template_folder='templates')


@user_blueprint.route("/users/<user_name>")
def page_user(user_name):
    user_posts = get_posts_by_user(user_name)
    count_posts = len(user_posts)
    return render_template("user-feed.html", posts=user_posts, count=count_posts)