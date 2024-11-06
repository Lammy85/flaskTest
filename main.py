from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Burger(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    broetchen = db.Column(db.String(200), nullable=True)
    patty = db.Column(db.String(200), nullable=True)
    salat = db.Column(db.String(200), nullable=True)
    kaese = db.Column(db.String(200), nullable=True)
    sauce = db.Column(db.String(200), nullable=True)

@app.route('/', methods=['GET', 'POST'])
def start_page():
    if request.method == 'POST':
        new_burger = Burger(
            broetchen = request.form[''],
            patty = request.form[''],
            salat = request.form[''],
            kaese = request.form[''],
            sauce = request.form['']
        )
        db.session.add(new_burger)
        db.session.commit()
    
    return "Hello, World!"

if __name__ == "__main__":
    app.run()