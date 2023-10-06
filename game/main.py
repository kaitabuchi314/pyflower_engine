import pygame

import pyflower.window
import pyflower.globals

window = pyflower.window.Window(960, 540, (pyflower.globals.LIGHT_BLUE), "logo.png", True)

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
    window.end_frame()