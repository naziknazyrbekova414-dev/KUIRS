import pygame
import sys


pygame.init()
s=w, h=800, 600
color =14, 150, 114
zoro=pygame.image.load('boll.jpg')
zoro=pygame.transform.scale(zoro, (100, 100))
z=zoro.get_rect()
z.x=0
z.y=0
speed=[1,1]
screen=pygame.display.set_mode(s)
while True:
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            sys.exit()
    z=z.move(speed)
    if z.right>w or z.left<0:0
        speed[0]=-speed[0]
    if z.bottom>h or z.top<0:
        speed[1]=-speed[1]


    screen.fill(color)
    screen.blit(zoro,z)
    pygame.display.flip()