# pip3 install pygame
import pygame
import sys
from snake_classes import Snake, Food
import time


# inicar fonte
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 12)

pygame.init()

screen_size = (300, 400)
screen = pygame.display.set_mode(screen_size)

# cronometro
tempo = pygame.time.Clock()

score = 0

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
        score += 1

    if snake.check_collision():
        # print("collided")
        score_surface = my_font.render(f'Pontuação {score}', True, (255,255,255))
        screen.blit(score_surface, (10,10))

        you_lose = my_font.render(f'YOU LOSE!', True, (255,255,255))
        screen.blit(you_lose, (100,180))
        pygame.display.flip()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # texto pontuacao
    # aqui eu tive erro porque score era um inteiro e ao usar render() eu estava mudando para um objeto e causando erro
    # por isso ajustei score para score_surface
    score_surface = my_font.render(f'Pontuação {score}', True, (255,255,255))
    screen.blit(score_surface, (10,10))

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

