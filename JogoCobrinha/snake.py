
import pygame, random
from pygame.locals import *

def on_grid_random():
    x = random.randint(0,590)
    y = random.randint(0,590)
    return (x//10 * 10, y//10 * 10)

def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

def play():
    pygame.init()
    screen = pygame.display.set_mode((600,600))
    pygame.display.set_caption('Snake')

    snake = [(200, 200), (210, 200), (220,200)]
    snake_skin = pygame.Surface((10,10))
    snake_skin.fill((255,255,255))

    apple_pos = on_grid_random()
    apple = pygame.Surface((10,10))
    apple.fill((255,0,0))

    game_over = False

    my_direction = LEFT

    clock = pygame.time.Clock()

    font = pygame.font.Font('freesansbold.ttf', 18)
    score = 0

    while True:
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

            if event.type == KEYDOWN:
                if event.key == K_UP and my_direction != DOWN:
                    my_direction = UP
                if event.key == K_DOWN and my_direction != UP:
                    my_direction = DOWN
                if event.key == K_LEFT and my_direction != RIGHT:
                    my_direction = LEFT
                if event.key == K_RIGHT and my_direction != LEFT:
                    my_direction = RIGHT
                if event.key == K_r:
                    play()
                if event.key == K_q:
                    pygame.quit()

        if collision(snake[0], apple_pos):
            apple_pos = on_grid_random()
            snake.append((0,0))
            score = score + 1

        if snake[0][0] == 600 or snake[0][1] == 600 or snake[0][0] < 0 or snake[0][1] < 0:
            game_over = True

        for i in range(1, len(snake) - 1):
            if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
                game_over = True

        for i in range(len(snake) - 1, 0, -1):
            snake[i] = (snake[i-1][0], snake[i-1][1])

        if my_direction == UP:
            snake[0] = (snake[0][0], snake[0][1] - 10)
        if my_direction == DOWN:
            snake[0] = (snake[0][0], snake[0][1] + 10)
        if my_direction == RIGHT:
            snake[0] = (snake[0][0] + 10, snake[0][1])
        if my_direction == LEFT:
            snake[0] = (snake[0][0] - 10, snake[0][1])

        screen.fill((0,0,0))
        screen.blit(apple, apple_pos)

        score_font = font.render('Score: %s' % (score), True, (255, 255, 255))
        score_rect = score_font.get_rect()
        score_rect.topleft = (600 - 120, 10)
        screen.blit(score_font, score_rect)


        for pos in snake:
            screen.blit(snake_skin,pos)

        pygame.display.update()

        if game_over:
            game_over_font = pygame.font.Font('freesansbold.ttf', 75)
            game_over_screen = game_over_font.render('Game Over', True, (255, 255, 255))
            game_over_rect = game_over_screen.get_rect()
            game_over_rect.midtop = (600 / 2, 10)
            screen.blit(game_over_screen, game_over_rect)

            restart_font = pygame.font.Font('freesansbold.ttf', 25)
            restart_screen = restart_font.render('Press r to restart the game', True, (255, 255, 255))
            restart_rect = restart_screen.get_rect()
            restart_rect.midtop = (600/2, 300)
            screen.blit(restart_screen, restart_rect)


            restart_font = pygame.font.Font('freesansbold.ttf', 25)
            restart_screen = restart_font.render('Press q to quit the game', True, (255, 255, 255))
            restart_rect = restart_screen.get_rect()
            restart_rect.midtop = (600/2, 400)
            screen.blit(restart_screen, restart_rect)

            
            pygame.display.update()
            pygame.time.wait(500)


play()
