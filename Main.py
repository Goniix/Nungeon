from instances.Item import Item
from instances.Colors import Colors
from instances.Item import *
from instances.Monster import *
from instances.Player import Player

import pygame
import sys


width = 1194
height = 834

pygame.init()
pygame.display.set_caption("Nungeon")

screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()


class Game:
    def __init__(self):
        self.colors = Colors()
        self.player = None

        self.run = False

        self.background = pygame.image.load(os.path.join("sprites/background_tile.png"))
        self.background.convert()


    def ask_player_name(self) -> int:
        if self.player is not None:
            print("Un joueur est déjà créé.")
            return 1

        player_name = input("Veuillez renseigner le pseudonyme du joueur : ")
        
        self.player = Player(player_name, (0, 0))

        return 0

    def update(self):
        # run updates of all instances (no draw)

        x_move = 0
        y_move = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

        key = pygame.key.get_pressed()
        y_move = key[pygame.K_s] - key[pygame.K_z]
        x_move = key[pygame.K_d] - key[pygame.K_q]

        pygame.display.flip()

        keys = (x_move, y_move)

        # self.player.update(keys)

        dt = clock.tick(144) / 144
        pass

    def draw(self) -> bool:
        count_per_line = floor(width / 64) + 2
        count_per_column = floor(height / 64) + 2

        for i in range(count_per_line):


    def start_game(self) -> int:
        self.ask_player_name()

        self.run = True

        while self.run:
            self.update()

        return 0


game = Game()
game.start_game()
