import pygame as pg
from random import *

pg.init()

#ekraan
clock = pg.time.Clock()
screen_width, screen_height = 600, 600
screen = pg.display.set_mode((screen_width, screen_height))

#ruut
"""moving_rect = pg.Rect(350, 350, 100, 100)
x_speed, y_speed = 5, 4"""

#palli koordinaadid
x_pos = 0
y_pos = 0
tegelane_x = 0
tegelane_y = 0
#palli gravitatsioon
y_grav = 1
tegelane_y_grav = 1
#palli hupe
jump_height = 20
tegelane_jump_height = 20
y_vel = jump_height
tegelane_y_vel = tegelane_jump_height
#palli koordinaadi muutus
xKoordinaat = 0
yKoordinaat = 0
xTegelane = 0
yTegelane = 0
#palli huppe check
jumping = False

#pildid
ground_img = pg.image.load('ground.png')
taust = pg.image.load('bglong.png')

jooksja3 = pg.image.load('jooksja3.png')
jooksja2 = pg.image.load('jooksja2.png')
jooksja1 = pg.image.load('jooksja1.png').convert_alpha()
jooksja1.set_colorkey((255, 255, 255))
jooksja2.set_colorkey((255, 255, 255))
jooksja3.set_colorkey((255, 255, 255))

class Jooksja(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for num in range(1, 4):
            img = pg.image.load(f'jooksja{num}.png')
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.vel = 0
        self.clicked = False

    def update(self):
        if flying == True:
            self.vel += 0.5
            if self.vel > 8:
                self.vel = 8
        if self.rect.bottom < 500:
            self.rect.y += int(self.vel)

        if game_over == False:
            if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                self.vel = -10
            if pg.mouse.get_pressed()[0] == 0:
                self.clicked = False

            self.counter += 1
            flap_cooldown = 5

            if self.counter > flap_cooldown:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images):
                    self.index = 0
            self.image = self.images[self.index]

            self.image = pg.transform.rotate(self.images[self.index], self.vel * -2)
        else:
            self.image = pg.transform.rotate(self.images[self.index], -90)

jooksja_group = pg.sprite.Group()
jo = Jooksja(100, int(screen_height / 2))

jooksja_group.add(jo)

#poranda kaamera
ground_scroll = 0
scroll_speed = 4

#tegelase kaamera
tegelane_scroll = 0

fps = 144
jooksja = jooksja1.get_rect(center=(100, 400))

#fps
font = pg.font.SysFont("Arial", 36)

def update_fps():
    frames = str(float(clock.get_fps()))
    frames_text = font.render(frames, 1, pg.Color("coral"))
    return frames_text

flying = False
game_over = False

run = True
while run:

    clock.tick(fps)

    #screen.blit(bg2, (0, 0))

    screen.blit(taust, (0, 0))
    jooksja_group.draw(screen)
    jooksja_group.update()
    screen.blit(ground_img, (ground_scroll, 500))
    print(jo.rect.bottom)

    if jo.rect.bottom >= 500:
        game_over = True
        flying = False
        print("jah")

    if game_over == False:
        ground_scroll -= scroll_speed
        if abs(ground_scroll) > 35:
            ground_scroll = 0

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.MOUSEBUTTONDOWN and flying == False and game_over == False:
            flying = True

        pg.display.update()

    x_pos += xKoordinaat
    y_pos += yKoordinaat
    tegelane_x += xTegelane
    tegelane_y += yTegelane


    if abs(ground_scroll) > 35:
        ground_scroll = 0
    if abs(tegelane_scroll) > 1:
        tegelane_scroll = 0
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN:
            print(pg.key.name(event.key))

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_a:
                xKoordinaat -= 10
                xTegelane -= 10
            if event.key == pg.K_d:
                xKoordinaat += 10
                xTegelane += 10
            if event.key == pg.K_w:
                yKoordinaat -= 10
                yTegelane -= 10
            if event.key == pg.K_s:
                yKoordinaat += 10
                yTegelane += 10

        if event.type == pg.KEYUP:
            if event.key == pg.K_a or event.key == pg.K_d:
                xKoordinaat = 0
                xTegelane = 0
            if event.key == pg.K_w or event.key == pg.K_s:
                yKoordinaat = 0
                yTegelane = 0

    keys = pg.key.get_pressed()
    if not keys[pg.K_SPACE] and not keys[pg.K_g]:
        pass
    else:
        jumping = True
        
    if jumping:
        y_pos -= y_vel
        tegelane_y -= tegelane_y_vel
        y_vel -= y_grav
        tegelane_y_vel -= tegelane_y_grav
        if y_vel < -jump_height or tegelane_y_vel < -tegelane_jump_height:
            jumping = False
            y_vel = jump_height
            tegelane_y_vel = tegelane_jump_height
        jooksja = jooksja3.get_rect(center=(tegelane_x, tegelane_y))
        screen.blit(jooksja2, jooksja)
    else:
        jooksja = jooksja3.get_rect(center=(tegelane_x, tegelane_y))
        screen.blit(jooksja3, jooksja)


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
    tegelane_x += xTegelane
    tegelane_y += yTegelane

    pg.time.delay(10)
    pg.display.update()


    #bouncing_rect()
    pg.display.flip()
    clock.tick(60)
