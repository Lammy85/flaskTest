from flask import Flask, render_template, request, redirect, url_for, jsonify
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

        choice1 = request.form.getlist('salatoption')

        salatchoice = ', '.join(choice1) if choice1 else 'Keine Auswahl'

        choice2 = request.form.getlist('sauceoption')

        saucechoice = ', '.join(choice2) if choice2 else 'Keine Auswahl'

        new_burger = Burger(
            broetchen = request.form['broetchen'],
            patty = request.form['patty'],
            salat = salatchoice,
            kaese = request.form['kaese'],
            sauce = saucechoice
        )
        db.session.add(new_burger)
        db.session.commit()

        return redirect('/')
    
    return render_template('index.html')

@app.route('/tabelle')
def tabelle():
        daten = Burger.query.all()
        return render_template('burgerlist.html', daten=daten)

@app.route('/delete/<int:burger_id>', methods=['DELETE'])
def delete_burger(burger_id):
    burger = Burger.query.get(burger_id)
    if burger:
        db.session.delete(burger)
        db.session.commit()
        return jsonify({'success': True}), 200
    return jsonify({'error': 'Datensatz nicht gefunden'}), 404

if __name__ == "__main__":
    app.run()