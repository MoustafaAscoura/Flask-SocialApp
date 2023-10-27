import os

from app.posts import posts_blueprint,category_blueprint
from flask import  request,render_template,redirect,url_for
from app.models import Post,Category
from werkzeug.utils import secure_filename

@posts_blueprint.route('', endpoint='index')
def index():
    allposts = Post.get_all_posts()
    return render_template('posts/index.html',posts=allposts)

@posts_blueprint.route('/details/<int:id>', endpoint='show')
def details(id): 
    post = Post.query.get_or_404(id)
    return render_template('posts/details.html',post=post)

@posts_blueprint.route('/delete/<int:id>', methods=['DELETE'], endpoint='delete')
def delete(id):
    Post.delete_post(id)
    return redirect(url_for('posts.index')) 

@posts_blueprint.route('/create', methods=['GET','POST'], endpoint='create')
def create():
    if request.method == 'GET':
        return render_template('posts/form.html',mode='create',post={})
    
    img = request.files['image']
    if img:
        filename = secure_filename(img.filename)
        img.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    Post.create_post(title=request.form['title'],body=request.form['body'],image=img)
    return redirect(url_for('posts.index'))

@posts_blueprint.route('/edit/<int:id>', methods=['GET','PUT'], endpoint='edit')
def edit(id): 
    post = Post.query.get_or_404(id)

    if request.method == 'GET':
        return render_template('posts/form.html',mode='edit',post=post)
    
    img = request.files['image']
    if img:
        filename = secure_filename(img.filename)
        # img.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        img.save(os.path.join('./static/posts/images', filename))
        image=img.filename
    else:
        image = "annon.png"
    
    title=request.form['title']
    body=request.form['body']

    post.edit_post(title=title,body=body,image=image)
    return redirect(url_for('posts.index'))
    
@category_blueprint.route('/<int:id>', endpoint='show')
def show_category(id):
    category = Category.query.get_or_404(id)
    return render_template('posts/index.html',category=category)