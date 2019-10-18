import pygame 
from extActor import imggrass , Sol
from cst import screenResolution
imgsautDroite = pygame.image.load("./RandomGame/img/sautdroite.bmp")
imgsautGauche = pygame.image.load("./RandomGame/img/sautgauche.bmp")
imgstill = pygame.image.load("./RandomGame/img/still.bmp")
imgmarcheDroite = pygame.image.load("./RandomGame/img/marchedroite.bmp")
imgmarcheGauche = pygame.image.load("./RandomGame/img/marchegauche.bmp")

l_KEY = 1
r_KEY = 2

KISautGauche = 101
KISautDroite = 102
KIStill = 103
KIMarcheDroite = 104
KIMarcheGauche = 105       

class Perso :
    def __init__(self,screen,sol):
        self.sol = sol
        self.screen = screen
        self.currentImg = imgstill
        self.x = 0
        self.y = 0
        self.mvtdelta = 1
        self.lastKey = 0
        self.injump = False
        self.jumpTime = 0
        self.jumpHeight = 80
        self.scrollingDistance = 100

    def move(self,objlist):
        self.keying()
        self.jump()
        self.screen.blit(self.currentImg,(self.x,self.y))
        if self.x + self.currentImg.get_rect().size[0] == screenResolution[0]:
            return False
        else :
            return True
        for obj in objlist :
            if self.checkcollision(obj) == True:
                obj.onCol()

    def keying(self):
        pygame.event.pump()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.lastKey = r_KEY
                if event.key == pygame.K_LEFT:
                    self.lastKey = l_KEY
                if  event.key == pygame.K_SPACE:
                    self.injump = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                        self.lastKey = 0 

        if self.lastKey == l_KEY and self.x > 0 :
            self.x -= self.mvtdelta
            if self.injump == True:
                self.imgChange(KISautGauche)
            else : 
                self.imgChange(KIMarcheGauche)
        elif self.lastKey == r_KEY and self.x + self.currentImg.get_rect().size[0] < screenResolution[0] :
            if self.x >= screenResolution[0] - self.scrollingDistance :
                self.scrolling(self.mvtdelta)
            self.x += self.mvtdelta
            if self.injump == True : 
                self.imgChange(KISautDroite)
            else :
                self.imgChange(KIMarcheDroite)
        elif self.injump == False :
            self.imgChange(KIStill)

    def checkcollision(self,obj):
        for rect in obj.getRect(): 
            if self.collisionWRect(rect) == True :
                return True
        return False


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

    def jump(self):
        if self.y <= 0:
            self.injump = False
            self.jumpTime = 0
        if self.injump == True :
            self.y -= self.mvtdelta
            self.jumpTime += 1 
            if self.jumpTime >= self.jumpHeight :
                self.injump = False
                self.jumpTime = 0
                if self.lastKey == l_KEY :
                    self.imgChange(KIMarcheGauche)
                else :
                    self.imgChange(KIMarcheDroite)
        elif self.y + self.currentImg.get_rect().size[1] and self.checkcollision(self.sol) == False:
            #gravity 
            self.y += 2

    def collisionWRect(self,rect):
        print(self.currentImg.get_rect().colliderect(rect))
        if self.currentImg.get_rect().colliderect(rect) != 1:
            return True
        else :
            return False

    def scrolling(self,x):
        print(x)
        self.sol.addx(x)