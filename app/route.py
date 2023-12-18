from flask import render_template
from app import app
from app.model import Post
from app.utils.extensions import title_to_slug

@app.route('/')
@app.route('/home')
def home():
    posts = Post.query.with_entities(Post.title, Post.post_text).all()
    all_posts = []
    for post in posts:
        post_obj = {
            'title' : post.title,
            'post_text' : post.post_text,
            'slug' : title_to_slug(post.title)
        }
        all_posts.append(post_obj)
    return render_template('home.html', posts=all_posts)

@app.route('/<category>/<post_title>')
def post(category, post_title):
    post = Post.get_post_with_slug(slug=post_title)
    print(post_title)
    print(post)
    return render_template('post.html')






