import pygame
class Sprite():
    """
    creates sprite container from its info
    images -> list with all imported frames (even if only one frame)
    w -> int widt of the sprite (all must be same size)
    h -> int height of the sprite (all must be same size)
    """
    def __init__(self,images):

        if type(images) != list:
            self.images=[images]
        else:
            self.images=images
        
        self.w=self.images[0].get_width()
        self.h=self.images[0].get_height()

class SpriteGroup():
    """
    class for storing groups of sprites
    """
    def __init__(self):
        pass