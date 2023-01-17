import pygame
from pygame.locals import *
import math

if __name__ == '__main__':

    pygame.init()
    pygame.display.set_caption(' ^____^ ')          # Name of pygame windo :)

    clock = pygame.time.Clock()

    # ------------------------------------------------
    # ------------ << Global constants >> ------------
    # ------------------------------------------------

    FrameHeight = 500
    FrameWidth = 1000
    window = pygame.display.set_mode((FrameWidth,FrameHeight))    #  width = 1000     height = 500
    # DEFINING MAIN VARIABLES IN SCROLLING
    scroll = 0


   

        #* Dar_ba_Dar ==  << HERO >>
    dar_ba_dar_rec_x = 10 
    dar_ba_dar_rec_y = 430 
    color_of_dar_ba_dar_rec_RGB =   (255,0,0)

   
        #* %%%%%%%%%%%%%%%%%%% << Move >>> %%%%%%%%%%%%%%%%%%% 
    spead_of_hero = 3

    Move_List_and_spead = {
                            ####### a-d-w-s 

            K_a: (-spead_of_hero, 0),  # << a for Move Left >> 
            K_d: (spead_of_hero, 0),   # << d for Move Right >>
            K_w: (0, -spead_of_hero),  # << w for Move up >>
            K_s: (0, spead_of_hero),  # << s for Move down >>
                            
                            ####### 4key :)
            K_LEFT: (-spead_of_hero, 0),
            K_RIGHT: (spead_of_hero, 0),
            K_UP: (0, -spead_of_hero),
            K_DOWN: (0, spead_of_hero)
            }

            #! ################## << Load img >> ################## 

                    # <<  Background >> 
    bg_img = pygame.image.load('img/bg.png')
    bg_img = pygame.transform.scale(bg_img,(1000,500))

    bullet_sample = pygame.image.load('img/bullet_1.png')
    number_of_shot_you_have = 5
        
    bullet_r3 = pygame.image.load('img/bullet_r3.png')
    
    R_key_png = pygame.image.load('img/R_key.png')
    bool_R_key_show_ = False

            #? ################## << Load img >> ################## 

    runing = True
    bool_shut_ = False
    shut_move_int = 50

    # ------------------------------------------------
    # ------------ << Global constants >> ------------
    # ------------------------------------------------



    # CHANGE THE BELOW 1 TO UPPER NUMBER IF
    # YOU GET BUFFERING OF THE IMAGE
    # HERE 1 IS THE CONSTATNT FOR REMOVING BUFFERING
    tiles = math.ceil(FrameWidth / bg_img.get_width()) + 1



    #! Main Loop     
    while runing:


            #! << Endless Scrolling in pygame >>
    #* ####################################### 
        
        # THIS WILL MANAGE THE SPEED OF
        # THE SCROLLING IN PYGAME
        clock.tick(100)
        
        I = 0

        while(I < tiles):
            window.blit(bg_img, (bg_img.get_width()*I + scroll, 0))
            I += 1
        # FRAME FOR SCROLLING
        scroll -= 6

        # RESET THE SCROLL FRAME
        if abs(scroll) > bg_img.get_width():
            scroll = 0


        #* ##############################################################################
        
        # window.blit(bg_img,(0,0))

        dar_ba_dar_rec =  pygame.Rect( dar_ba_dar_rec_x , dar_ba_dar_rec_y , 50 , 50)  # << our_hero >>

            ###################
        for i in range(number_of_shot_you_have):
            window.blit(bullet_sample,(15*(i),0))
            ###################

            ###################
        if(bool_R_key_show_):
            window.blit(R_key_png,(0,0))
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
                        bool_shut_ = True
                        shut_move_int = dar_ba_dar_rec_x + 50 
                    else:
                        bool_R_key_show_ = True

                # ============== << Reload time >>
                if ( event.key == K_r ):
                    number_of_shot_you_have = 5
                    bool_R_key_show_ = False



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
        
            ################### <<  Move it >> ###################
 
        keys =  pygame.key.get_pressed() 
        for i in Move_List_and_spead:
            if(keys[i]):
                xx,yy = Move_List_and_spead[i]
                dar_ba_dar_rec_x +=xx
                dar_ba_dar_rec_y +=yy
               

        # ! *******************************<< Drawing >> *******************************<<

        pygame.draw.rect(window ,color_of_dar_ba_dar_rec_RGB ,dar_ba_dar_rec )   # Drawing 

            #  -----> نمایش شلیک گلوله <----- 
        if(bool_shut_): 
            if(shut_move_int < 990):
                shut_move_int += 2 # << spead >>  :)
                window.blit(bullet_r3,(shut_move_int,dar_ba_dar_rec_y))
            else:
                bool_shut_ = False


        pygame.display.update()

    pygame.quit()