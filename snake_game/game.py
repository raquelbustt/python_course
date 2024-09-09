# pip3 install pygame
import pygame
import sys
from snake_classes import Snake, Food
import time

pygame.init()

screen_size = (300, 400)
screen = pygame.display.set_mode(screen_size)

# cronometro
tempo = pygame.time.Clock()

snake = Snake()
food = Food()
food_position = food.position

# starts game loop

while True:
    screen.fill((7,0,35)) # RGB

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.change_direction('RIGHT')
            if event.key == pygame.K_UP:
                snake.change_direction('UP')
            if event.key == pygame.K_DOWN:
                snake.change_direction('DOWN')
            if event.key == pygame.K_LEFT:
                snake.change_direction('LEFT')
    
    food_position = food.new_food()
    # se a cobra comeu a comida
    if snake.move(food_position):
        # comida devorada = True
        food.eaten = True

    if snake.check_collision():
        # print("collided")
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # snake draw
    for pos in snake.body:
        pygame.draw.rect(screen, pygame.Color(255,204,0), 
                                #esquerda, cima, largura, altura
                                pygame.Rect(pos[0], pos[1], 10, 10))

    # food draw
    pygame.draw.rect(screen, pygame.Color(255,0,0), pygame.Rect(food_position[0], food_position[1], 10, 10))

    pygame.display.update()

    # frames por segundo
    tempo.tick(22)

