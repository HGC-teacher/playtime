from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///playtime.db'

db = SQLAlchemy(app)

from app import routes, models

@app.cli.command('init-db')
def initialise_db():
    # Recreate the database for Playtime activities data
    db.drop_all()
    db.create_all()

    # Create an example with 4 Student records
    kylie = models.Student(id = 'KY001', name = 'Kylie', FormGroup = '8G', YearLevel = 8)
    bob = models.Student(id = 'BO001', name = 'Bob', FormGroup = '8G', YearLevel = 8)
    kyle = models.Student(id = 'KY002', name = 'Kyle', FormGroup = '8G', YearLevel = 8)

    db.session.add(kylie)
    db.session.add(bob)
    db.session.add(kyle)

    # Create 2 game records
    hangman = models.Game(name="Hangman", resources='Whiteboard', description='We all know hangman')
    highest_wins = models.Game(name='Highest wins', resources='Pens and paper', descritption='Invite student groups to add the numbers in their phone numbers, ages of family members, or street addresses. The group with the highest score wins.')
    db.session.add(hangman)
    db.session.add(highest_wins)

    # Set kylie to have played both games

    kylie.game.append(hangman)
    kylie.game.append(highest_wins)

    # Set kyle to have played 1 game
    kylie.game.append(hangman)

    db.session.commit()