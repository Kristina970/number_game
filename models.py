# import random
#
# from db import db
#
#
# game_players = db.Table(
#     'game_players',
#     db.Column('user_id', db.Integer, db.ForeignKey('game_user.id')),
#     db.Column('game_id', db.Integer, db.ForeignKey('game_table.id'))
# )
#
#
# class Game(db.Model):
#     __tablename__ = 'game_table'
#
#     id = db.Column(db.Integer, primary_key=True)
#     secret_number = db.Column(db.Integer, default=random.randint(0, 1))
#     attempts = db.Column(db.Integer)
#     status = db.Column(db.String, default='active')
#     author_id = db.Column(db.Integer, db.ForeignKey('game_user.id'))
#     players = db.relationship('game_user', secondary=game_players, backref=db.backref('players'))
#     range_from = db.Column(db.Integer)
#     range_to = db.Column(db.Integer)
#     winner_id = db.Column(db.Integer, db.ForeignKey('game_user.id'))
#     password = db.Column(db.String)
#
#     def __init__(self, secret_number, attempts, author_id,
#                  password=None,
#                  range_from=None, range_to=None):
#         self.secret_number = secret_number
#         self.attempts = attempts
#         self.author_id = author_id
#
#     def __repr__(self):
#         return f"Game({'self.secret_number'}, {'self.guessed'}, {'self.attempts'})"
#
#
# class GameUsers(db.Model):
#     __tablename__ = 'game_user'
#
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     name = db.Column(db.String(80), unique=True, nullable=True)
#     password = db.Column(db.String(80))
#     role = db.Column(db.String(80))
#
#     def __init__(self, name, password, role):
#         self.name = name
#         self.password = password
#         self.role = role
#
#
# class Statistics(db.Model):
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     game_id = db.Column(db.Integer, db.ForeignKey('game_table.id'))
#     player_id = db.Column(db.Integer, db.ForeignKey('game_user.id'))
#     attempts_number = db.Column(db.Integer,)
#
#     def __init__(self, game_id, player_id, attempts_number):
#         self.game_id = game_id
#         self.player_id = player_id
#         self.attempts_number = attempts_number
#
#
#

import random

from db import db

game_players = db.Table(
    'game_players',
    db.Column('user_id', db.Integer, db.ForeignKey('game_user.id')),
    db.Column('game_id', db.Integer, db.ForeignKey('game.id'))
)


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    secret_number = db.Column(db.Integer, default=random.randint(0, 10))
    attempt = db.Column(db.Integer)
    status = db.Column(db.String, default='active')
    author_id = db.Column(db.Integer, db.ForeignKey('game_user.id'))
    players = db.relationship('GameUsers', secondary=game_players, backref=db.backref('players'))
    range_from = db.Column(db.Integer)
    range_to = db.Column(db.Integer)
    winner_id = db.Column(db.Integer, db.ForeignKey('game_user.id'))
    password = db.Column(db.String)

    # def __init__(self, secret_number=None, attempt=None, status=None, author_id=None, range_from=None, range_to=None,
    #              password=None):
    def __init__(self, secret_number, attempt, status, author_id, range_from, range_to,
                 password):
        self.secret_number = secret_number
        self.attempt = attempt
        self.status = status
        self.author_id = author_id
        self.range_from = range_from
        self.range_to = range_to
        self.password = password


class Statistics(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    player_id = db.Column(db.Integer, db.ForeignKey('game_user.id'))
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'))
    numb_of_tries = db.Column(db.Integer)


class GameUsers(db.Model):

    __tablename__ = 'game_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String)
    role = db.Column(db.String)