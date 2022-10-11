import pygame
import os

def create_strip(filename, w, h):
    sheet= pygame.image.load(os.path.join(filename)).convert_alpha()
    strip=[]
    for i in range(sheet.get_width()//w):
        for j in range(sheet.get_height()//h):
            rect_surf=pygame.Surface((w,h))
            rect_surf.set_colorkey((0,0,0))
            rect_surf.blit(sheet,(0,0),(i*w,j*h,w,h))
            strip.append(rect_surf)
    return strip
        

class Sprite():
    """
    creates sprite container from its info
    images -> list with all imported frames (even if only one frame)
    w -> int widt of the sprite (all must be same size)
    h -> int height of the sprite (all must be same size)
    """
    def __init__(self,filename,w,h):
        self.images=create_strip(filename,w,h)
        
        self.w=self.images[0].get_width()
        self.h=self.images[0].get_height()

class SpriteGroup():
    """
    class for storing groups of sprites
    """
    def __init__(self):
        pass


