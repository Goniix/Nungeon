class Player:
    def __init__(self,name, coords):
        self.coord = [coords[0], coords[1]]
        self.inv = []
        self.base_health = 500
        self.health = self.base_health
        self.player_name = name

    def move_player(self, x_direction, y_direction):
        pass