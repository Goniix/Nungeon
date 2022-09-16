from instances.Item import Item
from instances.Colors import Colors
from instances.Item import *
from instances.Monster import *
from instances.Player import Player

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
        pass


    def start_game(self) -> int:
        self.ask_player_name()

        self.run = True

        while self.run:
            self.update()

        return 0
        
game = Game()
game.start_game()
