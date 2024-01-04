#1. Implement a blueprint using Flask-Smorest.
#2. Create Marshmallow schema.
#3. Define schema structures that accurately represent the data models.
#4. Ensure the schemas can handle data validation for incoming and outgoing requests.
#5. Utilize the Marshmallow schemas to validate data coming into the API (request validation).
#6. Implement validation for data going out of the API to ensure consistency (response validation).
#7. Refactor your route implementations into Flask MethodView classes.
#8. Organize the classes in a logical and maintainable structure.
#9. Ensure each class corresponds to a specific resource and encapsulates related functionality.

from flask import request
from uuid import uuid4 
from flask.views import MethodView

from schemas import PostSchema
from db import posts, Users as users
from . import bp








@bp.route('/<post_id>')
class Post(MethodView):

  @bp.response(200, PostSchema)
  def get(self, post_id):
    try:
      return posts[post_id]
    except KeyError:
      return {'message': "Invalid Post"}, 400

  @bp.arguments(PostSchema)
  def put(self, post_data ,post_id):
    try:
      post = posts[post_id]
      if post_data['user_id'] == post['user_id']:
        post['body'] = post_data['body']
        return { 'message': 'Post Updated' }, 202
      return {'message': "Unauthorized"}, 401
    except:
      return {'message': "Invalid Post Id"}, 400

  def delete(self, post_id):
    try:
      del posts[post_id]
      return {"message": "Post Deleted"}, 202
    except:
      return {'message':"Invalid Post"}, 400

@bp.route('/')
class PostList(MethodView):

  @bp.response(200, PostSchema(many = True))
  def get(self):
    return  list(posts.values())
  
  @bp.arguments(PostSchema)
  def post(self, post_data):
    user_id = post_data['user_id']
    if user_id in users:
      posts[uuid4()] = post_data
      return { 'message': "Post Created" }, 201
    return { 'message': "Invalid User"}, 401