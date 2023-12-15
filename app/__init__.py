from flask import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '2ae0a61787937e86297484b3051424dc'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_ECHO'] = True
app.config['PORT'] = 5000

db = SQLAlchemy(app)

with app.app_context():
    # db.drop_all()
    db.create_all()

from app import route
