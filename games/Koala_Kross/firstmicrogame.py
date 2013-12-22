import pygame, pygame.mixer
import pygame
from pygame import Surface
from pygame.image import load
from pygame.locals import *
from pygame.mixer import music
from pygame.rect import Rect
from pygame.sprite import Group, Sprite
from pygame.color import Color
from random import randint, choice

import locals 
from microgame import Microgame

def make_game():
    return KoalaKross()

def title():
    return 'Koala Kross'

def thumbnail():
    pass
def hint():
    return 'Save the koala, avoid the pandas, and eat the bread!!!'

def _load_image(name, x, y):
    '''
    Loads an image file, returning the surface and rectangle corresponding to
    that image at the given location.
    '''
    try:
        image = load(name)
        if image.get_alpha is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except pygame.error, msg:
        print 'Cannot load image: {}'.format(name)
        raise SystemExit, msg
    rect = image.get_rect().move(x, y)
    return image, rect

class Koala(Sprite):
    def __init__(self,game):
        Sprite.__init__(self)
        self.image=pygame.image.load('')
        self.rect=self.image.get_rect()
        self.velocity=(0,0)
##        self.area=game.rect
##        self.game=game
        
        
    

    def update(self):
        self.rect.x+=self.velocity[0]
        self.rect.x+=self.velocity[1]
        if not self.area.contains(self.rect):
            tl= not self.area.collidepoint(rect.topleft)
            tr= not self.area.collidepoint(rect.topright)
            bl= not self.area.collidepoint(rect.bottomleft)
            br = not self.area.collidepoint(rect.bottomright)
            if tl and tr or bl and br:
                self.game.lose()
                font.render('You just killed the koala #killyourself !')
                textpos = text.get_rect()
                textpos.centerx = background.get_rect().centerx
                background.blit(text, textpos)
            if tl and bl:
                self.game.lose()
                font.render("Don't kill the koalas! They're endangered!")
                textpos = text.get_rect()
            textpos.centerx = background.get_rect().centerx
            background.blit(text, textpos)
##pygame.init()
##surface=pygame.display.set_mode((1024,768))
##surface.fill(Color(0,0,200))
#make sure code handles mutually exclusve cases 

class Panda(Sprite):
    def __init__self(self,game,x,y,vx,vy):
        Sprite.__init__(self)
        self.image=_load_image('games/Koala_Kross/koala.png', x, y)
        self.image, self.rect = _load_image('',x,y)
        
        self.vx=vx
        self.vy=vy
        self.area=game.rect
        self.game=game
        
    def update(self):
        rect=self.rect.move(0,30)
        if not self.area.contains(self.rect):
            tl= not self.area.collidepoint(rect.topleft)
            tr= not self.area.collidepoint(rect.topright)
            bl= not self.area.collidepoint(rect.bottomleft)
            br = not self.area.collidepoint(rect.bottomright)
            if tl and tr or bl and blr:
                self.vy = -self.vy
            rect=self.rect.move(self.vx,self.vy)
        elif self.rect.colliderect(self.koala):
            font.render("Sorry! Koalas are deathly allergic to pandas.  You lose!")
            textpos = text.get_rect()
            textpos.centerx = background.get_rect().centerx
            background.blit(text, textpos)
            self.lose()
        else:
            self.rect=self.rect

class Bread(Sprite):
    
    def __init__(self,x,y):
        Sprite.__init__(self)
        self.image=pygame.image.load('koala.jpg')
        self.rect=rect((950,150))


    def update(self):
        rect=self.rect.move(0,0)
        if self.rect.colliderect(self.koala):
            self.game.win()
            font.render('Congrats! You have appropriately noursished this previously starving koala.')
            textpos = text.get_rect()
            textpos.centerx = background.get_rect().centerx
            background.blit(text, textpos)
            

class KoalaKross(Microgame):
    
    
    def __init__(self):
        Microgame.__init__(self)
        self.rect= Rect(0,0, locals.WIDTH, locals.HEIGHT)
##        surface=pygame.display.set_mode((1024,768))
##        surface.fill(Color(0,0,250))
        koala=Koala(self)
        self.panda1=Panda(200,100,0,2)
        self.panda2=Panda(500,100,0,2)
        self.bread=Bread(self)
        self.sprites=Group((koala,self.panda1,self.panda2,self.panda3))
        self.clock=pygame.time.Clock()

    def start():
        pass

    def stop():
        pass 

    def update(self):
        time=pygame.time.get_ticks()
        self.sprites.update()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key==K_DOWN:
                    koala.velocity=(0,-3)
                elif event.key==K_UP:
                    koala.velocity=(3,0)
                elif event.key == K_Right:
                    koala.velocity=(3,0)
                elif event.key == K_Left:
                    koala.velocity=(-3,0)
                elif event.key == K_q:
                    self.lose()
            elif event.type == KEYUP:
                koala.velocity=(0,0)

    def render (self, surface):
##        Surface=display.set_mode((1024,768))
        surface.fill.Color(0,0,0)
        self.sprites.draw(surface)
##        Surface=_load_image(,1024,768)


##running=True
##while running:
##    return KoalaKross()
##    if KoalaKross==self.game.win():
##        running = False
##    elif KoalaKross==self.game.lose():
##        running = False
##pygame.quit()
#what is the use of the clock? Clock updates the screen every _ ms, fast enough to make movement unnoticable. flip function? recflects changes onto the panel; makes it faster to load.
                
                #self.game check that out
                

#pygame.transform.smoothscale            
        
# in example how is the game started , and how big surface is
#pandas shouting shit
