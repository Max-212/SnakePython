import pygame

class Menu(object):
    """description of class"""

    

    def __init__(self):
        self.menu_img = pygame.image.load("images/menu.png")
        self.menu_rect = (442,0,259,441)
        self.display_rect = (455,395,300,40)   
        self.basicFont = pygame.font.SysFont("microsoftjhengheimicrosoftjhengheiuibold", 36)


    def menu_draw(self,window,):
        window.blit(self.menu_img,self.menu_rect)
        pygame.draw.rect(window, (55,55,66), self.display_rect)

    def score_draw(self,window,score):
        
        score_text = self.basicFont.render("Score: " + str(score), True, [181,79,24] , [55,55,66] )
        window.blit(score_text,self.display_rect)

    

    
     
