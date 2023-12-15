from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_migrate import Migrate

db = SQLAlchemy()
admin = Admin()
migrate = Migrate()


def register_extensions(app):

    db.init_app(app)
    admin.init_app(app)
    migrate.init_app(app, db)


def register_blueprints(app):
    from src.routes import base, post
    
    app.register_blueprint(base.base_route)
    app.register_blueprint(post.post_route)
