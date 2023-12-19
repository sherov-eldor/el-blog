from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from wtforms import  TextAreaField
from wtforms.widgets import TextArea
from app.utils.extensions import title_to_slug

app = Flask(__name__)
app.config['SECRET_KEY'] = '2ae0a61787937e86297484b3051424dc'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['FLASK_ADMIN_SWATCH'] = 'solar'
app.config['PORT'] = 5000

db = SQLAlchemy(app)
admin = Admin(app, name='el-blog', template_mode='bootstrap4')

from app.model import Category, Post
    
class CKTextAreaWidget(TextArea):
    def __call__(self, field, **kwargs):
        if kwargs.get('class'):
            kwargs['class'] += ' ckeditor'
        else:
            kwargs.setdefault('class', 'ckeditor')
        return super(CKTextAreaWidget, self).__call__(field, **kwargs)

class CKTextAreaField(TextAreaField):
    widget = CKTextAreaWidget()
    

class PostModelView(ModelView):
    column_list = ('title', 'body', 'category')
    form_excluded_columns = ('slug')
    extra_js = ['https://cdn.ckeditor.com/4.20.0/standard/ckeditor.js']
    form_overrides = {
        'body': CKTextAreaField
    }
    
    def on_model_change(self, form, model, is_created):
        model.title = form.data['title']
        # model.slug = sub(r"[-]+", "-", sub(r"[^a-z0-9|-]", "", model.title.lower().replace(" ", "-")))
        model.slug = title_to_slug(model.title)
        super(ModelView, self).on_model_change(form, model, is_created)



admin.add_view(ModelView(Category, db.session))
admin.add_view(PostModelView(Post, db.session))

with app.app_context():
    # db.drop_all()
    db.create_all()

from app import route
