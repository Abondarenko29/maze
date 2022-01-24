import pygame as pg
from colors import *
from time import sleep
pg.init ()

class Area (pg.sprite.Sprite):
    def __init__ (self, x, y, image, speed):
        super ().__init__ ()
        self.image = pg.transform.scale (pg.image.load (image), (150, 150))
        self.rect = self.image.get_rect ()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def reset (self):
        window.blit (self.image, (self.rect.x, self.rect.y))

    def move_up (self):
        window.fill ((Beige))
        self.rect.y -= self.speed
        window.blit (self.image, (self.rect.x, self.rect.y))
    def move_down (self):
        window.fill ((Beige))
        self.rect.y += self.speed
        window.blit (self.image, (self.rect.x, self.rect.y))
    def move_right (self):
        window.fill ((Beige))
        self.rect.x += self.speed
        window.blit (self.image, (self.rect.x, self.rect.y))
    def move_left (self):
        window.fill ((Beige))
        self.rect.x -= self.speed
        window.blit (self.image, (self.rect.x, self.rect.y))

window = pg.display.set_mode ((1800, 700))
pg.display.set_caption ("Доганялки")
my_profile = Area (0, 0, "object.png", 10)
x = 0
y = 0
enemy = Area (1300, 350, "enemy.png", 15)
finish = Area (1600, 550, "finish.png", 0)
'''mixer.music.load ("GameMusic2.ogg")
mixer.music.play ()'''
pg.mixer.music.load ("GameMusic.ogg")
pg.mixer.music.play ()
clock = pg.time.Clock ()
charge = pg.key.get_pressed ()
game = True
while game:
    window.fill ((Beige))
    my_profile.reset ()
    enemy.reset ()
    finish.reset ()
    for e in pg.event.get():
        if e.type == pg.QUIT:
            game = False
    pg.display.update ()
    clock.tick (60)
    for i in range (3):
        enemy.move_right ()
    for a in range (3):
        enemy.move_left ()

    if charge[pg.K_DOWN] and y <= 690:
        my_profile.move_down ()

    if charge[pg.K_UP] and y >= 10:
        my_profile.move_up ()

    if charge[pg.K_LEFT] and x >= 10:
        my_profile.move_left ()

    if charge[pg.K_RIGHT] and x <= 1790:
        my_profile.move_right ()