#IMPORTANT NOTEE
#I have no idea if this could crash your pc but if it can tell me afterwords how it went for you lmao
#do it at your own risk though, this is just some balls (kinda) bouncing arround a screen afterwords

import pygame as py
from random import *
import sys

py.init()

screenSize = 1000
clock = py.time.Clock()
canvas = py.display.set_mode((screenSize, screenSize))
colors = [(154, 42, 203), (76, 231, 182), (18, 96, 159), (101, 255, 31), (90, 187, 175), (204, 27, 114), (232, 69, 217), (238, 142, 10), (162, 228, 236), (244, 29, 199)]
obj_group = py.sprite.Group()

class Ball(py.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.x = x
        self.y = y
        self.image = py.Surface((20, 20))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.yvel = 1
        self.xvel = randint(6, 15)

    def update(self):
        self.yvel += 1
        self.rect.y += self.yvel

        self.rect.x += self.xvel
        self.checkCollision()

    def checkCollision(self):
        if self.rect.y >= screenSize - 50:
            self.yvel = 0
            self.yvel -= 35
            obj_group.add(Ball(randint(0, screenSize - 50), randint(0, screenSize - 50), choice(colors)))
        if self.rect.x >= screenSize - 50 or self.rect.x < 0: 
            self.xvel *= -1
            obj_group.add(Ball(randint(0, screenSize - 50), randint(0, screenSize - 50), choice(colors)))


obj_group.add(Ball(randint(0, screenSize - 50), randint(0, screenSize - 50), choice(colors)))

while True:
    canvas.fill((30, 30, 30))

    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()
    
    obj_group.update()
    obj_group.draw(canvas)

    py.display.flip()


    clock.tick(60)
