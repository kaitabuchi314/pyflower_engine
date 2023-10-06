import pygame
from pygame.locals import *


#color defenitions
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
LIGHT_BLUE = (0, 200, 240)
LIGHT_ORANGE = (240, 200, 0)

#init window
pygame.init()
displayInfo = pygame.display.Info()
screen = pygame.display.set_mode((700, 700))
background = pygame.image.load("game/bg.png").convert_alpha(screen)
pygame.mouse.set_visible(True)

#init game
running = True
mouse_pos = None
player_image = pygame.image.load("game/player.png").convert_alpha(screen)

#functions
def draw_sprite(sprite, position):
	screen.blit(sprite, position)

def draw_bg():
	screen.fill(LIGHT_ORANGE)

#Game Loop
while running:
	for event in pygame.event.get():
		#close the window if user commands
		if event.type == pygame.QUIT:
			running = False

		#draw Background
		draw_bg()

		#game logic
		player_pos = (10, 10)
		#draw sprites
		draw_sprite(player_image, player_pos)
		#end frame
		pygame.display.update()

pygame.quit()