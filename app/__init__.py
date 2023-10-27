from flask import Flask
from app.config import projectConfig as AppConfig
from flask_migrate import Migrate

from app.models import db, Post, Category

def create_app(config_name='dev'):
    app = Flask(__name__)
    current_config = AppConfig[config_name]
    app.config['SQLALCHEMY_DATABASE_URI'] = current_config.SQLALCHEMY_DATABASE_URI
    app.config.from_object(current_config)
    app.config['UPLOAD_FOLDER'] = './static/posts/images'

    db.init_app(app)
    migrate = Migrate(app, db, render_as_batch=True)

    #register blueprint in the application
    from app.posts import posts_blueprint, category_blueprint
    app.register_blueprint(posts_blueprint)
    app.register_blueprint(category_blueprint)


    # with app.app_context():
    #     db.create_all()

    #     from app.postsData import data
    #     posts = data['posts']
    #     for i in range(len(posts)):
    #         post = posts[i]
    #         for cat in post['tags']:
    #             if Category.query.filter_by(name=cat).first() is None:
    #                 _category = Category(name=cat)
    #                 db.session.add(_category)
    #                 db.session.commit()
    #         category=Category.query.filter_by(name=post['tags'][0]).first()
    #         _post = Post(title=post['title'], body=post['body'],image=f"picture{post['id']}.png",category=category)
    #         db.session.add(_post)
        
    #     db.session.commit()
    #     print(Post.query.all())
    
    return app

