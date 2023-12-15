from app import db

# class User(db.Model):
    
#     __tablename__ = "users"
    
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True)
#     password = db.Column(db.String, nullable=False)

#     def __init__(self, username, email):
#         self.username = username
#         self.email = email

#     def __repr__(self):
#         return '<User %r>' % self.username
    
class Language(db.Model):
    
    __tablename__ = "languages"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Language %r>' % self.name
    
    
class Tags(db.Model):
    
    __tablename__ = "tag"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Tags %r>' % self.name
    
class Post(db.Model):
    
    __tablename__ = "posts"
    