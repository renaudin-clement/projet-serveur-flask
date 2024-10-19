from flask import Flask
from flask_bootstrap import Bootstrap
import os.path
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
bootstrap = Bootstrap(app)




def mkpath (p):
    return os.path. normpath (os.path.join(
    os.path. dirname ( __file__ ),p))


app.config['SQLALCHEMY_DATABASE_URI'] = ('sqlite:///'+mkpath('../tuto.db'))
app.config['SECRET_KEY'] = "dde130c7-f86c-4035-b779-0395e501b271"
db = SQLAlchemy(app)
