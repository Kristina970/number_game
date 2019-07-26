from flask_restful import fields


game_structure = {
    "secret_number": fields.Integer,
    "attempts": fields.Integer,
    "range_from": fields.Integer,
    "range_to": fields.Integer,
    "password": fields.String,
    "players": fields.String,
    "author_id": fields.Integer

}