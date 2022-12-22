import pygame
import random

pygame.init()

x = 1280
y = 720

screen = pygame.display.set_mode((x, y))
pygame.display.set_caption("Navezinha")

bg = pygame.image.load('images/bg2.jpg').convert_alpha()
bg = pygame.transform.scale(bg, (x, y))

alien = pygame.image.load('images/spaceship.png').convert_alpha()
alien = pygame.transform.scale(alien, (50, 50))

playerImg = pygame.image.load('images/space.png').convert_alpha()
playerImg = pygame.transform.scale(playerImg, (50, 50))
playerImg = pygame.transform.rotate(playerImg, -90)

missile = pygame.image.load('images/missile.png').convert_alpha()
missile = pygame.transform.scale(missile, (25, 25))
missile = pygame.transform.rotate(missile, -45)

pos_alien_x = 500
pos_alien_y = 360

pos_player_x = 200
pos_player_y = 300

vel_missile_x = 0
pos_missile_x = 200
pos_missile_y = 300

points= 0

triggered = False

play = True

font = pygame.font.Font('freesansbold.ttf', 50)

player_rect = playerImg.get_rect()
alien_rect = alien.get_rect()
missile_rect = missile.get_rect()


def respawn():
    x = 1350
    y = random.randint(1, 640)
    return [x, y]


def respawnMissile():
    triggered = False
    respawn_missile_x = pos_player_x
    respawn_missile_y = pos_player_y
    vel_missile_x = 0
    return [respawn_missile_x, respawn_missile_y, triggered, vel_missile_x]

def colisions():
    global points
    if player_rect.colliderect(alien_rect) or alien_rect.x == 60:
        points -=0.5
        return True
    elif missile_rect.colliderect(alien_rect):
        points += 1
        return True
    else:
        return False

while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    screen.blit(bg, (0, 0))

    rel_x = x % bg.get_rect().width
    screen.blit(bg, (rel_x - bg.get_rect().width, 0))  # background
    if rel_x < 1280:
        screen.blit(bg, (rel_x, 0))

    key = pygame.key.get_pressed()
    if key[pygame.K_UP] and pos_player_y > 1:
        pos_player_y -= 1
        if not triggered:
            pos_missile_y -= 1

    if key[pygame.K_DOWN] and pos_player_y < 665:
        pos_player_y += 1
        if not triggered:
            pos_missile_y += 1

    if key[pygame.K_SPACE]:
        triggered = True
        vel_missile_x = 1


    # Rect positions
    player_rect.y= pos_player_y
    player_rect.x= pos_player_x

    missile_rect.y= pos_missile_y
    missile_rect.x= pos_missile_x

    alien_rect.y= pos_alien_y
    alien_rect.x= pos_alien_x

    # Objects movement
    x -= 0.5
    pos_alien_x -= 1
    pos_missile_x += vel_missile_x

    pygame.draw.rect(screen,(255,0,0), player_rect,4)
    pygame.draw.rect(screen,(255,0,0), missile_rect,4)
    pygame.draw.rect(screen,(255,0,0), alien_rect,4)

    score = font.render(f'Score: {int(points)}',True,(0,0,0))
    screen.blit(score,(50,50))

    # Respawn
    if pos_alien_x == 50:
        pos_alien_x = respawn()[0]
        pos_alien_y = respawn()[1]

    if pos_missile_x == 1300 or colisions():
        pos_missile_x, pos_missile_y, triggered, vel_missile_x = respawnMissile()

    if pos_alien_x == 50 or colisions():
        pos_alien_x = respawn()[0]
        pos_alien_y = respawn()[1]

    screen.blit(alien, (pos_alien_x, pos_alien_y))
    screen.blit(missile, (pos_missile_x, pos_missile_y))
    screen.blit(playerImg, (pos_player_x, pos_player_y))

    pygame.display.update()
