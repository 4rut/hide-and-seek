import pygame
import requests
import json

from window import Window, draw_window
from player import Player
from grid import grid
from movement_logic import movement_logic
import player_img

res = requests.get('http://localhost:1234').content.decode("utf8")
data = json.loads(res)


window = Window(800, 600)

trump = Player(w=24, h=36, speed=5)

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

    draw_window(window, trump)

pygame.quit()
