import pygame
from cst import * 

class Sol :
    def __init__(self):
        self.height = 10
        self.image = imggrass
        print(self.image.get_rect().size)

    def draw(self):
        i = 0
        while i <= screenResolution[0]:

            i += self.image.get_rect().size[0]