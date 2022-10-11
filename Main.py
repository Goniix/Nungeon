from instances.Item import Item
from instances.Colors import Colors
from instances.Item import *
from instances.Monster import *
from instances.Player import Player
import tools.devtools as dtools
import tools.spritetools as stools

import pygame
import sys
import os

from math import floor

width = 1194
height = 834

pygame.init()
pygame.display.set_caption("Nungeon")
pygame.font.init()


screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()


class Game:
    def __init__(self):
        self.colors = Colors()
        self.player = None
        
        self.fps_cap = 160
        self.run = False

        self.sprites = stools.SpriteGroup()
        self.sprites.player = stools.Sprite("sprites/player.png",32,32)
        self.sprites.background = stools.Sprite("sprites/background_tile.png",512,512)

        self.my_font = pygame.font.SysFont('Comic Sans MS', 10)

        self.debug=dtools.Debug()
        self.disp_list=[]

    def ask_player_name(self) -> int:
        if self.player is not None:
            print("Un joueur est déjà créé.")
            return 1

        player_name = "zub"#input("Veuillez renseigner le pseudonyme du joueur : ")

        self.player = Player(player_name, (0, 0), self.sprites.player.images[0], screen)
        return 0

    def update(self):
        # run updates of all instances (no draw)
        self.dt = clock.tick(self.fps_cap) / (1/60*1000)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

        key = pygame.key.get_pressed()
        y_move = key[pygame.K_s] - key[pygame.K_z]
        x_move = key[pygame.K_d] - key[pygame.K_q]

        pygame.display.flip()

        keys = (x_move, y_move)

        self.player.update(self.dt, keys)

    def draw(self):
        screen.fill((0, 0, 0))
        
        count_per_line = floor(width / self.sprites.background.w) + 2
        count_per_column = floor(height / self.sprites.background.h) + 2

        max_decal_x = floor(self.player.coord[0] % self.sprites.background.w)
        max_decal_y = floor(self.player.coord[1] % self.sprites.background.h)

        self.disp_list=[]
        
        for i in range(count_per_line):
            for j in range(count_per_column):
                self.disp_list.append((self.sprites.background.images[0], [(i * 512) - max_decal_x, (j * 512) - max_decal_y]))
                
        
        self.disp_list+=self.debug.draw()
        self.disp_list.append(self.player.draw())
        screen.blits(self.disp_list)

        

    def start_game(self) -> int:
        self.ask_player_name()

        self.debug.add_watcher("fps",lambda : clock.get_fps())
        self.debug.add_watcher("dt",lambda : game.dt)
        self.debug.add_watcher("blit_t",lambda : len(game.disp_list))

        self.run = True

        while self.run:
            self.update()
            self.draw()

        return 0


game = Game()
game.start_game()
