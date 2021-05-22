import pygame

from player import Player
from grid import grid
import player_img


class Window:
    def __init__(self, win_width=800, win_height=600):
        # Размеры ркна
        self.win_width = win_width
        self.win_height = win_height
        # Название окна
        pygame.display.set_caption("Прятки")
        # Создание окна
        self.win = pygame.display.set_mode((win_width, win_height))
        # Счетчик кадров
        self.animCount = 0


def draw_window(curr_window: Window, curr_player: Player):
    # заливка фона
    curr_window.win.fill((255, 153, 51))

    # прорисовка лабиринта по сетке grid
    for i in range(20):
        for j in range(15):
            if not grid[j][i]:
                pygame.draw.rect(curr_window.win, (100, 100, 100), (i * 40, j * 40, 40, 40))

    if curr_window.animCount + 1 >= 30:
        # проверка синхронизации анимаций с кадрами
        curr_window.animCount = 0

    # поворот модельки игрока
    if curr_player.pos_left:
        curr_window.win.blit(player_img.walkLeft[curr_window.animCount // 5], (curr_player.x, curr_player.y))
        curr_window.animCount += 1
    elif curr_player.pos_right:
        curr_window.win.blit(player_img.walkRight[curr_window.animCount // 5], (curr_player.x, curr_player.y))
        curr_window.animCount += 1
    else:
        curr_window.win.blit(player_img.playerStand, (curr_player.x, curr_player.y))

    # смена кадра
    pygame.display.update()
