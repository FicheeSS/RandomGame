import pygame
from cst import screenResolution 
import random
import math

imggrass = pygame.image.load("./RandomGame/img/grass.bmp")
EnemyImageList = [pygame.image.load("./RandomGame/img/macron.bmp"),pygame.image.load("./RandomGame/img/fusee.bmp")]

class Sol :
    def __init__(self,screen):
        self.image = imggrass
        self.screen = screen
        self.listRect = []

    def draw(self):
        i = 0
        while i <= screenResolution[0]:
            self.screen.blit(self.image,( i , screenResolution[1] -self.image.get_rect().size[1]))
            self.listRect.append(pygame.rect((i,screenResolution[1] -self.image.get_rect().size[1]),(self.image.get_rect().size[0],self.image.get_rect().size[1])))
            i += self.image.get_rect().size[0]

    
    def addx(self,add):
        self.x += add
    def getRect(self):
        return listRect



class Enemies :
    def __init__(self,pos,screen):
        self.img = pygame.transform.scale(EnemyImageList[random.randint(0,len(EnemyImageList)-1)],(50,100))
        self.size = self.img.get_rect().size
        self.x = pos[0]
        self.y = pos[1]
        self.screen = screen
        self.coef = random.randint(-5, 5)  

    def draw(self) :
        self.screen.blit(self.img,(self.x,self.y))
    
    def getRect(self):
        return self.img.get_rect()
    
    def moving(self):
        if self.x >= screenResolution[0] or self.x <= 0 or self.y >= screenResolution[0] or self.y <= 0 :
            return False
        else : 
            self.x = self.x * math.cos(self.coef)
            self.y = self.y * math.sin(self.coef)
            return True

    def onCol(self):
        print("xd t mort")

        
            
