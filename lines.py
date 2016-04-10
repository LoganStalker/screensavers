# -*- coding:utf-8 -*-

import pygame
pygame.init()

# создаем окно
window = pygame.display.set_mode((1600, 900), pygame.FULLSCREEN)
pygame.display.set_caption('What is it?')
screen = pygame.Surface((1600, 900))

pygame.font.init()
ff = pygame.font.Font(None, 32)

# класс для создания объектов анимации
class Obj:
    def __init__(self, x, y, speed = 1,right = True): # задаем ему икс, игрек координаты и движение - True разрешает в право двигаться, False запрещает (значит будут двигаться в лево)
        self.x = x
        self.y = y
        self.image = pygame.Surface((1, 1))
        self.color = (10, 150, 10)
        self.right = right
        self.speed = speed

    def update_horizontal(self):    # в данном методе объект двигается по горизонтали
        if self.right == True:
            self.x += self.speed
            if self.x > 1580:
                self.right = False
        elif self.right == False:
            self.x -= self.speed
            if self.x < 10:
                self.right = True
    def update_vertical(self):  # в данном методе объект двигается по вертикали
        if self.right == True:
            self.y += self.speed
            if self.y > 880:
                self.right = False
        elif self.right == False:
            self.y -= self.speed
            if self.y < 10:
                self.right = True


    def draw(self, surf, type_update = 'h'):    # отображаем объект. type_update - указывает по какой оси двигать объекты.
        self.image.fill(self.color)
        if type_update == 'h':
            self.update_horizontal()
        if type_update == 'v':
            self.update_vertical()
        surf.blit(self.image, (self.x, self.y))

# ниже создаем объекты и помещаем в списки obj_list для горизонтально движущихся, obj_list2 для вертикально движущихся
obj_list = list()   # функция list() создает список. Это стандартная функция
obj_list2 = list()
speed = 1
for i in range(1, 46):
    obj = Obj(i*35, i*20, speed*1.5)
    obj_list.append(obj)

    obj = Obj(1580-(i*35), i*20, speed, False)
    obj_list.append(obj)

    obj = Obj(i*35, i*20, speed)
    obj_list2.append(obj)

    obj = Obj(i*35, 900-(i*20), speed, False)
    obj_list2.append(obj)
    #speed += 0.05

done = True
clock = pygame.time.get_ticks()
dt = 0
while done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                done = False
    
    screen.fill((10, 10, 10))

    # рисуем линии между каждыми двумя объектами списка. Если убрать 2 в строке "for i in range(1, len(obj_list)-1, 2):", то линии будут рисоваться между всеми объектами списка.
    for i in range(1, len(obj_list), 2):
        pygame.draw.line(screen, (150, 10, 10), (obj_list[i-1].x, obj_list[i-1].y), (obj_list[i].x, obj_list[i].y), 1)
        pygame.draw.line(screen, (10, 150, 10), (obj_list2[i-1].x, obj_list2[i-1].y), (obj_list2[i].x, obj_list2[i].y), 1)
    for i in range(1, len(obj_list)):
        if i%2 == 0:
            pygame.draw.line(screen, (150, 10, 10), (obj_list[i-2].x, obj_list[i-2].y), (obj_list[i].x, obj_list[i].y), 10)
            pygame.draw.line(screen, (10, 150, 10), (obj_list2[i-2].x, obj_list2[i-2].y), (obj_list2[i].x, obj_list2[i].y), 10)
        if i%2 != 0 and i > 2:
            pygame.draw.line(screen, (150, 10, 10), (obj_list[i-2].x, obj_list[i-2].y), (obj_list[i].x, obj_list[i].y), 10)
            pygame.draw.line(screen, (10, 150, 10), (obj_list2[i-2].x, obj_list2[i-2].y), (obj_list2[i].x, obj_list2[i].y), 10)


    if dt < 1000000:
        for i in range(len(obj_list)):
            obj_list[i].draw(screen, 'v')   # если поменять тут v на h
            obj_list2[i].draw(screen, 'h')   # а тут h на v, то получится другой рисунок.
    if dt > 1000000:
        for i in range(len(obj_list)):
            obj_list[i].draw(screen, 'h')   # если поменять тут v на h
            obj_list2[i].draw(screen, 'v')   # а тут h на v, то получится другой рисунок.
    if dt > 2000000:
        dt = 0

    #screen.blit(ff.render(str(dt), 1,(255, 255, 255)), (5, 5))

    window.blit(screen, (0, 0))
    pygame.display.flip()
    # ативируй таймер чтобы разглядеть подробнее получающийся рисунок =)
    dt += clock