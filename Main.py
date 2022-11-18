from instances.Colors import Colors
from instances.Item import *
from instances.Monster import *
from instances.Player import Player
from tools.devtools import *
from tools.spritetools import *

import pygame
import sys
import os
import time

from math import floor

width = 1280
height = 720

pygame.init()
pygame.display.set_caption("Nungeon")
pygame.font.init()

try:
    screen = pygame.display.set_mode((width, height),vsync=1,flags=pygame.SCALED|pygame.NOFRAME)
except Exception as e:
    print(e)
finally:
    screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()


class Game:
    def __init__(self):
        self.colors = Colors()
        self.player = None
        
        self.fps_cap = 400
        self.run = False
        self.frame_count = 0
        self.dt_frame = 0

        self.sprites = SpriteGroup()
        self.sprites.player = Sprite("sprites/player_sepia.png",32,32)
        self.sprites.background = Sprite("sprites/background.png",1280,702)
        self.sprites.light = Sprite("sprites/light.png",64,64,75,image_speed=6)
        
        self.sprites.background.count_per_line = floor(width / self.sprites.background.image_w) + 2
        self.sprites.background.count_per_column = floor(height / self.sprites.background.image_h) + 2

        self.my_font = pygame.font.SysFont('Comic Sans MS', 10)
        
        self.debug=Debug()
        self.disp_list=[]

    def ask_player_name(self) -> int:
        if self.player is not None:
            print("Un joueur est déjà créé.")
            return 1

        player_name = "zub"#input("Veuillez renseigner le pseudonyme du joueur : ")

        self.player = Player(player_name, (0, 0), self.sprites.player, screen)
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
        if key[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit(0)

        pygame.display.flip()

        keys = (x_move, y_move)

        self.player.update(self.dt, keys)

    def draw(self):
        
        max_decal_x = self.player.coord[0] % self.sprites.background.image_w
        max_decal_y = self.player.coord[1] % self.sprites.background.image_h

        self.disp_list=[]
        
        for i in range(self.sprites.background.count_per_line):
            for j in range(self.sprites.background.count_per_column):
                self.disp_list.append((self.sprites.background.images[0], [(i * self.sprites.background.image_w) - max_decal_x, (j * self.sprites.background.image_h) - max_decal_y]))
                

        self.disp_list.append(self.sprites.light.get_blitable(width/2,height/2,self.dt_frame))
        self.disp_list.append(self.player.draw())

        self.disp_list+=self.debug.draw()
        screen.fill((0, 0, 0))
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
            self.frame_count +=1
            self.dt_frame += self.dt

        return 0


game = Game()
game.start_game()
