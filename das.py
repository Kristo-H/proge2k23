import pygame
windowsize = (900,500)
win = pygame.display.set_mode(windowsize)

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 40)

pilt = pygame.image.load("pilt.JFIF")


def draw(pildiinfo):
    greenBackground = (0,255,0)
    win.fill(greenBackground)

    msg = myfont.render('Hello', False, (0,0,0))
    if frog.x > 700 and frog.y > 300:
        msg=myfont.render('You win', False, (255,0,0))
    win.blit(msg, (150, 50))
    win.blit(pilt, (0,0))
    pygame.display.update()


def main():
    pildiinfo = pygame.Rect(0,0,50,50)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
        keys=pygame.key.get_pressed()
        if keys[pygame.K_a]:
            pildiinfo.x -= 1
        draw(pildiinfo)
    pygame.quit()