from random import randint
import pygame
import os
# импорт необходимых модулей

pygame.init()
pygame.time.set_timer(pygame.USEREVENT, 3000)
screen = pygame.display.set_mode((1000, 1000))
image = pygame.image.load(os.path.join('data', 'back.jpg'))
screen.blit(image, [0, 0])
# инициализация поля 
    
BOYS = ('boy.jpg','boy1.jpg', 'boy2.jpg', 'boy3.jpg')
BOYS_SURF = []  
for i in range(len(BOYS)):
    BOYS_SURF.append(pygame.image.load(os.path.join('data', BOYS[i])).convert_alpha())
heart = pygame.image.load(os.path.join('data', 'heart.png'))
# загрузка необходимых изображений
    
    
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
    def love(boys, pos):
        for b in boys:
            if b.rect.collidepoint(pos):
                b.image = heart
        # замена изображения парня изображением сердца при нажатии
        
boys = pygame.sprite.Group() # создание группы

Boy(randint(1, 900), BOYS_SURF[randint(0, 2)], boys) # первая картинка

while 1: # игровой цикл
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            # завершение
        elif event.type == pygame.USEREVENT:
            Boy(randint(1, 900), BOYS_SURF[randint(0, 2)], boys)
            # появление спрайтов
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            Boy.love(boys, pos)
            # нажатие мышью
    
    screen.blit(image, [0, 0]) 
    boys.draw(screen) # отрисовка спрайтов
    pygame.display.update()# обновление поля
    pygame.time.delay(10)
    boys.update() # обновление группы
