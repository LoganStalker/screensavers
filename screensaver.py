# -*- coding:utf-8 -*-

from pygame import display, Surface, FULLSCREEN, draw,\
    event, KEYDOWN, K_ESCAPE, font, mouse
from pygame.time import Clock
from math import sin, cos
from random import randint, random, choice

window = display.set_mode((0, 0), FULLSCREEN)
W = window.get_width()
H = window.get_height()
screen = Surface((W, H))

class Round_square(object):
    def __init__(self, x = 0, y = 0):
        self.radius = 0
        self.step_radius = random()
        self.points = []
        self.step = random()/10
        self.angle = 0
        self.x = x
        self.y = y
        self.color = (randint(50, 255), randint(50, 255), randint(50, 255))
        self.num_angles = choice([3,4,5,6,7,8,30])

    def update(self):
        self.points = []
        self.radius += self.step_radius
        self.angle += self.step
        v = 0
        for i in range(self.num_angles):
            self.points.append((cos(self.angle+v)*self.radius+self.x, sin(self.angle+v)*self.radius+self.y))
            v += 6.28/self.num_angles

    def blit(self, surface):
        self.update()
        draw.aalines(surface, self.color, 1, self.points, 1)

mouse.set_visible(False)

font.init()
ff = font.Font(None, int(W/100*12.5))
lable_x_positions = (('PRESS', int(W / 100 * 34.6875)),
                     ('ESC', int(W / 100 * 40.625)),
                     ('FOR', int(W / 100 * 40.625)),
                     ('EXIT', int(W / 100 * 38.75)))
lable_start_y = int(W / 100 * 9.375)

square_list = []
done = True
timer = Clock()
while done:
    for e in event.get():
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                done = False

    screen.fill((30, 30, 50))

    # draw lables
    for lable in lable_x_positions:
        screen.blit(ff.render(lable[0], 1, (40, 40, 70)), (lable[1], lable_start_y * (lable_x_positions.index(lable) + 1)))

    if len(square_list) < 500:
        for i in range(randint(1, 5)):
            square_list.append(Round_square(randint(0, W), randint(0, H)))

    for sq in square_list:
        if sq.radius >= 50:
            square_list.remove(sq)
        else:
            sq.blit(screen)

    window.blit(screen, (0, 0))
    display.flip()
    timer.tick(60)