from flask import Blueprint, render_template, request

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    data = [
        ("01-01-2020", 15632),
        ("02/01/2020", 2545),
        ("03-01-2020", 456),
        ("04-01-2020", 15465),
        ("05-01-2020", 6546),
        ("06-01-2020", 45645),
        ("07-01-2020", 546)
    ]
    labels = [row[0] for row in data]
    data = [row[1] for row in data]

    return render_template("home.html", labels=labels, data=data)
