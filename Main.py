from instances.Item import Item
from instances.Colors import Colors
from instances.Item import *
from instances.Monster import *
from instances.Player import Player

import pygame


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

    
    def ask_player_name(self) -> int:
        if self.player is not None:
            print("Un joueur est déjà créé.")
            return 1

        player_name = input("Veuillez renseigner le pseudonyme du joueur : ")
        
        self.player = Player(player_name, (0, 0))

        return 0

    def update(self):
        # run updates of all instances (no draw)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
                break

        pygame.display.flip()

        dt = clock.tick(144) / 144
        print(dt)
        pass


    def start_game(self) -> int:
        self.ask_player_name()

        self.run = True

        while self.run:
            self.update()

        return 0
        
game = Game()
game.start_game()
