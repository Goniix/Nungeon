from .instances.Item import Item

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


game = Game()
display = Draw()
while game.run:
    game.update()
    display.update()
