from datetime import datetime
from app import db
from app.utils.extensions import title_to_slug
    
class Category(db.Model):
    
    __tablename__ = "categories"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    slug = db.Column(db.String(120), unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Category %r>' % self.name
    
    
class Post(db.Model):
    
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True)
    slug = db.Column(db.String(255), unique=True)
    post_text = db.Column(db.String(255))
    body = db.Column(db.Text)
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    category = db.relationship(Category, backref=db.backref('posts', uselist=True, lazy='select', cascade='delete-orphan,all'))
    
    @classmethod
    def get_post_with_slug(cls, slug):
        print("slug : ", slug)
        
    
    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return '<Post %r>' % self.title