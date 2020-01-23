#Импорт модулей и классов
import pygame
import time
from Snake_Class import Snake
from Food_Class import Food
from Map_Class import Map
from Control_Class import Control
from Menu_Class import Menu

# Загрузка изображений
gameover_img = pygame.image.load("images/GAMEOVER.png")
win_img = pygame.image.load("images/WIN.png")

#Начало программы
pygame.init()
fps = pygame.time.Clock()

#Задаем параметры окна
window = pygame.display.set_mode((700,441))
pygame.display.set_caption("Snake")
window_rect = pygame.Rect(0,0,441,441)

#Создаем объекты игры
score =0

control = Control()
snake = Snake()

map=Map()
#Создаем изображение карты.
map.create_img()
map = Map()
#Сортирует карту-список на списки границ и свободного пространства
map.filter() 

food = Food()
food.get_food_position(map)

menu = Menu()
menu.menu_draw(window)

#Цикл работы приложения
while True:

    control.control()
    menu.score_draw(window, "     ")

    #Игровой цикл
    while control.flag_game:

        #Получение события
        control.control()

        #Заливка экрана
        window.blit(map.ground_img,window_rect)
    

        #Отрисовка змеи на окне
        snake.draw(window)
    
        #Отрисовка еды на окне
        food.draw_food(window)

        #Отрисовка карты на окне
        map.draw_map(window)
        
        #Отображение счета
        menu.score_draw(window, score)

        if control.flag_pause:
        
            #Перемещение змеи
            snake.move(control) 

            #Анимация передвижения
            snake.animation()

            #Отрисовка змеи на окне
            snake.draw(window)

            #Проверка столкновений с границами
            if snake.check_end_game(map,control):
                window.blit(gameover_img,window_rect)
                control.flag_game = False
                snake = Snake()
                control.flag_direction = "RIGHT"
                map.changeLevel(map.level1)
                food.get_food_position(map)
                score = 0
                
                


            #Проверка столкновения с едой
            if snake.eat(food,map):
                score+=1
                if score == 10:
                    map.changeLevel(map.level2)
                    snake = Snake()
                    control.flag_pause = False
                    control.flag_direction = "RIGHT"
                    food.get_food_position(map)
                if score == 20:
                    map.changeLevel(map.level3)
                    snake = Snake()                   
                    control.flag_pause = False
                    control.flag_direction = "RIGHT"
                    food.get_food_position(map)
                if score == 30:
                    window.blit(win_img,window_rect)
                    control.flag_game = False
                    snake = Snake()
                    control.flag_direction = "RIGHT"
                    map.changeLevel(map.level1)
                    food.get_food_position(map)
                    menu.score_draw(window, score)
                    score = 0
                
#
        #Обновление экрана !Возможна альтернатива: pygame.display.update()
        pygame.display.flip()
        fps.tick(15)