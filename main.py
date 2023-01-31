from utils import *
from flask import Flask, render_template
from main.views import main_blueprint
from posts.views import posts_bluprint
from search.views import search_blueprint
from user.views import user_blueprint
from api.views import api_blueprint

app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(posts_bluprint)
app.register_blueprint(search_blueprint)
app.register_blueprint(user_blueprint)
app.register_blueprint(api_blueprint)


@app.errorhandler(500)
def error_500(er):
    return "Ошибка загрузки данных"


@app.errorhandler(404)
def error_404(er):
    return "Страница не найдена"


if __name__ == "__main__":
    app.run()