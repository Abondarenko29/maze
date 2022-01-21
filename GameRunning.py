import pygame as pg
from colors import *
pg.init ()
#mixer.init ()

class Area (pg.sprite):
    def __init__ (self, x, y, image, speed):
        super ().__init__ (self)
        self.image = pg.transform.scale (pg.image.load (image), (50, 50))
        self.rect = self.get_rect ()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def reset (self):
        window.blit (image, (self.rect.x, self.rect.y))

    def move_up (self):
        image.rect.y += self.speed
    def move_down (self):
        image.rect.y -= self.speed
    def move_right (self):
        image.rect.x += self.speed
    def move_left (self):
        image.rect.x -= self.speed

ImageName = "object.png"
window = pg.display.set_mode ((300, 250))
pg.display.set_caption ("Наздожиналки")
window.fill ((Beige))
MyProfile = Area (0, 0, ImageName, 10)
x = 0
y = 0
enemy = Area (0, 0, "enemy.jpg", 15)
'''mixer.music.load ("GameMusic2.ogg")
mixer.music.play ()'''
'''mixer.music.load ("GameMusic.ogg")
mixer.music.play ()'''
#window.blit (MyProfile, (x, y))
clock = pg.time.Clock ()
prapor = True
while prapor:
    for e in pg.event.get ():
        prapor = False
    pg.display.update ()
    clock.tick (60)
    for i in range (3):
        enemy.move_right ()
    for a in range (3):
        enemy.move_left ()

'''    if k_down and y <= 240:
        MyProfile.move_down ()

    if k_up and y >= 10:
        MyProfile.move_up ()

    if k_left and x >= 10:
        MyProfile.move_left ()

    if k_right and x <= 290:
        MyProfile.move_right'''