import pygame
from pygame.locals import *

class Window:
    def __init__(self, width, height, bgcolor, icon, resizable):
        pygame_icon = pygame.image.load(icon)
        pygame.init()
        pygame.display.set_icon(pygame_icon)
        displayInfo = pygame.display.Info()
        self.bgcolor = bgcolor
        if resizable:
            self.screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
        else:
            self.screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
    
    def render_background(self):
        self.screen.fill(self.bgcolor)
    def end_frame(self):
        pygame.display.update()
