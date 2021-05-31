from http.server import BaseHTTPRequestHandler, HTTPServer
import json

from player import Player


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(json.dumps(self.data), "utf-8"))

    def send_data(self, player=Player(), number_of_players=2, number_of_players_now=1):
        self.data = json.loads('{}')

        self.data['player_name'] = player.name

        self.data['player_pos_x'] = player.x
        self.data['player_pos_y'] = player.y

        self.data['player_is_left'] = player.pos_left
        self.data['player_is_right'] = player.pos_right

        self.data['number_of_players'] = number_of_players
        self.data['number_of_players_now'] = number_of_players_now

