import pygame

pygame.init()

clock = pygame.time.Clock()
fps = 60

ekraani_laius = 1800
ekraani_korgus = 1050
ekraan = pygame.display.set_mode((ekraani_laius, ekraani_korgus))
pygame.display.set_caption('Parkuur')

# väärtused
ruudu_suurus = 50
mang_labi = 0
level = 1
main_menu = True
roosa = (255, 0, 125)
sinine = (0, 0, 255)
roheline = (0, 128, 0)
punane = (255, 0, 0)

# font
font = pygame.font.SysFont('Bauhaus 93', 50)
voidu_font = pygame.font.SysFont('Bauhaus93', 200)
timer_font = pygame.font.SysFont('Times New Roman', 50)

# pildid
lopp_img = pygame.image.load('lopp.png')
nrg_img = pygame.image.load('nrg.png')
hirm_img = pygame.image.load('hirm.png')
kast_img = pygame.image.load('kast.png')
mees_img = pygame.image.load('mees.png')
taser_img = pygame.image.load('taserrr.png')
tulnukas_img = pygame.image.load('tulnukas.png')
spike_img = pygame.image.load('spike.png')
flame_img = pygame.image.load('flame.png')
ice_img = pygame.image.load('ice.png')
uks_img = pygame.image.load('uks.png')
pro_mees = pygame.image.load('pro_mees.png')
kastu_img = pygame.image.load('kastu.png')

# sounds
pygame.mixer.music.load('muusika.wav')
pygame.mixer.music.play(-1, 0.0, 5000)
hype_sound = pygame.mixer.Sound('hype.wav')
hype_sound.set_volume(0.5)
surm_sound = pygame.mixer.Sound('surm.wav')
surm_sound.set_volume(0.5)
voit_sound = pygame.mixer.Sound('voit.wav')
voit_sound.set_volume(0.5)

# timer
minutid = 0
sekundid = 0
millisekundid = 0

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    ekraan.blit(img, (x, y))

def reset_level(level):
    player.reset(50, ekraani_korgus - 130)

    return world

