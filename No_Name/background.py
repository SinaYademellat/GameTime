import pygame
from pygame.locals import *

if __name__ == '__main__':

    pygame.init()
    pygame.display.set_caption(' ^____^ ')          # Name of pygame windo :)
    window = pygame.display.set_mode((1000,500))    #  width = 1000     height = 500

    # Adding a background image
    bg_img = pygame.image.load('img/bg.png')
    bg_img = pygame.transform.scale(bg_img,(1000,500))

    '''
         #~~~~~~~~~~~~ <<  dar_ba_dar_rec :  our_hero >>

                    Rect(left, top, width, height)
                    Rect(pos, size)
                    Rect(obj)
      pygame.draw.rect(window ,color_of_dar_ba_dar_rec_RGB ,dar_ba_dar_rec )
    '''
    
    dar_ba_dar_rec_x , dar_ba_dar_rec_y = ( 10 ,430 )
    color_of_dar_ba_dar_rec_RGB =   (255,0,0)
   
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ << Move >>>  
    spead_of_hero = 0.3
    Move_List_and_spead = {
            K_a: (-spead_of_hero, 0),  # << a for Move Left >> 
            K_d: (spead_of_hero, 0),   # << d for Move Right >>
            K_w: (0, -spead_of_hero),  # << w for Move up >>
            K_s: (0, spead_of_hero)    # << s for Move down >>
        }

    ################
    bullet_sample = pygame.image.load('img/bullet_1.png')
    number_of_shot_you_have = 5
    ###################


    # Load img 
    #! Main Loop 
    
    runing = True
    
    while runing:
       
        window.blit(bg_img,(0,0))
        
        dar_ba_dar_rec =  pygame.Rect( dar_ba_dar_rec_x , dar_ba_dar_rec_y , 50 , 50)  # << our_hero >>

  
        ###################
        for i in range(number_of_shot_you_have):
            window.blit(bullet_sample,(15*(i),0))

        ###################

        for event in pygame.event.get():
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ << Exit >>
            if( (event.type == QUIT)  or (event.type == KEYDOWN and event.key == K_ESCAPE  ) ):
                runing = False
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ << KEYDOWN >>
            if(event.type == KEYDOWN ) :
                             # ============== << Fier >>
                if ( event.key == K_SPACE ):
                    if(number_of_shot_you_have > 0):
                        number_of_shot_you_have -= 1
                    else:
                        print("tir Nadari dadash :)")


        '''
        # !~~~~~~~~~~~~!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ << ^__^ BUG ^__^ >> ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ << Move Hero >>
        # if event.type == KEYDOWN : 
        #     if event.key in Move_List_and_spead:
        #         go_go_go = Move_List_and_spead[event.key]
        #         dar_ba_dar_rec.move_ip(go_go_go)

                # !~~~~~~~~~~~~~~~~~~~~~~~ << NEW >> ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                # ?How could I cause the plumber sprite to move constantly when left or right key is being held down?
                #* URL : https://stackoverflow.com/questions/9961563/how-can-i-make-a-sprite-move-when-key-is-held-down        
        
                #?~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<<END>>~~~~~~~~~~~~~~~~~~~~
        #! ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        '''
        
        keys =  pygame.key.get_pressed() 
        for i in Move_List_and_spead:
            if(keys[i]):
                xx,yy = Move_List_and_spead[i]
                dar_ba_dar_rec_x +=xx
                dar_ba_dar_rec_y +=yy
               
        
        pygame.draw.rect(window ,color_of_dar_ba_dar_rec_RGB ,dar_ba_dar_rec )   # Drawing 
        pygame.display.update()


    pygame.quit()