import pygame
class Player:
    """class of the player"""
    def __init__(self,name, coords, sprt, screen):
        self.coord = [coords[0], coords[1]]
        self.inv = []
        self.base_health = 500
        self.health = self.base_health
        self.player_name = name
        self.base_speed = 3
        self.speed = self.base_speed
        self.sprt = sprt
        self.scrn = screen
        self.screen_info=pygame.display.Info()

    def get_x(self):
        return self.coord[0]

    def set_x(self,x):
        self.coord[0] = x

    def get_y(self):
        return self.coord[1]

    def set_y(self,y):
        self.coord[1] = y

    def get_inv(self):
        return self.inv

    def add_item_to_inv(self,itm):
        self.inv.append(itm)

    def move_player(self, tcor, x_direction, y_direction):
        self.coord[0]+= x_direction*self.speed*tcor
        self.coord[1]+= y_direction*self.speed*tcor

    def draw(self):
        return (self.sprt.images[0],[(self.screen_info.current_w/2)-(self.sprt.image_w/2),(self.screen_info.current_h/2)-(self.sprt.image_h/2)])

    def update(self, dt, keyinput):
        self.set_x(self.get_x()+(keyinput[0]*self.speed*dt))
        self.set_y(self.get_y()+(keyinput[1]*self.speed*dt))
