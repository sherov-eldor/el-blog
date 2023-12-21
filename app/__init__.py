from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin, form
from flask_admin.contrib.sqla import ModelView
from markupsafe import Markup
from wtforms import  TextAreaField, MultipleFileField
from wtforms.widgets import TextArea
from app.utils.extensions import title_to_slug
import os, ast
import os.path as op
# from fields import MultipleImageUploadField
from secrets import token_hex


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
    
def prefix_name(obj, file_data):
    _, ext = op.splitext(file_data.filename)
    return token_hex(10) + ext

file_path = 'app/uploads'

# function to delete image and thumbnail when deleting image in edit section
@db.event.listens_for(db.Model, 'after_delete') # change product with db.Model in which you are saving file names
def del_image(mapper, connection, target):
    if target.images:
        # Delete image
        try:
            print(file_path, target.images)
            os.remove(op.join(file_path, target.images))
        except OSError:
            pass

        # Delete thumbnail
        try:
            os.remove(op.join(file_path,
                              form.thumbgen_filename(target.images)))
        except OSError:
            pass

class PostModelView(ModelView):
    column_list = ('title', 'body', 'category')
    form_excluded_columns = ('slug')
    extra_js = ['https://cdn.ckeditor.com/4.20.0/standard/ckeditor.js']
    form_overrides = {
        'body': CKTextAreaField
    }
    
    def _list_thumbnail(view, context, model, name):

        if not model.images:
            return ''

        def gen_img(filename):
            return '<img src="{}">'.format(url_for('static', 
                   filename="app/uploads/" + form.thumbgen_filename(filename)))

        return Markup("<br />".join([gen_img(image) for image in ast.literal_eval(model.images)]))
    

    column_formatters = {'post_img_uri': _list_thumbnail} # My column name is images in this case
    
    form_extra_fields = {
        'post_img_uri': form.ImageUploadField(label='Upload post image in lenta', base_path='app/uploads/articles')
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
