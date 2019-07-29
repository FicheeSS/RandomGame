import pygame
from cst import *
from extActor import *

sol = Sol()
moving = Moving()
pygame.init()
screen = pygame.display.set_mode(screenResolution)

while i < 10000:
    sol.draw()
    moving.move()