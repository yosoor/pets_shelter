from flask import Flask, render_template, request, redirect, url_for
from models import db_session, Pet, init_db
from config import Config

app = Flask(__name__)

# Инициализация БД
@app.before_request
def before_request():
    init_db()

@app.route('/')
def index():
    pets = db_session.query(Pet).all()
    return render_template('index.html', pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    if request.method == 'POST':
        name = request.form['name']
        species = request.form['species']
        age = request.form['age']
        new_pet = Pet(name=name, species=species, age=age)
        db_session.add(new_pet)
        db_session.commit()
        return redirect(url_for('index'))
    return render_template('add_pet.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_pet(id):
    pet = db_session.query(Pet).get(id)
    if not pet:
        return "Животное не найдено", 404

    if request.method == 'POST':
        pet.name = request.form['name']
        pet.species = request.form['species']
        pet.age = request.form['age']
        db_session.commit()
        return redirect(url_for('index'))
    return render_template('edit_pet.html', pet=pet)

@app.route('/delete/<int:id>')
def delete_pet(id):
    pet = db_session.query(Pet).get(id)
    if not pet:
        return "Животное не найдено", 404

    db_session.delete(pet)
    db_session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)