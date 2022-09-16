class Item:
    def __init__(self, x, y, item_base):
        self.coord = [x, y]
        self.collide_method = item_base.collide_method
        self.step_method = item_base.step_method
        self.description = item_base.description
        self.type = item_base.type
        self.solid = item_base.solid

    def collide(self):
        self.collide_method()

    def execute_item(self):
        self.step_method()


class ItemTemplate:
    def __init__(self):
        self.solid = False
        self.type = "X"

    def collide_method(self):
        """executed when player steps on it"""
        pass

    def step_method(self):
        """executed on each turn"""
        pass