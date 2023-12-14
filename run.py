from src import create_app
from src.utils.extensions import db

if __name__ == "__main__":
    app = create_app('dev')

    with app.app_context():
        db.create_all()
    app.run(host=app.config.get('HOST', '0.0.0.0'), port=app.config.get('PORT', 5000))