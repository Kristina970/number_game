from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    secret_number = db.Column(db.Integer) #придумане число
    guessed = db.Column(db.Boolean)  #відгадане число
    attempts = db.Column(db.Integer)

    def __init__(self, secret_number, guessed, attempts):
        self.secret_number = secret_number
        self.guessed = guessed
        self.attempts = attempts

