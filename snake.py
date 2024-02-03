import pygame
pygame.init()

from random import randint

WIN_SIZE = (500, 500)
win = pygame.display.set_mode(WIN_SIZE)
clock = pygame.time.Clock()


class Food:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def draw(self):
        pygame.draw.rect(win, (255, 0, 0),
                         (self.x * 10, self.y * 10, 10, 10))


class Snake:
    def __init__(self, x, y, facing):
        self.x = x
        self.y = y
        self.facing = facing
        self.body = []
    def draw(self):
        pygame.draw.rect(win, (255, 255, 255),
                         (self.x * 10, self.y * 10, 10, 10))
        for piece in self.body:
            pygame.draw.rect(win, (255, 255, 255),
                             (piece[0] * 10, piece[1] * 10, 10, 10))


def redraw_win():
    win.fill((0, 0, 0))
    apples[0].draw()
    snake.draw()
    pygame.display.update()

snake = Snake(25, 25, "right")
apples = []

game_over = False
done = False
while not done:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.facing != "down":
                snake.facing = "up"
            elif event.key == pygame.K_DOWN and snake.facing != "up":
                snake.facing = "down"
            elif event.key == pygame.K_RIGHT and snake.facing != "left":
                snake.facing = "right"
            elif event.key == pygame.K_LEFT and snake.facing != "right":
                snake.facing = "left"

    if len(apples) > 0:
        if apples[0].x == snake.x and apples[0].y == snake.y:
            snake.body.append([snake.x, snake.y, snake.x, snake.y])
            apples = []
        
    if len(apples) < 1:
        apple_place = (randint(0, 49), randint(0, 49))
        for piece in snake.body:
            while ((apple_place[0] == piece[0]
                    and apple_place[1] == piece[1])
                   or (apple_place[0] == snake.x
                       and apple_place[1] == snake.y)):
                apple_place = (randint(1, 50), randint(1, 50))
        apples.append(Food(apple_place[0], apple_place[1]))
    
    if len(snake.body) > 0:
        snake.body[0][2] = snake.body[0][0]
        snake.body[0][3] = snake.body[0][1]
        snake.body[0][0] = snake.x
        snake.body[0][1] = snake.y
        if len(snake.body) > 1:
            for i in range(1, len(snake.body)):
                snake.body[i][2] = snake.body[i][0]
                snake.body[i][3] = snake.body[i][1]
                snake.body[i][0] = snake.body[i-1][2]
                snake.body[i][1] = snake.body[i-1][3]

    if snake.facing == "right":
        snake.x += 1
    elif snake.facing == "left":
        snake.x -= 1
    elif snake.facing == "up":
        snake.y -= 1
    elif snake.facing == "down":
        snake.y += 1

    if (snake.x > 49 or snake.x < 0 or snake.y > 49 or snake.y < 0):
        done = True
    else:
        for piece in snake.body:
            if snake.x == piece[0] and snake.y == piece[1]:
                done = True
    
    redraw_win()

pygame.quit()
