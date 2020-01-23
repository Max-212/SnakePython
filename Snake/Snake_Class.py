import pygame 

class Snake(object):
    """description of class"""
    #Конструктор
    def __init__(self):
        #Параметры змеи
        self.head = [221,232]
        self.body = [[221,232],[210,232],[199,232]]
        
    #Движение змейки 
    def move(self,control):
        if control.flag_direction == "RIGHT":
            self.head[0]+=11;
            control.checkMove = True
        if control.flag_direction == "LEFT":
            self.head[0]-=11;
            control.checkMove = True
        if control.flag_direction == "UP":
            self.head[1]-=11;
            control.checkMove = True
        if control.flag_direction == "DOWN":
            self.head[1]+=11;
            control.checkMove = True


    #Отрисовка змеи
    def draw(self,window):
        body_img = pygame.image.load("images/body.png")
        body_img = pygame.transform.scale(body_img , (11,11))
        head_img = pygame.image.load("images/head.png")
        head_img = pygame.transform.scale(head_img , (11,11))
        for segment in self.body[1:]:
            body_rect = pygame.Rect(segment[0],segment[1],11,11)    
            window.blit(body_img,body_rect)
        
        head_rect = pygame.Rect(self.body[0][0],self.body[0][1],11,11)
        window.blit(head_img,head_rect)
            
    #Анимация передвижения
    def animation(self):
        self.body.insert(0,list(self.head))
        self.body.pop()
    #Проверка столкновения с границами и зеркальное перемещение змейки !Не активно
    def check_boom(self):
        if self.head[0] == 419:
            self.head[0]=23
        elif self.head[0] ==12:
            self.head[0]=419
        elif self.head[1] ==23:
            self.head[1]=419
        elif self.head[1] ==419:
            self.head[1]=23
    #Взаимодействие с едой
    def eat(self,food,map):
         if self.head == food.food_position:
             self.body.append(food.food_position)
             food.get_food_position(map)
             return True
    #Проверка столкновений и выход из игры
    def check_end_game(self,map,control):
        if self.head in map.barrier:
            return True
        if self.head in self.body[1:]:
            return True



