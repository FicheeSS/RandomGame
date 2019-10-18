import pygame
from cst import screenResolution 
from extActor import Sol , Enemies
from animate import *
import sys
import random
import time

pygame.init()
screen = pygame.display.set_mode(screenResolution)
sol = Sol(screen)


perso = Perso(screen,sol)

EnnemiesList = []
Elimit = 2

for i in range(random.randint(0,Elimit)):
    EnnemiesList.append(Enemies((1000,1000),screen))

endgame = True
while endgame == True : 
    ft = time.time()
    screen.fill((0,0,0))
    sol.draw()
    objlist = EnnemiesList
    """
    for foe in EnnemiesList :
        if perso.collisionWRect(foe.getRect()) :
            endgame = False
        else :
            if foe.moving() == False :
                EnnemiesList.remove(foe)
            foe.draw()
    """
    if endgame :
        endgame = perso.move(objlist)


    pygame.display.flip()
    ExecTime =  (time.time() - ft)
    if ExecTime > 1/60 : 
        print("Frame time too high lack : " + str((ExecTime-1/60)*-1) )

    #else : 
        #wait(1/60 - ExecTime)


    
pygame.quit()


sys.exit(0)