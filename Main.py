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


# game instances
class Player:
    def __init__(self):
        self.baseHealth = 500
        self.Health = self.baseHealth
        self.coord = [0, 0]
        self.inv = []

    def move_player(self, x_direction, y_direction):
        pass


class Item:
    def __init__(self, x, y, itemBase):
        self.coord = [x, y]
        self.stepMethod = itemBase.method
        self.description = itemBase.description
        self.type = itemBase.type

    def execute_item(self):
        self.stepMethod()


class Monster:
    pass


game = Game()
display = Draw()
while game.run:
    game.update()
    display.update()
