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
    def dieth (self, x, y):
        self.rect.x = 0
        self.rect.y = 0

class Label (Area):
    def move (self):
        if self.direction == "right":
            self.rect.x += self.speed
        if self.direction == "left":
            self.rect.x -= self.speed
        if self.rect.x >= 1700:
            self.direction = "left"
        if self.rect.x <= 0:
            self.direction = "right"

class Wall (pg.sprite.Sprite):
    def __init__ (self, x, y, H, V, color):
        super ().__init__ ()
        self.wall = pg.Surface ((H, V))
        self.rect = self.wall.get_rect ()
        self.rect.x = x
        self.rect.y = y
        self.wall.fill ((color))
    def draw_wall (self):
        window.blit (self.wall, (self.rect.x, self.rect.y))

def located_wall ():
    wall1 = Wall (100, 0, 5, 450, Lime)
    wall2 = Wall (100, 450, 200, 5, Lime)
    wall3 = Wall (300, 305, 5, 150, Lime)
    wall4 = Wall (300, 300, 100, 5, Lime)
    wall5 = Wall (400, 300, 5, 150, Lime)
    wall6 = Wall (400, 450, 200, 5, Lime)
    wall7 = Wall (600, 305, 5, 150, Lime)
    wall8 = Wall (600, 305, 100, 5, Lime)
    wall9 = Wall (700, 305, 5, 150, Lime)
    wall10 = Wall (700, 450, 200, 5, Lime)
    wall11 = Wall (900, 305, 5, 150, Lime)
    wall12 = Wall (900, 305, 100, 5, Lime)
    wall13 = Wall (1000, 305, 5, 150, Lime)
    wall14 = Wall (1000, 450, 200, 5, Lime)
    wall15 = Wall (1200, 305, 5, 150, Lime)
    wall16 = Wall (1200, 305, 100, 5, Lime)
    wall17 = Wall (1300, 305, 5, 150, Lime)
    wall18 = Wall (1300, 555, 5, 195, Lime)
    wall19 = Wall (1300, 695, 200, 5, Lime)
    wall20 = Wall (1400, 450, 5, 150, Lime)
    wall21 = Wall (1500, 600, 5, 150, Lime)
    wall22 = Wall (1300, 450, 500, 5, Lime)
    wall000 = Wall (0, 550, 1305, 5, Lime)
    wall1.draw_wall ()
    wall2.draw_wall ()
    wall3.draw_wall ()
    wall4.draw_wall ()
    wall5.draw_wall ()
    wall6.draw_wall ()
    wall7.draw_wall ()
    wall8.draw_wall ()
    wall9.draw_wall ()
    wall10.draw_wall ()
    wall11.draw_wall ()
    wall12.draw_wall ()
    wall13.draw_wall ()
    wall14.draw_wall ()
    wall15.draw_wall ()
    wall16.draw_wall ()
    wall17.draw_wall ()
    wall18.draw_wall ()
    wall19.draw_wall ()
    wall20.draw_wall ()
    wall21.draw_wall ()
    wall22.draw_wall ()
    wall000.draw_wall ()
    wallsDown = [wall000]
    wallsUp = [wall2, wall4, wall6, wall8, wall10, wall12, wall14, wall16, wall22]
    wallsRight = [wall1, wall5, wall9, wall13, wall17, wall21]
    wallsLeft = [wall3, wall7, wall11, wall15]
    for v in wallsDown:
        if pg.sprite.collide_rect (my_profile, v):
            my_profile.rect.y -= my_profile.speed
    for q in wallsUp:
        if pg.sprite.collide_rect (my_profile, q):
            my_profile.rect.y += my_profile.speed
    for u in wallsRight:
        if pg.sprite.collide_rect (my_profile, u):
            my_profile.rect.x -= my_profile.speed
    for i in wallsLeft:
        if pg.sprite.collide_rect (my_profile, i) and my_profile.rect.y < 350:
            my_profile.rect.x += my_profile.speed
    if pg.sprite.collide_rect (my_profile, wall20):
        if my_profile.rect.x < 1350:
            my_profile.rect.x -= my_profile.speed
        elif my_profile.rect.x > 1350:
            my_profile.rect.x += my_profile.speed
    if pg.sprite.collide_rect (my_profile, wall18):
        my_profile.rect.x += my_profile.speed

window = pg.display.set_mode ((1800, 700))
pg.display.set_caption ("Лабіринт")
my_profile = TextArea (0, 0, "object.png", 2)
x = 0
y = 0
enemy = Label (1500, 450, "enemy.png", 2)
enemy2 = Label (200, 450, "enemy.png", 2)
enemy.direction = "left"
enemy2.direction = "right"
finish = Area (1600, 550, "finish.png", 0)
clock = pg.time.Clock ()
'''mixer.music.load ("GameMusic2.ogg")
mixer.music.play ()'''
pg.mixer.music.load ("GameMusic.ogg")
pg.mixer.music.play ()
clock = pg.time.Clock ()
a = 3
game = True
finish_effect = pg.mixer.Sound ("finish.ogg")
die = pg.mixer.Sound ("die.ogg")
finishP = False
while game:
    for e in pg.event.get ():
        if e.type == pg.QUIT:
            game = False
    if finishP != True:
        window.fill ((Beige))
        my_profile.reset ()
        my_profile.move ()
        enemy.move ()
        enemy2.move ()
        enemy2.reset ()
        enemy.reset ()
        located_wall ()
        finish.reset ()
        if pg.sprite.collide_rect (my_profile, finish):
            finish_effect.play ()
            window.fill ((Yellow))
            font = pg.font.Font (None, 300)
            text = font.render ("Перемога ваша!", True, (Purple))
            window.blit (text, (100, 250))
            finishP = True
        if a > 0 and pg.sprite.collide_rect (my_profile, enemy):
            die.play ()
            a -= 1
            my_profile.dieth (0, 0)
        if a > 0 and pg.sprite.collide_rect (my_profile, enemy2):
            die.play ()
            a -= 1
            my_profile.dieth (0, 0)
        if a <= 0:
            window.fill ((Grey))
            font = pg.font.Font (None, 300)
            text = font.render ("Ви програли!", True, (Red))
            window.blit (text, (100, 250))
            finishP = True
        pg.display.update ()
        clock.tick (120)