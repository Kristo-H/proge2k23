import pygame as pg

pg.init()

screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()
player = pg.image.load("Pygame_logo.svg.png").convert_alpha()
player2 = pg.transform.scale(player, (200,200))

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

    pg.display.update()
    clock.tick(60)