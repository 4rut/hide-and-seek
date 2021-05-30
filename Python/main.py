import pygame
import requests
import json
import threading

from http.server import BaseHTTPRequestHandler, HTTPServer

from server import MyServer

from player import Player
from movement_logic import movement_logic
import player_img

from window import Window, draw_window
from grid import grid


res = requests.get('http://localhost:1234').content.decode("utf8")
data = json.loads(res)


window = Window(800, 600)

trump = Player(w=24, h=36, speed=5)


def game_window(window: Window, trump: Player):
    # работа окна
    run = True
    while run:
        pygame.time.Clock().tick(30)

    #    res = requests.get('http://localhost:1234').content.decode("utf8")
    #    data = json.loads(res)
    #    print(data)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        movement_logic(window, trump, pygame.key.get_pressed())

        srv.send_data(srv, trump)

        draw_window(window, trump)

    pygame.quit()


if __name__ == '__main__':
    srv = MyServer

    webServer = HTTPServer(('localhost', 5001), srv)
    print("Server started http://%s:%s" % ('localhost', 5001))

    th_srv = threading.Thread(target=webServer.serve_forever)
    try:
        th_srv.start()
    except KeyboardInterrupt:
        pass

    game_window(window, trump)

    th_srv.join()
    webServer.server_close()
