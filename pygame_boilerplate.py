"""
This file is boilerplate to set up your pygame environment.
You should use this as a template to begin coding your game.
"""

from sys import exit  # kill Python after pygame.quit()
import pygame

# ---- Configure the constants below ---- #
SCREEN_WIDTH = 800  # pixels
SCREEN_HEIGHT = 400  # pixels
CAPTION = "Game Title"
# movement is rendered in terms of frames
# e.g. sprite moves 10 px per frame
MAXIMUM_FPS = 60
# --------------------------------------- #

pygame.init()  # initialize pygame process
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(CAPTION)
clock = pygame.time.Clock()

while True:
    # main loop to run the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # checks if close-window is pressed
            pygame.quit()  # kill pygame process
            exit()  # kills Python process

    pygame.display.update()  # update screen by drawing next frame
    clock.tick(MAXIMUM_FPS)
