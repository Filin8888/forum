# admin.py
from flask_admin import Admin, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from flask import redirect, url_for
from models import User, Post
from extentios import db

class MyAdminIndexView(AdminIndexView):
    @expose('/')
    def index(self):
        return redirect(url_for('main.index'))
    



admin = Admin(name="Forum Admin", template_mode="bootstrap4", index_view=MyAdminIndexView())

def init_admin(app):
    admin.init_app(app)

    # додаємо моделі
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Post, db.session))

