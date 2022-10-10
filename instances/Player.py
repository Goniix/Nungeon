class Player:
    def __init__(self,name, coords, sprite):
        self.coord = [coords[0], coords[1]]
        self.inv = []
        self.base_health = 500
        self.health = self.base_health
        self.player_name = name
        self.base_speed = 10
        self.speed = self.base_speed
        self.sprite = sprite

    def move_player(self, tcor, x_direction, y_direction):
        self.coord[0]+= x_direction*self.speed*tcor
        self.coord[1]+= y_direction*self.speed*tcor
    
    def draw(self):
        pass
        #draw at players coord