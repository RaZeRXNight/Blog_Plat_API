from flask import Blueprint

blog_blueprint = Blueprint("blog", __name__)

# Return a json containing a list of all posts.
@blog_blueprint.get("/posts")
def list_posts():
    pass

@blog_blueprint.route("/posts/<post_id>")
def post_operations(post):
    # Check for ID Validity 
    pass