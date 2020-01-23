import random
import pygame

class Food(object):
    """description of class"""

    food_img = pygame.image.load("images/food.png")
    

    #Конструктор
    def __init__(self):
        self.food_position = []
    #Определение случайных координат еды из списка свободного пространства
    def get_food_position(self,map):
        
        self.food_position = random.choice(map.free)
    #Отрисовка еды
    def draw_food(self,window):
        food_rect = pygame.Rect(self.food_position[0],self.food_position[1],10,10)
        window.blit(self.food_img,food_rect)

