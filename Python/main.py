import pygame

from window import Window, draw_window
from player import Player
from grid import grid
from movement_logic import movement_logic
import player_img

window = Window(800, 600)

trump = Player(speed=5)

# работа окна
run = True
while run:
    # настройка тикрейта
    pygame.time.Clock().tick(30)

    # проверка выхода
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # проверка передвижения игрока
    keys = pygame.key.get_pressed()

    movement_logic(window, trump, keys)

    draw_window(window, trump)

    # pygame.draw.rect(window.win, (0, 0, 0), (trump.x + (trump.w // 2), trump.y - trump.speed + trump.h, 20, 20))

pygame.quit()
