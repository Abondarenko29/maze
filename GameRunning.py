import pygame as pg
from colors import *
pg.init ()

window = pg.display.set_mode ((300, 250))
window.fill ((Beige))
MyProfile = pg.transform.scale (pg.image.load ("object.png"), (50, 50))
x = 0
y = 0
window.blit (MyProfile, (x, y))
clock = pg.time.Clock ()

while True:
    pg.display.update ()
    clock.tick (120)

for event in pg.event.get ():
    if event.type == QUIT:
        game = False

check = pg.key.get_pressed ()

if check [K_DOWN] and y <= 240:
    MyProfile.rect.y += 10

if check [K_UP] and y >= 10:
    MyProfile.rect.y -= 10

if check [K_LEFT] and x >= 10:
    MyProfile.rect.x -= 10

if check [K_RIGHT] and x <= 290:
    MyProfile.rect.x += 10