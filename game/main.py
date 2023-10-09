import pygame
from pyflower.gameobject import GameObject
from pyflower.vector2 import Vector2
from pyflower.spriterenderer import SpriteComponent
import pyflower.window
import pyflower.globals

window = pyflower.window.Window(960, 540, (pyflower.globals.LIGHT_BLUE), "logo.png", True)

o = GameObject(Vector2(0,0))
o.AddComponent(SpriteComponent(object, "logo.png", window))

running = True
while (running):
    for event in pygame.event.get():
        #close the window if user commands
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if window.bgcolor == pyflower.globals.LIGHT_BLUE:
                window.bgcolor = pyflower.globals.LIGHT_ORANGE
            elif window.bgcolor == pyflower.globals.LIGHT_ORANGE:
                window.bgcolor = pyflower.globals.LIGHT_BLUE
            
    window.render_background()
    o.update()
    window.end_frame()
