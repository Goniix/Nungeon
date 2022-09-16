class Player:
    def __init__(self,name):
        self.coord = [0, 0]
        self.inv = []
        self.base_health = 500
        self.health = self.base_health
        self.base_speed = 5
        self.speed = self.base_speed
        self.name = name

    def move_player(self, x_direction, y_direction):
        pass