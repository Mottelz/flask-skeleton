from flask import Flask, render_template
from model import db, Dummy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route('/')
def home():
    data = Dummy.query.all()
    return render_template('example.html', messages=data)