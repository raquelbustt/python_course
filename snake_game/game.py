# pip3 install pygame

import pygame
import sys
from snake_classes import Snake, Food

pygame.init()

screen_size = (300, 400)
screen = pygame.display.set_mode(screen_size)

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

    # snake draw
    for pos in snake.body:
        pygame.draw.rect(screen, pygame.Color(255,204,0), 
                                #esquerda, cima, largura, altura
                                pygame.Rect(pos[0], pos[1], 10, 10))

    # food draw
    pygame.draw.rect(screen, pygame.Color(255,0,0), pygame.Rect(food_position[0], food_position[1], 10, 10))

    pygame.display.update()

