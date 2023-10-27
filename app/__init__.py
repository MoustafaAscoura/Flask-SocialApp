from flask import Flask
from app.config import projectConfig as AppConfig
from flask_migrate import Migrate
from flask_restful import Api

from app.models import db

from app.posts.apiviews import PostsView, PostView

def create_app(config_name='dev'):
    app = Flask(__name__)
    current_config = AppConfig[config_name]
    app.config['SQLALCHEMY_DATABASE_URI'] = current_config.SQLALCHEMY_DATABASE_URI
    app.config.from_object(current_config)
    app.config['UPLOAD_FOLDER'] = './static/posts/images'

    db.init_app(app)
    migrate = Migrate(app, db, render_as_batch=True)

    #Api settings
    api = Api(app)
    api.add_resource(PostsView, '/api/posts')
    api.add_resource(PostView, '/api/posts/<int:id>')


    #register blueprint in the application
    from app.posts import posts_blueprint, category_blueprint
    app.register_blueprint(posts_blueprint)
    app.register_blueprint(category_blueprint)

    
    return app

