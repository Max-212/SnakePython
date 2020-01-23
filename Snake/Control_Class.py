import pygame
from pygame.locals import*
class Control(object):
    """description of class"""
    #Конструктор
    def __init__(self):
        self.flag_game = True
        self.flag_direction = "RIGHT";
        self.flag_pause= False
        self.checkMove = True
    #Функция конца игры
    def GameOut(self):
        quit()
        exit()
        
    #Получение событий
    def control(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.GameOut()
            elif event.type ==  KEYDOWN and self.flag_pause and self.flag_game:
               
                if event.key == K_RIGHT and self.flag_direction!="LEFT" and self.checkMove:
                    self.flag_direction="RIGHT"
                    self.checkMove = False
                elif event.key == K_LEFT and self.flag_direction!="RIGHT" and self.checkMove:
                    self.flag_direction="LEFT"
                    self.checkMove = False
                elif event.key == K_UP and self.flag_direction!="DOWN" and self.checkMove:
                    self.flag_direction="UP"
                    self.checkMove = False
                elif event.key == K_DOWN and self.flag_direction!="UP" and self.checkMove:
                    self.checkMove = False
                    self.flag_direction="DOWN"
               
            if event.type ==  KEYDOWN:
                    
                if event.key == K_ESCAPE:
                     self.GameOut()
                elif event.key == K_SPACE:
                    if self.flag_pause:
                        self.flag_pause = False
                    else:
                        self.flag_pause = True
                    if not self.flag_game:
                        self.flag_game = True
                    
                        

