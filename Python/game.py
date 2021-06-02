import pygame
import threading

from server import MyServer

import requests
import json

from window import Window, draw_window
from player import Player
from movement_logic import movement_logic


window = Window(800, 600)


def game_window(srv: MyServer, this_player: Player, number_of_player: int):
    run = True
    while run:
        pygame.time.Clock().tick(30)

        res = requests.get('http://localhost:1234').content.decode("utf8")
        data = json.loads(res)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        movement_logic(window, this_player, pygame.key.get_pressed())

        srv.send_data(srv, this_player, number_of_players=number_of_player)

        draw_window(window, this_player, data)


    pygame.quit()
