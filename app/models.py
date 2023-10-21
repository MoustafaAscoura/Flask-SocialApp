from flask_sqlalchemy import SQLAlchemy
from flask import url_for

db = SQLAlchemy()

class Post(db.Model):
    __tablename__='post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    image = db.Column(db.String)
    body = db.Column(db.String)
    Category_id = db.Column(db.Integer, db.ForeignKey('category.id'),nullable=False)
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    @property
    def get_image_url(self):
        return url_for('static', filename=f'posts/images/{self.image}')

    @property
    def get_show_url(self):
        return  url_for('posts.show', id=self.id)

    @property
    def get_delete_url(self):
        return  url_for('posts.delete', id= self.id)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    posts = db.relationship('Post', backref='category', lazy=True)

    @property
    def get_show_url(self):
        return  url_for('category.show', id=self.id)
