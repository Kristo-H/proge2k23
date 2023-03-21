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

x = 1
y = 1
xKoordinaat = 0
yKoordinaat = 0
gameplay = True
while gameplay:
    clock.tick(60)
    screen.fill((0, 0, 0))
    color = (255, 0, 0)
    x += xKoordinaat
    y += yKoordinaat
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
            if event.key == pg.K_SPACE:
                hupe = 10
        if event.type == pg.KEYUP:
            if event.key == pg.K_a or event.key == pg.K_d:
                xKoordinaat = 0
            if event.key == pg.K_w or event.key == pg.K_s:
                yKoordinaat = 0

        if x > 600 or x < 0:
            print("x aar")
            x = 0
        if y > 600 or y < 0:
            print("y aar")
            y = 0
    x += xKoordinaat
    y += yKoordinaat
    pg.draw.rect(screen, color, (x, y, 50, 50))
    screen.blit(player2, (x, y))

    pg.display.update()