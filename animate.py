import pygame
from main import * 
from cst import *

class Moving :
    def __init__(self):
        self.currentImg = imgstill
        self.x = 0
        self.y = 0
        self.lastKey = 0

    def move(self):
        screen.blit(self.currentImg,(self.x,self.y))

    def keying(self):
    pygame.event.pump()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.lastKey = r_KEY
            if event.key == pygame.K_LEFT:
                self.lastKey = l_KEY
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                self.lastKey = 0 
    if self.lastKey == l_KEY and self.x > 0:
        self.x -= self.mvtdelta
    elif self.lastKey == r_KEY and self.x + self.width < SCREENSIZE[0]:
        self.x += self.mvtdelta
    
    def imgChange(self,moving):
        if moving == KISautGauche : 
            self.currentImg = imgsautGauche
        if moving == KISautDroite : 
            self.currentImg = imgsautDroite
        if moving == KIMarcheDroite : 
            self.currentImg = imgmarcheDroite
        if moving == KIMarcheGauche : 
            self.currentImg = imgmarcheGauche
        if moving == KIStill : 
            self.currentImg = imgstill
