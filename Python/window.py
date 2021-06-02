import pygame
import json

from player import Player
from grid import grid
import player_img


class Window:
    def __init__(self, win_width=800, win_height=600):
        self.win_width = win_width
        self.win_height = win_height

        pygame.display.set_caption("Прятки")

        self.win = pygame.display.set_mode((win_width, win_height))

        self.animCount = 0


def draw_window(curr_window: Window, curr_player: Player, data: json):
    curr_window.win.fill((255, 153, 51))

    for i in range(20):
        for j in range(15):
            if not grid[j][i]:
                pygame.draw.rect(curr_window.win, (100, 100, 100), (i * 40, j * 40, 40, 40))

    if curr_window.animCount + 1 >= 30:
        curr_window.animCount = 0

    if curr_player.pos_left:
        curr_window.win.blit(player_img.walkLeft[curr_window.animCount // 5], (curr_player.x, curr_player.y))
        curr_window.animCount += 1
    elif curr_player.pos_right:
        curr_window.win.blit(player_img.walkRight[curr_window.animCount // 5], (curr_player.x, curr_player.y))
        curr_window.animCount += 1
    else:
        curr_window.win.blit(player_img.playerStand, (curr_player.x, curr_player.y))

    if data['number_of_players_now'] != 0:
        for (player, val) in data['players'].items():
            if val['player_name'] != curr_player.name:
                if val['player_is_left']:
                    curr_window.win.blit(player_img.walkLeft[curr_window.animCount // 5], (val['player_pos_x'], val['player_pos_y']))
                elif val['player_is_right']:
                    curr_window.win.blit(player_img.walkRight[curr_window.animCount // 5], (val['player_pos_x'], val['player_pos_y']))
                    curr_window.animCount += 1
                else:
                    curr_window.win.blit(player_img.playerStand, (val['player_pos_x'], val['player_pos_y']))

    if curr_player.is_dead:
        curr_player.x = curr_window.win_width - 40
        curr_player.y = 0
    else:
        curr_window.win.blit(player_img.overview, (curr_player.center_x - 800, curr_player.center_y - 600))

    pygame.display.update()
