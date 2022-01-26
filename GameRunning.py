import pygame as pg
from colors import *
from time import sleep
pg.init ()

class Area (pg.sprite.Sprite):
    def __init__ (self, x, y, image, speed):
        super ().__init__ ()
        self.image = pg.transform.scale (pg.image.load (image), (100, 100))
        self.rect = self.image.get_rect ()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def reset (self):
        window.blit (self.image, (self.rect.x, self.rect.y))

class TextArea (Area):
    def move(self):
        key = pg.key.get_pressed ()
        if key[pg.K_LEFT] and self.rect.x >= 0:
            self.rect.x -= self.speed
        if key[pg.K_RIGHT] and self.rect.x <= 1700:
            self.rect.x += self.speed
        if key[pg.K_UP] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if key[pg.K_DOWN] and self.rect.y <= 600:
            self.rect.y += self.speed
class Enemy (Area):
    def move (self):
        if self.direction == "right":
            self.rect.x += self.speed
        if self.direction == "left":
            self.rect.x -= self.speed
        if self.rect.x >= 1700:
            self.direction = "left"
        if self.rect.x <= 0:
            self.direction = "right"

window = pg.display.set_mode ((1800, 700))
pg.display.set_caption ("Лабіринт")
my_profile = TextArea (0, 0, "object.png", 5)
x = 0
y = 0
enemy = Enemy (1500, 450, "enemy.png", 20)
enemy.direction = "left"
finish = Area (1600, 550, "finish.png", 0)
enemy.direction = "right"
clock = pg.time.Clock ()
'''mixer.music.load ("GameMusic2.ogg")
mixer.music.play ()'''
pg.mixer.music.load ("GameMusic.ogg")
pg.mixer.music.play ()
clock = pg.time.Clock ()
game = True
while game:
    window.fill ((Beige))
    my_profile.reset ()
    my_profile.move ()
    enemy.move ()
    enemy.reset ()
    finish.reset ()
    for e in pg.event.get ():
        if e.type == pg.QUIT:
            game = False
    pg.display.update ()
    clock.tick (60)