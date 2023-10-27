from flask_restful import reqparse

post_parser = reqparse.RequestParser()

post_parser.add_argument('title',type=str,required=True, help='A title is required')
post_parser.add_argument('body', type=str, required=True, help='A body is required')
post_parser.add_argument('category_id', type=int, required=True, help='Choose category from 1 to 10', location='json')
post_parser.add_argument('image', type=str, help='A body is required')
