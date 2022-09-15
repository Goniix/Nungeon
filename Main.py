class Game:
    def __init__(self):
        self.run = True

    def update(self):
        # run updates of all instances (no draw)
        pass


class Draw:
    def __init__(self):
        pass

    def update(self):
        # update display
        pass


class Dict:
    def __init__(self):
        pass

# game instances
class Player:
    def __init__(self):
        self.baseHealth=500
        self.Health=self.baseHealth
        self.coord=[0,0]
    pass


class Item:
    pass


class Monster:
    pass


game = Game()
display = Draw()
while game.run:
    game.update()
    display.update()