class Player():
    def __init__(self, x, y):
        self.reset(x, y)

    def reset(self, x, y):
        self.images_right = []
        self.images_left = []
        self.index = 0
        self.counter = 0
        for num in range(1, 5):
            img_right = pygame.image.load(f'nookas{num}.png')
            img_right = pygame.transform.scale(img_right, (40, 80))
            img_left = pygame.transform.flip(img_right, True, False)
            self.images_right.append(img_right)
            self.images_left.append(img_left)
        self.dead_image = pygame.image.load('skull.png')
        self.image = self.images_right[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False
        self.direction = 0

    def update(self, mang_labi):
        dx = 0
        dy = 0
        walk_cooldown = 5

        if mang_labi == 0:
            # keypresses
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE] or key[pygame.K_w] and self.jumped == False:
                hype_sound.play()
                self.vel_y = -15
                self.jumped = True
            if key[pygame.K_SPACE] == False and key[pygame.K_w] == False:
                self.jumped = False
            if key[pygame.K_a]:
                dx -= 5
                self.counter += 1
                self.direction = -1
            if key[pygame.K_d]:
                dx += 5
                self.counter += 1
                self.direction = 1
            if key[pygame.K_a] == False and key[pygame.K_d] == False:
                self.counter = 0
                self.index = 0
                if self.direction == 1:
                    self.image = self.images_right[self.index]
                if self.direction == -1:
                    self.image = self.images_left[self.index]

            # animatsioon
            if self.counter > walk_cooldown:
                # counter vaatab viimast pilti
                self.counter = 0
                # index vaatab mitmenda pildi juures on
                self.index += 1
                if self.index >= len(self.images_right):
                    self.index = 0
                # 1, vaatab paremale
                if self.direction == 1:
                    self.image = self.images_right[self.index]
                # -1, vaatab vasakule
                if self.direction == -1:
                    self.image = self.images_left[self.index]

            # gravitatsioon
            self.vel_y += 1
            if self.vel_y > 10:
                self.vel_y = 10
            dy += self.vel_y

            # check for collision
            for ruut in world.tile_list:
                # check for collision ( x direction )
                # funktsioon kontrollib kas oleksid jargmisel framel ruudu sees, kui jah siis kiirendus = 0
                if ruut[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    dx = 0
                # check for collision ( y direction )
                if ruut[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    # check if below the ground ( jumping )
                    if self.vel_y < 0:
                        # tegelase ulemine ots ja ruudu alumine ots, tostab kohakuti need kaks
                        dy = ruut[1].bottom - self.rect.top
                        self.vel_y = 0
                    # check if above the ground ( falling )
                    elif self.vel_y >= 0:
                        # kui tegelane kukub ruudu sisse, siis ta jaab ruudu peale
                        dy = ruut[1].top - self.rect.bottom
                        self.vel_y = 0


           #asjadega kokkuporge
            if pygame.sprite.spritecollide(self, hirm_group, False):
                mang_labi = 2
                surm_sound.play()

            if pygame.sprite.spritecollide(self, mees_group, False):
                mang_labi = 2
                surm_sound.play()

            if pygame.sprite.spritecollide(self, taser_group, False):
                mang_labi = 2
                surm_sound.play()

            if pygame.sprite.spritecollide(self, spike_group, False):
                mang_labi = 2
                surm_sound.play()

            if pygame.sprite.spritecollide(self, flame_group, False):
                mang_labi = 2
                surm_sound.play()

            if pygame.sprite.spritecollide(self, ice_group, False):
                mang_labi = 2
                surm_sound.play()

            if pygame.sprite.spritecollide(self, tulnukas_group, False):
                mang_labi = 2
                surm_sound.play()

            if pygame.sprite.spritecollide(self, pro_mees_group, False):
                mang_labi = 1
                pygame.mixer.music.stop()
                voit_sound.play()

            # update player coordinates ( kiirendus )
            self.rect.x += dx
            self.rect.y += dy


        elif mang_labi == 2:
            self.image = self.dead_image
            if self.rect.y > 200:
                self.rect.y -= 10

        #player
        ekraan.blit(self.image, self.rect)

        return mang_labi


class World():
    def __init__(self, data):
        self.tile_list = []

        rida_count = 0
        for rida in data:
            col_count = 0
            for ruut in rida:
                if ruut == 1:
                    img = pygame.transform.scale(kast_img, (ruudu_suurus, ruudu_suurus))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * ruudu_suurus
                    img_rect.y = rida_count * ruudu_suurus
                    ruut = (img, img_rect)
                    self.tile_list.append(ruut)
                if ruut == 2:
                    img = pygame.transform.scale(kastu_img, (ruudu_suurus, ruudu_suurus))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * ruudu_suurus
                    img_rect.y = rida_count * ruudu_suurus
                    ruut = (img, img_rect)
                    self.tile_list.append(ruut)
                if ruut == 4:
                    mees = Mees(col_count * ruudu_suurus, rida_count * ruudu_suurus + 15)
                    mees_group.add(mees)
                if ruut == 6:
                    hirm = Hirm(col_count * ruudu_suurus, rida_count * ruudu_suurus + 15)
                    hirm_group.add(hirm)
                if ruut == 7:
                    taser = Taser(col_count * ruudu_suurus, rida_count * ruudu_suurus)
                    taser_group.add(taser)
                if ruut == 8:
                    spike = Spike(col_count * ruudu_suurus, rida_count * ruudu_suurus)
                    spike_group.add(spike)
                if ruut == 9:
                    flame = Flame(col_count * ruudu_suurus, rida_count * ruudu_suurus)
                    flame_group.add(flame)
                if ruut == 10:
                    ice = Ice(col_count * ruudu_suurus, rida_count * ruudu_suurus)
                    ice_group.add(ice)
                if ruut == 11:
                    tulnukas = Tulnukas(col_count * ruudu_suurus, rida_count * ruudu_suurus + 15)
                    tulnukas_group.add(tulnukas)
                if ruut == 12:
                    pro_mees = Pro_mees(col_count * ruudu_suurus, rida_count * ruudu_suurus)
                    pro_mees_group.add(pro_mees)

                col_count += 1
            rida_count += 1


    #lisab listist ruudud. ruut[0] on asukoht, ruut[1] on pilt
    def draw(self):
        for ruut in self.tile_list:
            ekraan.blit(ruut[0], ruut[1])



class Taser(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('taserrr.png')
        self.image = pygame.transform.scale(img, (ruudu_suurus, ruudu_suurus))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Spike(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('spike.png')
        self.image = pygame.transform.scale(img, (ruudu_suurus, ruudu_suurus))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Flame(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('flame.png')
        self.image = pygame.transform.scale(img, (ruudu_suurus, ruudu_suurus))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Ice(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('ice.png')
        self.image = pygame.transform.scale(img, (ruudu_suurus, ruudu_suurus))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Hirm(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('hirm.png').convert_alpha()
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0

    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 1
        if abs(self.move_counter) > 50:
            self.move_direction *= -1
            self.move_counter *= -1

class Mees(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('mees.png')
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0

    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 2
        if abs(self.move_counter) > 50:
            self.move_direction *= -1
            self.move_counter *= -1

class Tulnukas(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('tulnukas.png')
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0

    def update(self):
        self.rect.y += self.move_direction
        self.move_counter += 0.5
        if abs(self.move_counter) > 50:
            self.move_direction *= -1
            self.move_counter *= -1

class Pro_mees(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('pro_mees.png')
        self.image = pygame.transform.scale(img, (ruudu_suurus * 2, ruudu_suurus * 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

#map, igale numbrile vastab pilt
world_data = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 9, 2, 1, 3, 10, 0, 0, 0, 0, 8, 0, 0, 0, 8, 8, 0, 0, 0, 0, 8, 8, 8, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 12, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 11, 0, 0, 0, 7, 0, 0, 0, 0, 7, 0, 0, 0, 4, 0, 0, 1, 1, 7, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10, 0, 1],
    [1, 1, 8, 8, 0, 0, 0, 11, 1, 0, 0, 0, 0, 8, 8, 0, 9, 1, 0, 0, 11, 8, 0, 0, 0, 0, 0, 8, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 10, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 10, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 11, 0, 0, 0, 1, 0, 0, 0, 1, 7, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 10, 0, 0, 1, 0, 4, 0, 0, 0, 6, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 6, 0, 6, 0, 0, 0, 1, 0, 0, 0, 1, 7, 1],
    [1, 10, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 10, 0, 0, 0, 0, 0, 0, 9, 1, 11, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 8, 1, 1, 1, 8, 1, 1, 1, 1, 8, 8, 8, 11, 1],
    [1, 10, 0, 0, 0, 0, 0, 0, 9, 1, 0, 0, 0, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 0, 0, 0, 11, 0, 0, 0, 0, 0, 0, 9, 1],
    [1, 10, 1, 0, 0, 4, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 1],
    [1, 1, 1, 7, 1, 1, 1, 0, 0, 0, 0, 7, 1, 1, 1, 0, 0, 6, 0, 0, 7, 1, 1, 1, 7, 1, 1, 1, 7, 1, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 9, 2, 10, 0, 0, 0, 0, 0, 2, 10, 0, 0, 11, 0, 0, 0, 1, 0, 0, 0, 8, 0, 0, 0, 1, 0, 0, 0, 11, 0, 1],
    [1, 0, 0, 0, 0, 9, 2, 10, 0, 0, 0, 0, 0, 2, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 1, 1],
    [1, 0, 0, 2, 0, 0, 0, 0, 0, 9, 2, 10, 0, 0, 0, 0, 9, 2, 0, 1, 0, 0, 0, 1, 0, 0, 0, 7, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 2, 0, 0, 0, 0, 0, 9, 2, 10, 0, 0, 0, 0, 9, 2, 11, 1, 7, 7, 7, 1, 1, 1, 1, 1, 0, 0, 0, 4, 6, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

#mangija, tema asukoht.
player = Player(50, ekraani_korgus - 190)

#grupid. sprited voetakse gruppidesse kokku
hirm_group = pygame.sprite.Group()
mees_group = pygame.sprite.Group()
taser_group = pygame.sprite.Group()
spike_group = pygame.sprite.Group()
flame_group = pygame.sprite.Group()
ice_group = pygame.sprite.Group()
tulnukas_group = pygame.sprite.Group()
pro_mees_group = pygame.sprite.Group()


world = World(world_data)

run = True
while run:
    dt = clock.tick(fps)
    millisekundid += dt
    if millisekundid >= 1000:
        sekundid += 1
        millisekundid -= 1000
    if sekundid >= 60:
        minutid += 1
        sekundid -= 60

    ekraan.blit(nrg_img, (0, 0))
    ekraan.blit(lopp_img, (50, 50))
    ekraan.blit(uks_img, (50, 900))
    ekraan.blit(uks_img, (1700, 900))
    aeg = str(minutid) + ":" + str(sekundid) + ":" + str(round(millisekundid, 1))
    draw_text(aeg, timer_font, (255, 0, 0), 50, 50)

    # mangu algus, opetus, nupud
    if main_menu == True:
        ekraan.blit(nrg_img, (0, 0))
        draw_text('mängu õpetus:', font, roosa, 700, 200)
        draw_text('ara mine kollide ega takistuste vastu', font, punane, 700, 250)
        draw_text('nupud:', font, roosa, 250, 300)
        draw_text('q - mang kinni', font, sinine, 250, 400)
        draw_text('f - mangu alustamine', font, sinine, 250, 500)
        draw_text('r - mangu uuesti alustamine', font, sinine, 250, 600)
        draw_text('a - vasakule liikumine', font, roheline, 250, 700)
        draw_text('d - paremale liikumine', font, roheline, 250, 800)
        draw_text('space, w - huppamine', font, roheline, 250, 900)
        key = pygame.key.get_pressed()
        # vajutad q, siis mang laheb kinni
        if key[pygame.K_q] == True:
            run = False
        # vajutad f, siis mang laheb toole
        if key[pygame.K_f] == True:
            main_menu = False
    else:
        world.draw()
        # koik grupid joonistatakse ekraanile
        hirm_group.update()
        hirm_group.draw(ekraan)
        mees_group.update()
        mees_group.draw(ekraan)
        taser_group.update()
        taser_group.draw(ekraan)
        spike_group.update()
        spike_group.draw(ekraan)
        flame_group.update()
        flame_group.draw(ekraan)
        ice_group.update()
        ice_group.draw(ekraan)
        tulnukas_group.update()
        tulnukas_group.draw(ekraan)
        pro_mees_group.update()
        pro_mees_group.draw(ekraan)
        mang_labi = player.update(mang_labi)

    # mang_labi == 2 : tegelane saab surma.
    if mang_labi == 2:
        key = pygame.key.get_pressed()
        if key[pygame.K_r] == True:
            world_data = []
            world = reset_level(level)
            mang_labi = 0
            score = 0
    # mang_labi == 1 : tegelane joudis leveli lõppu ja võitis
    if mang_labi == 1:
        draw_text('võitja', voidu_font, roosa, 200, 400)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()