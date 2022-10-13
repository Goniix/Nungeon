import pygame
class Player:
    def __init__(self,name, coords, sprt, screen):
        self.coord = [coords[0], coords[1]]
        self.inv = []
        self.base_health = 500
        self.health = self.base_health
        self.player_name = name
        self.base_speed = 5
        self.speed = self.base_speed
        self.sprt = sprt
        self.scrn = screen
        
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
        return (self.sprt.images[0],[(1194/2)-(self.sprt.w/2),(834/2)-(self.sprt.h/2)])
    
    def update(self, dt, keyinput):
        self.set_x(self.get_x()+(keyinput[0]*self.speed*dt))
        self.set_y(self.get_y()+(keyinput[1]*self.speed*dt))