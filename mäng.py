import pygame as pg
from random import *

pg.init()

#screen_w = 600
#screen_h = 600
#screen = pg.display.set_mode((screen_w, screen_h))
#clock = pg.time.Clock()
#player = pg.image.load("Pygame_logo.svg.png").convert_alpha()
#player2 = pg.transform.scale(player, (200,200))

def bouncing_rect():
    global x_speed, y_speed, other_speed, other_speed2, other_speed3
    moving_rect.x += x_speed
    moving_rect.y += y_speed

    if moving_rect.right >= screen_width or moving_rect.left <= 0:
        x_speed *= -1
    if moving_rect.bottom >= screen_height or moving_rect.top <= 0:
        y_speed *= -1

    other_rect.y += other_speed
    if other_rect.top <= 0 or other_rect.bottom >= screen_height:
        other_speed *= -1

    other_rect2.x += other_speed2
    if other_rect2.left <= 0 or other_rect2.right >= screen_width:
        other_speed2 *= -1

    other_rect3.y += other_speed3
    if other_rect3.top <= 0 or other_rect3.bottom >= screen_height:
        other_speed3 *= -1

    collision_tolerance = 10
    if moving_rect.colliderect(other_rect):
        if abs(other_rect.top - moving_rect.bottom) < collision_tolerance and y_speed > 0:
            y_speed *= -1
        if abs(other_rect.bottom - moving_rect.top) < collision_tolerance and y_speed < 0:
            y_speed *= -1
        if abs(other_rect.bottom - moving_rect.left) < collision_tolerance and x_speed < 0:
            x_speed *= -1
        if abs(other_rect.bottom - moving_rect.right) < collision_tolerance and x_speed > 0:
            x_speed *= -1
    if moving_rect.colliderect(other_rect2):
        if abs(other_rect2.top - moving_rect.bottom) < collision_tolerance and y_speed > 0:
            y_speed *= -1
        if abs(other_rect2.bottom - moving_rect.top) < collision_tolerance and y_speed < 0:
            y_speed *= -1
        if abs(other_rect2.bottom - moving_rect.left) < collision_tolerance and x_speed < 0:
            x_speed *= -1
        if abs(other_rect2.bottom - moving_rect.right) < collision_tolerance and x_speed > 0:
            x_speed *= -1
    if moving_rect.colliderect(other_rect3):
        if abs(other_rect3.top - moving_rect.bottom) < collision_tolerance and y_speed > 0:
            y_speed *= -1
        if abs(other_rect3.bottom - moving_rect.top) < collision_tolerance and y_speed < 0:
            y_speed *= -1
        if abs(other_rect3.bottom - moving_rect.left) < collision_tolerance and x_speed < 0:
            x_speed *= -1
        if abs(other_rect3.bottom - moving_rect.right) < collision_tolerance and x_speed > 0:
            x_speed *= -1
    pg.draw.rect(screen, (255, 0, 0), moving_rect)
    pg.draw.rect(screen, (0, 255, 0), other_rect)
    pg.draw.rect(screen, (0, 0, 255), other_rect2)
    pg.draw.rect(screen, (255, 0, 255), other_rect3)

pg.init()
clock = pg.time.Clock()
screen_width, screen_height = 600, 600
screen = pg.display.set_mode((screen_width, screen_height))
moving_rect = pg.Rect(350, 350, 100, 100)
x_speed, y_speed = 5, 4

other_rect = pg.Rect(300, 400, 200, 100)
other_speed = 2

other_rect2 = pg.Rect(randint(100, 300), randint(100, 400), randint(100, 200), randint(50, 100))
other_speed2 = randint(1, 10)

other_rect3 = pg.Rect(randint(100, 300), randint(100, 400), randint(100, 200), randint(50, 100))
other_speed3 = randint(2, 10)

class Ruut:
    def __init__(self, kyljepikkus):
        self.kyljepikkus = kyljepikkus

class ring:
    def __init__(self, kyljepikkus):
        self.kyljepikkus = kyljepikkus

x_pos = 0
y_pos = 0
y_grav = 1
jump_height = 20
y_vel = jump_height
xKoordinaat = 0
yKoordinaat = 0
gameplay = True
v = 5
m = 1
isjump = False
jumping = False

standing_surface = pg.transform.scale(pg.image.load("basketball3.png"), (96, 128))
jumping_surface = pg.transform.scale(pg.image.load("basketball4.png"), (96, 128))
bg = pg.transform.scale(pg.image.load("images.png"), (600, 600))
hoop = pg.transform.scale(pg.image.load("hoop.png"), (200, 200))

ball_rect = standing_surface.get_rect(center=(x_pos, y_pos))
while gameplay:
    #clock.tick(60)
    screen.fill((0, 0, 0))
    color = (255, 0, 0)
    x_pos += xKoordinaat
    y_pos += yKoordinaat
    #rect = pg.draw.rect(screen, color, (x_pos, y_pos, 50, 50))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            gameplay = False
        if event.type == pg.KEYDOWN:
            print(pg.key.name(event.key))

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_a:
                xKoordinaat -= 10
            if event.key == pg.K_d:
                xKoordinaat += 10
            if event.key == pg.K_w:
                yKoordinaat -= 10
            if event.key == pg.K_s:
                yKoordinaat += 10

        if event.type == pg.KEYUP:
            if event.key == pg.K_a or event.key == pg.K_d:
                xKoordinaat = 0
            if event.key == pg.K_w or event.key == pg.K_s:
                yKoordinaat = 0

    #screen.blit(standing_surface, ball_rect)
    keys = pg.key.get_pressed()
    if keys[pg.K_SPACE]:
        jumping = True
    screen.blit(bg, (0, 0))
    screen.blit(hoop, (300, 300))
    if jumping:
        y_pos -= y_vel
        y_vel -= y_grav
        if y_vel < -jump_height:
            jumping = False
            y_vel = jump_height
        ball_rect = standing_surface.get_rect(center=(x_pos, y_pos))
        screen.blit(jumping_surface, ball_rect)
    else:
        ball_rect = standing_surface.get_rect(center=(x_pos, y_pos))
        screen.blit(standing_surface, ball_rect)



    if x_pos > 600:
        x_pos = 0
        print("x aar", x_pos)
    elif x_pos < 0:
        x_pos = 600
        print("x aar", x_pos)
    if y_pos > 600:
        y_pos = 0
        print("y aar", y_pos)
    elif y_pos < 0:
        y_pos = 600
        print("y aar", y_pos)
    x_pos += xKoordinaat
    y_pos += yKoordinaat
    #rect = pg.draw.rect(screen, color, (x_pos, y_pos, 50, 50))
    pg.time.delay(10)
    pg.display.update()
    #screen.blit(player2, (x, y))

    """pg.display.update()
    clock.tick(60)"""

    bouncing_rect()
    pg.display.flip()
    clock.tick(60)