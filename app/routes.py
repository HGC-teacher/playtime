from flask import render_template

from app import app, db
from app.models import Game, Student

@app.route('/')
@app.route('/games')
def game_list():
    games = Game.query.all()
    return render_template('game_list.html', games = games)

@app.route('/games/<int:id>')
def game_details(id):
    game = Game.query.get_or_404(id)
    return render_template('game_details.html', game = game)

@app.route('/students')
def student_list():
    students = Student.query.all()
    return render_template('student_list.html', students = students)

@app.route('/students/<text:id>')
def student_details(id):
    student = Student.query.get_or_404(id)
    return render_template('student_details.html', student = student)