import pygame
from pyflower.component import Component

class SpriteComponent(Component):
    def __init__(self, gameObject, sprite, window):
        super().__init__(gameObject)
        self.window = window
        self.sprite = pygame.image.load(sprite).convert_alpha(window.screen)
        self.gameObject = gameObject
        self.name = "SpriteComponent"
    
    def update(self):
        self.window.screen.blit(self.sprite, (self.gameObject.position.x, self.gameObject.position.y))