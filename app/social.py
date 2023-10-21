from app import  create_app
from flask import render_template

app = create_app('prd')

@app.route('/about', endpoint='about')
def about(): 
    return render_template('posts/about.html')

@app.route('/contact', endpoint='contact')
def contact(): 
    return render_template('posts/contact.html')


if __name__=='__main__':
    
    app.run()

