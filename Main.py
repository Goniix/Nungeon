from instances.Item import Item
from instances.Colors import Colors
from instances.Item import *
from instances.Monster import *
from instances.Player import Player

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

        self.run = False

        self.background = pygame.image.load(os.path.join("sprites/background_tile.png"))
        self.background.convert()

        self.sprites = [pygame.image.load(os.path.join("sprites/player.png")).convert()]
        self.my_font = pygame.font.SysFont('Comic Sans MS', 10)

    def ask_player_name(self) -> int:
        if self.player is not None:
            print("Un joueur est déjà créé.")
            return 1

        player_name = "zub"#input("Veuillez renseigner le pseudonyme du joueur : ")

        self.player = Player(player_name, (0, 0), self.sprites[0], screen)

        return 0

    def update(self):
        # run updates of all instances (no draw)
        self.dt = clock.tick(60) / (1/60*1000)

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
        count_per_line = floor(width / 64) + 2
        count_per_column = floor(height / 64) + 2

        max_decal_x = floor(self.player.coord[0] % 64)
        max_decal_y = floor(self.player.coord[1] % 64)

        dt_surface= self.my_font.render("dt: "+str(self.dt), False, (255,255,255))
        fps_surface= self.my_font.render("fps: "+str(clock.get_fps()), False, (255,255,255))
        temp=[]
        for i in range(count_per_line):
            for j in range(count_per_column):
                temp.append((self.background, [(i * 64) - max_decal_x, (j * 64) - max_decal_y]))

        temp.append((fps_surface,(0,0)))
        temp.append((dt_surface,(0,16)))
        screen.blits(temp)

        self.player.draw()

    def start_game(self) -> int:
        self.ask_player_name()

        self.run = True

        while self.run:
            self.update()
            self.draw()

        return 0


game = Game()
game.start_game()
