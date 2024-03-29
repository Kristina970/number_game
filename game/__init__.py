from flask import Blueprint
from flask_restful import Api
from .routes import GameResources, PlayGame


game = Blueprint('game', __name__)
game_api = Api(game)

game_api.add_resource(GameResources, '/games')
game_api.add_resource(PlayGame, '/play/<int:game_id>')



