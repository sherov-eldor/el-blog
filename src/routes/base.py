from flask import Blueprint
from src.views.base import base_controller

base_route = Blueprint('base_route', __name__)

@base_route.route('/')
def index():
    return base_controller()
