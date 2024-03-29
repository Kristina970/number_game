from flask_restful import reqparse

game_parse = reqparse.RequestParser()
game_parse.add_argument('secret_number')
game_parse.add_argument('attempts')
game_parse.add_argument('range_from')
game_parse.add_argument('range_to')
game_parse.add_argument('password', required=False)
