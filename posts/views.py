from flask import Blueprint, render_template
from utils import *

posts_bluprint = Blueprint("posts_blueprint", __name__, template_folder='templates')


@posts_bluprint.route('/posts/<int:post_id>')
def page_post(post_id):
    post = get_post_by_pk(post_id)
    comments = get_comments_by_post_id(post_id)
    count_comments = len(comments)
    return render_template('post.html', post=post, comments=comments, count_comments=count_comments)