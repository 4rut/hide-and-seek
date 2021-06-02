import pygame
import requests
import json
import threading

import game
from http.server import BaseHTTPRequestHandler, HTTPServer

from server import MyServer

from player import Player
from movement_logic import movement_logic
import player_img

from window import Window, draw_window
from grid import grid


if __name__ == '__main__':

    res = requests.get('http://localhost:1234').content.decode("utf8")
    data = json.loads(res)

    srv = MyServer
    PORT = data['number_of_players_now'] + 1234 + 1

    srv.send_data(srv, number_of_players=1, number_of_players_now=data['number_of_players_now'] + 1)

    webServer = HTTPServer(('localhost', PORT), srv)

    print("Server started http://%s:%s" % ('localhost', PORT))

    th_srv = threading.Thread(target=webServer.serve_forever)
    try:
        th_srv.start()
    except KeyboardInterrupt:
        pass

    this_player = Player()
    number_of_player = 1

    game.game_window(srv, this_player, number_of_player)

    th_srv.join()

    webServer.server_close()
