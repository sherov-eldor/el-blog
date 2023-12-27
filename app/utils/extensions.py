from re import sub
import flask_admin as admin
from flask import redirect, request, url_for
from flask_admin import helpers,  expose
import flask_login as login
from flask_admin.contrib.sqla import ModelView

from app.templates.form.login import LoginForm

def title_to_slug(string):
    return sub(r"[-]+", "-", sub(r"[^a-z0-9|-]", "", string.lower().replace(" ", "-")))

    
class UserModelView(ModelView):

    def is_accessible(self):
        return login.current_user.is_authenticated