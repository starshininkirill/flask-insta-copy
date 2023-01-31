import json


def get_post_by_pk(pk):
    posts = get_posts_all()
    res_post = []
    for post in posts:
        if post['pk'] == pk:
            return post
    if res_post == []:
        raise(ValueError("Такого поста не сущестует"))


def get_comments_all():
    with open('data/comments.json', 'r', encoding='utf-8') as file:
        comments = json.load(file)
    return comments


def get_posts_all():
    with open('data/posts.json', 'r', encoding='utf-8') as file:
        posts = json.load(file)
    return posts


def get_posts_by_user(user_name):
    posts = get_posts_all()
    comments = get_comments_all()
    res = []
    user = []
    count_user = 0
    for comment in comments:
        if user_name in comment['commenter_name']:
            count_user += 1
    for post in posts:
        if user_name == post['poster_name']:
            count_user += 1
            res.append(post)
    if count_user > 0:
        return res
    else:
        raise(ValueError("Такого пользователя не существует"))


def search_for_posts(query):
    posts = get_posts_all()
    res = []
    for post in posts:
        if str(query).lower() in post['content'].lower():
            res.append(post)
    return res


def get_comments_by_post_id(post_id):
    posts = get_posts_all()
    find_post = get_post_by_pk(post_id)
    comments = get_comments_all()
    result = []
    for comment in comments:
        if comment['post_id'] == post_id:
            result.append(comment)
    return result

