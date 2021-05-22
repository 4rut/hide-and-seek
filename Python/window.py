import pygame
from grid import grid


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
