from flask import Blueprint, render_template, request
from utils import *

search_blueprint = Blueprint("search_blueprint", __name__, template_folder='templates')


@search_blueprint.route("/search/")
def search_pade():
    search_word = request.args.get('search')
    posts = search_for_posts(search_word)
    count_posts = len(posts)
    return render_template('search.html', posts=posts, count=count_posts)