import pygame
import os
from math import floor

def create_strip(filename, w, h,alpha):
    """
    returns a list of sprite from a sprite sheet
    filename-> path to image
    w-> width of each invidual sprite (has to be the same from each sprite or there maybe be cropping)
    h-> height of each invidual sprite (has to be the same from each sprite or there maybe be cropping)
    alpha-> alpha of strip (same for each frame)
    """
    sheet= pygame.image.load(os.path.join(filename))
    strip=[]
    for i in range(sheet.get_width()//w):
        for j in range(sheet.get_height()//h):
            rect_surf=pygame.Surface((w,h))
            rect_surf.set_colorkey((0,0,0))
            rect_surf.set_alpha(alpha)
            rect_surf.blit(sheet,(0,0),(i*w,j*h,w,h))
            strip.append(rect_surf)
    return strip
        

class Sprite():
    """
    creates sprite container from its info
    images -> list with all imported frames (even if only one frame)
    w -> int widt of the sprite (all must be same size)
    h -> int height of the sprite (all must be same size)
    alpha -> alpha of strip (same for each frame)
    image_speed -> speed of the animation (bigger->slower)
    """
    def __init__(self,filename,w,h,alpha=255,image_speed=2):
        self.images=create_strip(filename,w,h,alpha)
        
        self.w=self.images[0].get_width()
        self.h=self.images[0].get_height()
        self.image_n=len(self.images)
        self.image_speed=image_speed
        self.align = [self.w/2,self.h/2]
    
    def get_blitable(self, x, y, dt_frame):
        return (self.images[floor(dt_frame/self.image_speed)%self.image_n],[x-self.align[0],y-self.align[1]])


class SpriteGroup():
    """
    class for storing groups of sprites
    """
    def __init__(self):
        pass


