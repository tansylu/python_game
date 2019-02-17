from random import randint
import pygame
import os
import random
# импорт необходимых модулей

pygame.init()
pygame.time.set_timer(pygame.USEREVENT, 3000)
screen = pygame.display.set_mode((1000, 1000))
image = pygame.image.load(os.path.join('data', 'back.jpg'))
screen.blit(image, [0, 0])
# инициализация поля

bomb = pygame.image.load(os.path.join('data', 'bomb.png')).convert_alpha()
heart = pygame.image.load(os.path.join('data', 'heart.png'))
gameover = pygame.image.load(os.path.join('data', 'death.jpg'))
# загрузка необходимых изображений

back = pygame.mixer.Sound('back.wav')
back.play(-1)
final = pygame.mixer.Sound('final.wav')
boom = pygame.mixer.Sound('boom.wav')
sound = pygame.mixer.Sound('action.wav')
# добавление звука 

def plays(ok, h):
    global q
    if not ok and q:
        back.stop()
        final.play(0)
        q = False
       
 
n, h, j, c, d, q = 0, 5, 8, 8, 15, True
# очки и скорость

ok = True
BOYS = ('boy.jpg','boy1.jpg', 'boy2.jpg', 'boy3.jpg')
BOYS_SURF = []  
for i in range(len(BOYS)):
    BOYS_SURF.append(pygame.image.load(os.path.join('data', BOYS[i])).convert_alpha())
heart = pygame.image.load(os.path.join('data', 'heart.png'))
# загрузка необходимых изображений
    
class Particle(pygame.sprite.Sprite):
    fire = [heart]
    for scale in (5, 10, 20):
        fire.append(pygame.transform.scale(fire[0], (scale, scale)))
 
    def __init__(self, pos, dx, dy):
        super().__init__(all_sprites)
        self.image = random.choice(self.fire)
        self.rect = self.image.get_rect()
        self.velocity = [dx, dy]
        self.rect.x, self.rect.y = pos
        self.gravity = 1
 
    def update(self):
        self.velocity[1] += self.gravity
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        if not self.rect.colliderect([0,0,1000,1000]):
            self.kill()
        # класс частиц
class Boy(pygame.sprite.Sprite):
    def __init__(self, x, surf, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(center=(x, 0))
        self.add(group)  
        self.speed = randint(2, 15)  
        # инициализация класса спрайтов
    def update(self):
        if self.rect.y < 1000:
            self.rect.y += self.speed
        else:
            self.kill()
        # функция, удаляющая спрайт за пределами поля
class Bomb(pygame.sprite.Sprite):
    def __init__(self, x, surf, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(center=(x, 0))
        self.add(group)  
        self.speed = randint(5, 8)  
 
    def update(self):
        if self.rect.y < 1000:
            self.rect.y += self.speed
        else:
            self.kill()
            # класс бомб

boys = pygame.sprite.Group() # создание группы
bombs = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
Bomb(randint(50, 900), bomb, bombs)# первая картинка
count = 1
def create_particles(position):
        particle_count = 20
        numbers = range(-15, 15)
        for _ in range(particle_count):
            Particle(position, random.choice(numbers), random.choice(numbers))
            # создание частиц 
def love(boys, pos):
        global n, h, j, c, d, ok,  image, gameover
        for b in boys:
            if b.rect.collidepoint(pos):
                sound.play()
                b.image = heart
                n += 1
                h += 2
                j += 2
            else:
                ok = False
                image = gameover # завершение игры при нажатии не на картинку
        for b in bombs:
            if b.rect.collidepoint(pos):
                boom.play()
                b.kill()
                n += 10
                c += 2
                d += 2
                Bomb.create_particles(pos)
            else:
                ok = False
                image = gameover # завершение игры при нажатии не на картинку
        # замена изображения парня изображением сердца при нажатии
def score(n):
    font = pygame.font.SysFont( 'couriernew', 25)
    text = font.render("Caught: "+str(n), True, (0, 0, 0))
    sp = font.render("Boys_Speed: "+str(h)+'-'+str(j), True, (0, 0, 0))
    spb = font.render("Bombs_Speed: "+str(c)+'-'+str(d), True, (0, 0, 0))
    if ok:
        screen.blit(text,(0,0))
        screen.blit(sp,(0,25))
        screen.blit(spb,(0,50))
    else:
        font = pygame.font.SysFont( 'couriernew', 50)
        text = font.render("Record: "+str(n), True, (238, 8, 8))
        screen.blit(text,(0,0))
    # вывод очков и скорости

while 1: # игровой цикл
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            # завершение
        elif event.type == pygame.USEREVENT:
            if count%randint(1, 8) != 0:
                Boy(randint(50, 900), BOYS_SURF[randint(0, 2)], boys)
            else:
                Bomb(randint(50, 900), bomb, bombs)
            count+=1
            # появление спрайтов
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            love(boys, pos)
            # нажатие мышью
        plays(ok, q)
     if not ok:
        final.play()
     screen.blit(image, [0, 0])
     score(n)
     bombs.draw(screen)
     boys.draw(screen)
     all_sprites.draw(screen)# отрисовка спрайтов
     pygame.display.update()# обновление поля
     pygame.time.delay(10)
     bombs.update()
     boys.update() 
     all_sprites.update()# обновление групп
