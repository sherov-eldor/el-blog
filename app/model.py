from datetime import datetime
from app import db
from app.utils.extensions import title_to_slug
from flask_login import UserMixin
    
class Category(db.Model):
    
    __tablename__ = "categories"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    slug = db.Column(db.String(120), unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name
    
    
class Post(db.Model):
    
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True)
    slug = db.Column(db.String(255), unique=True)
    post_img_uri = db.Column(db.String(255))
    # lenta_img = db.Column(db.LargeBinary, nullable = False)
    post_text = db.Column(db.String(255))
    body = db.Column(db.Text)
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    category = db.relationship(Category, backref=db.backref('posts', uselist=True, lazy='select', cascade='delete-orphan,all'))
    
    @classmethod
    def get_post_with_slug(cls, slug):
        return cls.query.filter_by(slug = slug).first()
        
    
    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return '<Post %r>' % self.title


# Create user model.
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(64))

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    # Required for administrative interface
    def __unicode__(self):
        return self.username