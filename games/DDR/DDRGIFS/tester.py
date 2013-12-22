import pygame
from pygame.locals import *
import sys
import time
import pyganim

pygame.init()

windowSurface = pygame.display.set_mode((1280,720), 0, 32)

dancerguy = pyganim.PygAnimation([('TWERK/twerk1.png', 0.1),
                                  ('TWERK/twerk2.png', 0.1),
                                  ('TWERK/twerk3.png', 0.1),
                                  ('TWERK/twerk4.png', 0.1),
                                  ('TWERK/twerk5.png', 0.1),
                                  ('TWERK/twerk6.png', 0.1)])
                                 
dancerguy.play()

mainClock = pygame.time.Clock()
BackgroundColor = (255,255,255)
while True:
    windowSurface.fill(BackgroundColor)
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and event.key == K_l:
            dancerguy.loop = False

    dancerguy.blit(windowSurface, (100, 50))

    pygame.display.update()
    mainClock.tick(30)
