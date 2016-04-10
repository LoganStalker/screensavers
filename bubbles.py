# -*- coding:utf-8 -*-

from pygame import display, Surface, FULLSCREEN, draw,\
    event, KEYDOWN, K_ESCAPE, font, mouse
from pygame.time import Clock
from random import randint, random, gauss

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
        self.y = y+500
        self.color = (randint(50, 255), randint(50, 255), randint(50, 255))

    def update(self):
        self.y -= self.radius/2
        self.points = []
        self.radius += self.step_radius
        self.angle += self.step
        self.image = Surface((self.radius, self.radius))

    def blit(self, surface):
        self.update()
        draw.circle(surface, self.color, (int(self.x), int(self.y)), int(self.radius+2), 1)

font.init()
ff = font.Font(None, int(W/100*12.5))
lable_x_positions = (('PRESS', int(W / 100 * 34.6875)),
                     ('ESC', int(W / 100 * 40.625)),
                     ('FOR', int(W / 100 * 40.625)),
                     ('EXIT', int(W / 100 * 38.75)))
lable_start_y = int(W / 100 * 9.375)

mouse.set_visible(False)

square_list = []
timer = Clock()
done = True
while done:
    for e in event.get():
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                done = False

    screen.fill((30, 30, 70))

    # draw lables
    for lable in lable_x_positions:
        screen.blit(ff.render(lable[0], 1, (50, 50, 70)), (lable[1], lable_start_y * (lable_x_positions.index(lable) + 1)))

    if len(square_list) < 500:
        for i in range(randint(1, 5)):
            square_list.append(Round_square(int(gauss(W/2, W/3)), int(gauss(H/2, H/3))))

    for sq in square_list:
        sq.blit(screen)
        if sq.radius > 100:
            square_list.remove(sq)

    window.blit(screen, (0, 0))
    display.flip()
    timer.tick(60)