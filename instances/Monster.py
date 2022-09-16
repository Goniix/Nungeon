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