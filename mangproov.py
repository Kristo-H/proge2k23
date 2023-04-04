import pygame


WIDTH, HEIGHT = 900, 500
win = pygame.display.setmode((WIDTH, HEIGHT))

def main():

    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        WIN.fill(WHITE)
        pygame.display.update()


    pygame.quit()

if __name__ == '__main__':
    main()


