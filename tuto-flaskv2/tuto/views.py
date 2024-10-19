from .app import app
from flask import render_template
from .models import get_sample
from flask_wtf import FlaskForm
from wtforms import StringField , HiddenField
from wtforms.validators import DataRequired
from flask import url_for , redirect
from .app import db
from .models import Author
from .models import *
from flask_wtf import FlaskForm


@app.route("/")
def home():
    return render_template(
        "booksBS.html", 
        title="My Books !",
        books=get_sample())


@app.route("/detail/<id>")
def detail(id):
    books = get_sample()
    book = books[int(id)-1]
    return render_template(
        "detail.html",
        book=book)

@app.route("/save/author/", methods =("POST",))
def save_author ():
    a = None
    f = AuthorForm ()
    if f.validate_on_submit():
        id = int(f.id.data)
        a = get_author(id)
        a.name = f.name.data
        db.session.commit ()
        return redirect ( url_for ('detail', id=a.id))
    a = get_author(int(f.id.data ))
    return render_template ("edit-author.htm",author =a, form=f)





class AuthorForm ( FlaskForm ):
    id = HiddenField ('id')
    name = StringField ('Nom', validators =[DataRequired()])
    @app.route("/edit/author/<int:id>")
    def edit_author (id):
        a = get_author(id)
        f = AuthorForm(id=a.id , name=a.name)
        return render_template ("edit-author.htm",author =a, form=f)
    

class ajoutAuthorForm ( FlaskForm ):
    id = StringField ('id')
    name = StringField ('Nom')
    @app.route("/ajout/author/")
    def ajout_author ():
        a = None
        f = ajoutAuthorForm ()
        return render_template ("ajout-author.html",author =a, form=f)
    




