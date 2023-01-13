import pygame
from pygame.locals import *

if __name__ == '__main__':

    pygame.init()
    pygame.display.set_caption(' ^____^ ') # Name of pygame windo :)
    width = 1000
    height = 500
    window = pygame.display.set_mode((width,height))

    # STEP 3: Adding a background image
    bg_img = pygame.image.load('img/bg.png')
    bg_img = pygame.transform.scale(bg_img,(width,height))

    #! Main Loop 
    runing = True
    while runing:
        
        window.blit(bg_img,(0,0))

         
        for event in pygame.event.get():
        
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ << Exit >>
            if event.type == QUIT:
                runing = False

        pygame.display.update()


    pygame.quit()

    ###############################################################