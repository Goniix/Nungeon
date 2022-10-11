from logging.handlers import WatchedFileHandler
import pygame

class Debug:
    def __init__(self):
        self.watcher_list=[]
        self.my_font = pygame.font.SysFont('Comic Sans MS', 10)
    
    def add_watcher(self, label, method):
        """
        adds an event watcher to the debugtool
        label -> string 
        ex: "fps"
        methof -> lambda 
        ex: lambda: clock.get_fps()
        """
        self.watcher_list.append((label,method))

    def draw(self):
        surf_list = []
        j=0
        for i in self.watcher_list:
            surf_list.append((self.my_font.render(str(i[0])+": "+str(i[1]()), False, (255,255,255)),[0,0+(15*j)]))
            j+=1
        return surf_list