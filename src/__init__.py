from flask import Flask
from src.utils.extensions import register_extensions, register_blueprints


def create_app(config:str):
    app = Flask(__name__)

    if config in ['dev', 'prod', 'test']:
        app.config.from_object(f"src.utils.config.{config.capitalize()}Config")

    register_blueprints(app)
    register_extensions(app)

    return app