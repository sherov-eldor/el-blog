from re import sub
import flask_admin as admin
from flask import redirect, request, url_for
from flask_admin import helpers,  expose
import flask_login as login
from flask_admin.contrib.sqla import ModelView

from flask_admin import AdminIndexView

def title_to_slug(string):
    return sub(r"[-]+", "-", sub(r"[^a-z0-9|-]", "", string.lower().replace(" ", "-")))

class MyIndexView(AdminIndexView):
    def is_accessible(self):
        return login.current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('login', next=request.url))
    
class UserModelView(ModelView):

    def is_accessible(self):
        return login.current_user.is_authenticated