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
    window.render_background()
    window.end_frame()