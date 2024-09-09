import random

class Snake:
    def __init__(self, screen=(300, 400), position=[50,30], body=[[50, 30], [40, 30], [30,30]], direction = 'RIGHT'):
            self.screen = screen
            self.position = position
            self.body = body
            self.direction = direction
    
    def change_direction(self, new_direction):
        if new_direction == 'RIGHT' and not self.direction == 'LEFT':
            self.direction = 'RIGHT'
        if new_direction == 'LEFT' and not self.direction == 'RIGHT':
            self.direction = 'LEFT'
        if new_direction == 'UP' and not self.direction == 'DOWN':
            self.direction = 'UP'
        if new_direction == 'DOWN' and not self.direction == 'UP':
            self.direction = 'DOWN'
    
    def move(self, food_position):
        if self.direction == 'RIGHT':
            self.position[0] += 10
        if self.direction == 'LEFT':
            self.position[0] -= 10
        if self.direction == 'UP':
            self.position[1] -= 10
        if self.direction == 'DOWN':
            self.position[1] += 10

        # adiciona pedaço do corpo da cabeça na frente da cabeça
        self.corpo.insert(0, list(self.position))
        # confere se comeu comida
        if self.position == food_position:
            return True
        # remove um pedaço da cauda
        self.body.pop()


    def check_collision(self):
        pass
    

class Food:
    def __init__(self, screen=(300, 400)):
        self.screen = screen
        self.position = [random.randrange(10, self.screen[0],10), random.randrange(10, self.screen[1], 10)]
        self.eaten = False

    def new_food(self):
        pass