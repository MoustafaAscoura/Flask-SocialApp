from flask_restful import Resource, fields, marshal_with
from flask import abort
from app.models import Post
from app.posts.parsers import post_parser

category_serializer = {
    'name':fields.String
}

posts_serializer = {
    'id':fields.Integer,
    'title':fields.String,
    'image':fields.String,
    'body':fields.String,
    'Category_id':fields.Integer,
    'category':fields.Nested(category_serializer),
    'created_on':fields.DateTime
}


class PostsView(Resource):
    @marshal_with(posts_serializer)
    def get(self):
        return Post.query.all()
    
    def put(self):
        args = post_parser.parse_args()
        try:
            Post.create_post(**args)
            return  200
        except:
            abort(400)

class PostView(Resource):
    @marshal_with(posts_serializer)
    def get(self,id):
        try:
            post=Post.query.get_or_404(id)
            return post, 200
        except:
            abort(404, 'Post not found')
    
    def delete(self,id):
        try:
            post=Post.delete_post(id)
            return 204
        except:
            abort(404, 'Post not found')

    @marshal_with(posts_serializer)
    def put(self, id):
        post = Post.query.get_or_404(id)
        args = post_parser.parse_args()
        post.edit_post(**args)

        return  post, 204
