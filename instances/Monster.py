from math import *
class Monster:
    def __init__(self, x, y, monster_base):
        self.coord = [x, y]
        self.type = monster_base.type
        self.base_health = monster_base.baseHealth
        self.health = self.base_health
        self.base_speed = monster_base.baseSpeed
        self.speed = self.base_speed
        self.description = monster_base.description
        self.name = monster_base.name

        self.step_method = monster_base.step_method
        #self.attack_method = monster_base.attack_method
        self.hit_method = monster_base.hit_method
        self.death_method = monster_base.death_method

class MonsterTemplate:
    def __init__(self) -> None:
        self.name = "Defaultname"
        self.description = "DefaultDescription"
        self.base_health = 500
        self.base_speed = 10
        self.type = "M"

    def step_method(self,player_x,player_y):
        """method executed each turn by the monster"""
        dist=sqrt(((player_x-self.coord[0])**2)-((player_y-self.coord[1])**2))
        self.coord[0]+= 0
        pass

    def death_method(self):
        pass
    
    def hit_method(self):
        pass
