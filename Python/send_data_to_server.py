from flask import Flask, jsonify
import json
from player import Player


def server_start(player: Player):

    app = Flask(__name__)

    data = json.loads('{}')

    def send_data():
        global data
        data['player_pos_x'] = player.x
        data['player_pos_y'] = player.y
        data['player_name'] = 'Player'
        data['player_is_pos_left'] = player.pos_left
        data['player_is_pos_right'] = player.pos_right

    @app.route('/', methods=['GET'])
    def send_data_to_server():
        # return data.get_json()
        # data = json.loads('{"a": "v", "id": 123}')
        global data
        return jsonify(data)

    app.run(port=5001)
