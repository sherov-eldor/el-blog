from flask import Blueprint
from src.views.post import post_controller

post_route = Blueprint("post_route", __name__, url_prefix='/post')

@post_route.route('/a')
def post():
    return post_controller()
