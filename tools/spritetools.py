from math import floor
import os
import pygame

def create_strip(filename, image_w, image_h,alpha):
    """
    returns a list of sprite from a sprite sheet
    filename-> path to image
    w-> width of each invidual sprite (has to be the same from each sprite
    h-> height of each invidual sprite (has to be the same from each sprite)
    alpha-> alpha of strip (same for each frame)
    """
    sheet= pygame.image.load(os.path.join(filename))
    strip=[]
    for i in range(sheet.get_width()//image_w):
        for j in range(sheet.get_height()//image_h):
            rect_surf=pygame.Surface((image_w,image_h))
            rect_surf.set_colorkey((0,0,0))
            rect_surf.set_alpha(alpha)
            rect_surf.blit(sheet,(0,0),(i*image_w,j*image_h,image_w,image_h))
            strip.append(rect_surf)
    return strip   

class Sprite():
    """
    creates sprite container from its info
    filename -> path to image
    w -> int widt of the sprite (all must be same size)
    h -> int height of the sprite (all must be same size)
    alpha -> alpha of strip (same for each frame)
    image_speed -> speed of the animation (bigger->slower)
    """
    def __init__(self,filename,image_w,image_h,alpha=255,image_speed=2):
        self.images=create_strip(filename,image_w,image_h,alpha)

        self.image_w=self.images[0].get_width()
        self.image_h=self.images[0].get_height()
        self.image_n=len(self.images)
        self.image_speed=image_speed
        self.align = [self.image_w/2,self.image_h/2]

    def get_blitable(self, target_x, target_y, dt_frame):
        """returns """
        return (self.images[floor(dt_frame/self.image_speed)%self.image_n],[target_x-self.align[0],target_y-self.align[1]])


class SpriteGroup():
    """
    class for storing groups of sprites
    """
    def __init__(self):
        pass
