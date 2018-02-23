from flask import Flask
from flask_login import AnonymousUserMixin, LoginManager
from flask_sqlalchemy import SQLAlchemy

from .utils.import_all import import_all


class Pynome(Flask):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config.from_object(__name__)
        self.config.from_envvar('FLASK_CONFIG', silent=False)


class Anon(AnonymousUserMixin):
    @property
    def peson(self):
        pass


app = Pynome(__name__)
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.anonymous_user = Anon

import_all('lib.routes')
