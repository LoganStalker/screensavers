# -*- coding:utf-8 -*-
__author__ = 'veles'

from pygame import display, Surface, draw, KEYDOWN, K_ESCAPE,\
    event, time, FULLSCREEN, NOFRAME, font, mouse
import sys
from math import sin, cos, pi

window = display.set_mode((0, 0), FULLSCREEN|NOFRAME)
SIZE = window.get_size()
screen = Surface(SIZE)

def drawing(pos=[0, 0], angle=0, line_size=0):
    draw.aaline(screen, (0, 255, 0), pos, (sin(angle+120*(pi/180))*line_size+pos[0],
                                            cos(angle+120*(pi/180))*line_size+pos[1]), 1)
    draw.aaline(screen, (0, 255, 0), pos, (sin(angle+240*(pi/180))*line_size+pos[0],
                                            cos(angle+240*(pi/180))*line_size+pos[1]), 1)
    draw.aaline(screen, (0, 255, 0), pos, (sin(angle+0*(pi/180))*line_size+pos[0],
                                            cos(angle+0*(pi/180))*line_size+pos[1]), 1)

font.init()
ff = font.Font(None, int(SIZE[0]/100*12.5))

figure_line_size = SIZE[0]/100*3.125

angle = 0 # angle of rotation
start_rows_even = SIZE[0]/100*0.1875 # start position for even rows
start_rows_uneven = SIZE[0]/100*2.8125 # start position for uneven rows
start_cols = SIZE[0]/100*1.625 # start position for cols
step_rows = SIZE[0]/100*5.3125 # rows shift
step_cols = SIZE[0]/100*4.6875 # columns shift
pos = [start_rows_uneven, start_cols]

rows = int(SIZE[1]/((SIZE[0]/100*3.125)*1.5))+1 # number of rows
cols = int(SIZE[0]/((SIZE[0]/100*3.125)*1.5))+1 # number of columns

# list x coords for lable words
lable_x_positions = (('PRESS', int(SIZE[0] / 100 * 34.6875)),
                     ('ESC', int(SIZE[0] / 100 * 40.625)),
                    ('FOR', int(SIZE[0] / 100 * 40.625)),
                    ('EXIT', int(SIZE[0] / 100 * 38.75)))
lable_start_y = int(SIZE[0] / 100 * 9.375)

mouse.set_visible(False) # set invisible for mouse cursor

while 1:
    for e in event.get():
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                sys.exit()

    screen.fill((40, 40, 40))

    # draw lables
    for lable in lable_x_positions:
        screen.blit(ff.render(lable[0], 1, (55, 55, 55)), (lable[1], lable_start_y*(lable_x_positions.index(lable)+1)))

    # rotation
    if angle > 1.04 and angle < 1.05:
        time.delay(2000)
    elif angle > 2.09 and angle < 2.10:
        time.delay(2000)
        angle = 0
    angle += 0.01

    # drawing
    pos[1] = start_cols
    for i in range(rows):
        if (i+1) % 2 == 0: # if row is even
            pos[0] = start_rows_even
        else:
            pos[0] = start_rows_uneven
        for _ in range(cols):
            drawing(pos, angle, figure_line_size)
            pos[0] += step_rows
        pos[1] += step_cols

    # bliting on window
    window.blit(screen, (0, 0))
    display.flip()