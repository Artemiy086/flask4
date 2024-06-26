from flask import render_template, Blueprint, redirect, url_for
from .forms import LoginForm


bp = Blueprint("users", __name__, url_prefix="")


@bp.route("/")
def index():
    return render_template("index.html", title="Главная")


@bp.route("/answer")
def answer():
    answer_d = {
        "name": "man",
        "last_name": "van",
        "education": "ниже среднего",
        "prof": "Строитель",
        "male": "Мужчина",
        "motivation": "Мечтал застрять на Марсе",
        "stay": "True"
    }
    return render_template("auto_answer.html", title="answer", answer=answer_d)


@bp.route("/auto_answer")
def answer_auto():
    answer_d = {
        "name": "man",
        "last_name": "van",
        "education": "ниже среднего",
        "prof": "Строитель",
        "male": "Мужчина",
        "motivation": "Мечтал застрять на Марсе",
        "stay": "True"
    }
    return render_template("auto_answer.html", title="answer", answer=answer_d)


@bp.route("/index/<title>")
def index_title(title):
    return render_template("index.html", title=title)


@bp.route("/training/<prof>")
def training(prof):
    h4 = "Инженерные тренажеры"
    scr = url_for('static', filename='img/nlo1.png')

    if prof.strip().lower() in ["строитель", "инженер"]:
        h4 = "Научные симуляторы"
        scr = url_for('static', filename='img/nlo2.png')

    return render_template("path.html", title="training", h4=h4, scr=scr)


@bp.route("/login")
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect("/")
    return render_template("login.html", form=form)
