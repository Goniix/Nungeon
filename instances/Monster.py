class Monster:
    def __init__(self, x, y, monster_base):
        self.coord = [x, y]
        self.type = monster_base.type
        self.base_health = monster_base.baseHealth
        self.health = self.base_health
        self.base_speed = monster_base.baseSpeed
        self.speed = self.base_speed
        self.speedgen = monster_base.speedgen
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
        self.speedgen = 10
        self.type = "M"

    def step_method(self):
        """method executed each turn by the monster"""
        pass

    def death_method(self):
        pass
    
    def hit_method(self):
        pass
