import pygame

from window import Window
from player import Player
from grid import grid

import player_img

window = Window(800, 600)

trump = Player(speed=5)


# прорисовка окна
def draw_window():
    global window

    # заливка фона
    window.win.fill((255, 153, 51))

    # прорисовка лабиринта по сетке grid
    for i in range(20):
        for j in range(15):
            if not grid[j][i]:
                pygame.draw.rect(window.win, (100, 100, 100), (i * 40, j * 40, 40, 40))

    if window.animCount + 1 >= 30:
        # проверка синхронизации анимаций с кадрами
        window.animCount = 0

    # поворот модельки игрока
    if trump.pos_left:
        window.win.blit(player_img.walkLeft[window.animCount // 5], (trump.x, trump.y))
        window.animCount += 1
    elif trump.pos_right:
        window.win.blit(player_img.walkRight[window.animCount // 5], (trump.x, trump.y))
        window.animCount += 1
    else:
        window.win.blit(player_img.playerStand, (trump.x, trump.y))

    # смена кадра
    pygame.display.update()


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

    if keys[pygame.K_LEFT] and trump.x > trump.speed:
        grid_check_x = trump.x // 40
        grid_check_y_1 = trump.y // 40
        grid_check_y_2 = (trump.y + trump.h) // 40
        grid_check_y_3 = (trump.y + trump.h // 2) // 40

        if grid[grid_check_y_1][grid_check_x] and grid[grid_check_y_2][grid_check_x] and grid[grid_check_y_3][
            grid_check_x]:
            trump.x -= trump.speed
            trump.pos_left = True
            trump.pos_right = False

    elif keys[pygame.K_RIGHT] and trump.x < window.win_width - trump.speed - trump.w:
        grid_check_x = (trump.x + trump.w) // 40
        grid_check_y_1 = trump.y // 40
        grid_check_y_2 = (trump.y + trump.h) // 40
        grid_check_y_3 = (trump.y + trump.h // 2) // 40

        if grid[grid_check_y_1][grid_check_x] and grid[grid_check_y_2][grid_check_x] and grid[grid_check_y_3][
            grid_check_x]:
            trump.x += trump.speed
            trump.pos_left = False
            trump.pos_right = True
    else:
        trump.pos_left = False
        trump.pos_right = False
        window.animCount = 0

    if keys[pygame.K_UP] and trump.y > trump.speed:
        grid_check_x = (trump.x + trump.w // 2) // 40
        grid_check_y = trump.y // 40

        if grid[grid_check_y][grid_check_x]:
            trump.y -= trump.speed

    if keys[pygame.K_DOWN] and trump.y < window.win_height - trump.speed - trump.h:
        grid_check_x = (trump.x + trump.w // 2) // 40

        grid_check_y = (trump.y + trump.h) // 40

        if grid[grid_check_y][grid_check_x]:
            trump.y += trump.speed

    draw_window()
    pygame.draw.rect(window.win, (0, 0, 0), (trump.x + (trump.w // 2), trump.y - trump.speed + trump.h, 20, 20))

pygame.quit()
