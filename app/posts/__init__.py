from flask import Blueprint

posts_blueprint = Blueprint('posts',__name__,url_prefix='/posts')
category_blueprint = Blueprint('category',__name__,url_prefix='/category')
from app.posts import views