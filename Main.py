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
        self.coord = [0, 0]
        self.inv = []
        self.base_health = 500
        self.health = self.base_health
        self.base_speed = 5
        self.speed = self.base_speed

    def move_player(self, x_direction, y_direction):
        pass


class Item:
    def __init__(self, x, y, item_base):
        self.coord = [x, y]
        self.collide_method = item_base.collide_method
        self.step_method = item_base.step_method
        self.description = item_base.description
        self.type = item_base.type

    def collide(self):
        self.collide_method()

    def execute_item(self):
        self.step_method()


class Monster:
    def __init__(self, x, y, monster_base):
        self.coord = [x, y]
        self.step_method = monster_base.method
        self.description = monster_base.description
        self.type = monster_base.type
        self.base_health = monster_base.baseHealth
        self.health = self.base_health
        self.base_speed = monster_base.baseSpeed
        self.speed = self.base_speed


game = Game()
display = Draw()
while game.run:
    game.update()
    display.update()
