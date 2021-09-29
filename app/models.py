from app import db

games_played = db.Table ('enrolments',
    db.Column('student_id', db.Text, db.ForeignKey('student.id'), primary_key=True),
    db.Column('game_id', db.Integer, db.ForeignKey('game.id'), primary_key=True)
)

class Student(db.Model):
    id = db.Column(db.Text, primary_key=True)
    name = db.Column(db.Text)
    FormGroup = db.Column(db.Text)
    YearLevel = db.Column(db.Integer)
    Score = db.Column(db.Integer)

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    resources = db.Column(db.Text)
    description = db.Column(db.Text)

    def __repr__(self):
        return f'Game: {self.name}    Description: {self.description}'