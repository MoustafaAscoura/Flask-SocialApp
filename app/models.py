from flask_sqlalchemy import SQLAlchemy
from flask import url_for
from werkzeug.utils import secure_filename
import app,os

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

    def edit_post(self,request):
        img = request.files['image']
        if img:
            filename = secure_filename(img.filename)
            # img.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            img.save(os.path.join('./static/posts/images', filename))
            self.image=img.filename

        self.title=request.form['title']
        self.body=request.form['body']
        
        db.session.commit()

    @classmethod
    def get_all_posts(cls):
        return cls.query.all()
        
    @classmethod
    def create_post(cls,**kwargs):
        post = Post(title=kwargs['title'], body=kwargs['body'],image=kwargs['image'])
        db.session.add(post)
        db.session.commit()
        
    @classmethod
    def delete_post(cls,id):
        post = Post.query.get_or_404(id)
        db.session.delete(post)
        db.session.commit()
    


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    posts = db.relationship('Post', backref='category', lazy=True)

    @property
    def get_show_url(self):
        return  url_for('category.show', id=self.id)
    
    @classmethod
    def get_posts(cls,id):
        category = Category.query.get_or_404(id)
        return category.posts

    def __str__(self):
        return self.name
