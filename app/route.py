from flask import redirect, render_template, current_app, send_from_directory, request, url_for
from app import app
from app.model import Post, Category,User
from app.templates.form.login import LoginForm    
from flask_login import current_user, login_required, login_user, logout_user

# HOME PAGE
# GET ALL CATEGORIES AND POSTS
@app.route('/')
@app.route('/home')
def home():
    categories = Category.query.all()
    posts = Post.query.join(Category, Post.category_id == Category.id).with_entities(Post.title, Post.post_img_uri, Post.category_id, Post.post_text, Post.created_date, Post.slug).all()
    posts.reverse()
    return render_template('home.html', categories=categories, posts=posts)


# GET POST BY POST SLUG
@app.route('/post/<post_slug>')
def post(post_slug):
    post = Post.get_post_with_slug(slug=post_slug)
    return render_template('post.html', post=post)

# GET ALL POST BY CATEGORY SLUG
@app.route('/category/<category_slug>')
def get_category_posts(category_slug):
    category = Category.query.filter_by(slug = category_slug).first()
    category_obj = {
        'name' : category.name,
        'slug' : category.slug
    }
    return render_template('home.html', posts = category.posts, category= category_obj)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for('admin.index'))
        
    if form.validate_on_submit():
        user = User.query.filter_by(login=form.login.data, password=form.password.data).first()
        if user:
            login_user(user)
            return redirect(url_for('admin.index'))
            
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
    
    
# CUSTOM TIMPLATE FILTERS
@app.template_filter('category_slug')
def get_category_slug(id):
    return Category.query.filter_by(id = id).first().slug
    

@app.template_filter('category_name')
def get_category_name(id):
    return Category.query.filter_by(id = id).first().name


@app.template_filter('limited_str')
def limited_str(str):
    return f"{str[0:200]}..."

@app.template_filter('limited_title')
def limited_title(str):
    return f"{str[0:50]}..."

@app.route('/uploads/<file_name>')
def uploads(file_name):
    return send_from_directory('uploads/articles', file_name)