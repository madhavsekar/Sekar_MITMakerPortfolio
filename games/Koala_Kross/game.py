import pygame, pygame.mixer
import pygame
from pygame import Surface
from pygame.image import load
from pygame.locals import *
from pygame.mixer import music
from pygame.rect import Rect
from pygame.sprite import Group, Sprite, OrderedUpdates
from pygame.color import Color
from random import randint, choice
from pygame.font import Font
from os.path import join 

import locals 
from microgame import Microgame

def make_game():
    return KoalaKross()

def title():
    return 'Koala Kross'

def thumbnail():
    return  'games/Koala_Kross/koalakross.png'

def hint():
    return 'Save the koala, avoid the pandas, and eat the bread!!!'
#winscreen #losescreen
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
        self.image=pygame.image.load(join('games','Koala_Kross','koala.png'))
        self.rect=self.image.get_rect()
        self.velocity=(0,0)
        self.area=game.rect
        self.game=game

        

    def update(self):
        self.rect.x+=self.velocity[0]
        self.rect.y+=self.velocity[1]
        if not self.area.contains(self.rect):
            tl= not self.area.collidepoint(self.rect.topleft)
            tr= not self.area.collidepoint(self.rect.topright)
            bl= not self.area.collidepoint(self.rect.bottomleft)
            br = not self.area.collidepoint(self.rect.bottomright)
            if tl and tr or bl and br:
                self.game.lose()
##                font = pygame.font.Font(None, 36)
##                text = font.render("Hello There", 1, (10, 10, 10))
##                textpos = text.get_rect()
##                textpos.centerx = surface.get_rect().centerx
##                surface.blit(text, textpos)
            if tl and bl:
                self.game.lose()
##                font.render("Don't kill the koalas! They're endangered!")
##                textpos = text.get_rect()
##                textpos.centerx = background.get_rect().centerx
##                background.blit(text, textpos)
##pygame.init()
##surface=pygame.display.set_mode((1024,768))
##surface.fill(Color(0,0,200))
#make sure code handles mutually exclusve cases 

class Panda(Sprite):
    
    def __init__(self,game,x,y,vx,vy):
        Sprite.__init__(self)
        self.image, self.rect=_load_image(join('games','Koala_Kross','panda.png'), x, y)
##        self.image=pygame.image.load(join('games','Koala_Kross','panda.png'))
##        self.rect=(x,y,self.image.get_rect())
        self.vx=vx
        self.vy=vy
        self.area=game.rect
        self.game=game
        
        
    def update(self):
        self.rect=self.rect.move(self.vx,self.vy)
####        self.rect=self.rect.move(self.vx,30)
##        self.rect.x=self.rect.x
##        self.rect.y=self.rect.y+30
##        self.vy=self.vy+30
        if not self.area.contains(self.rect):
            tl= not self.area.collidepoint(self.rect.topleft)
            tr= not self.area.collidepoint(self.rect.topright)
            bl= not self.area.collidepoint(self.rect.bottomleft)
            br = not self.area.collidepoint(self.rect.bottomright)
            if tl and tr or bl and br:
                self.vy = -self.vy
            rect=self.rect.move(self.vx,self.vy)
            if tl and bl or tr and br:
                self.vx = -self.vx
            rect=self.rect.move(self.vx,self.vy)
        elif self.rect.colliderect(self.game.koala.rect):
##            font.Font.render("Sorry! Koalas are deathly allergic to pandas.  You lose!")
##            textpos = text.get_rect()
##            textpos.centerx = surface.get_rect().centerx
##            surface.blit(text, textpos)
    
            self.game.lose()
##            font=pygame.font.Font(None,30)
##            self.surface=
            
        else:
            self.rect=self.rect

        
            

class Bread(Sprite):
    
    def __init__(self,game,x,y):
        Sprite.__init__(self)
        self.image, self.rect= _load_image(join('games','Koala_Kross','bread.png'), x, y)
        self.game=game
        

    def update(self):
        
        if self.rect.colliderect(self.game.koala.rect):
            self.game.win()
            
##            font.render('Congrats! You have appropriately noursished this previously starving koala.')
##            textpos = text.get_rect()
##            textpos.centerx = background.get_rect().centerx
##            background.blit(text, textpos)
        else:
            self.rect=self.rect.move(0,0)

class Background(Sprite):
    def __init__(self):
        Sprite. __init__(self)
        self.image, self. rect= _load_image(join('games','Koala_Kross','eucalyptus.jpg'),0,0)

class KoalaKross(Microgame):
    
    
    def __init__(self):
        Microgame.__init__(self)
        self.rect= Rect(0,0, locals.WIDTH, locals.HEIGHT)
##        surface=pygame.display.set_mode((1024,768))
##        surface.fill(Color(0,0,250))
        self.koala=Koala(self)
        self.panda1=Panda(self,200,100,randint(2,10),randint(5,15))
        self.panda2=Panda(self,500,100,randint(5,15),randint(10,25))
        self.panda3=Panda(self,800,100,randint(6,17),randint(20,30))
        self.bread=Bread(self,randint(400,1000),randint(100,600))
        self.background=Background()
        self.sprites=OrderedUpdates([self.background,self.koala,self.bread,self.panda1,self.panda2,self.panda3,self.background])
        self.clock=pygame.time.Clock()

    def start(self):
 ##       music.load(join('games','Koala_Kross','remix.ogg')
        music.load('games/Koala_Kross/remix.ogg')
        music.play()

    def stop(self):
        music.stop()

    def update(self):
##        time=pygame.time.get_ticks()
        self.sprites.update()
        for event in pygame.event.get():
      
            
            if event.type==KEYDOWN and event.key==K_DOWN:
                self.koala.velocity=(0,30)
            if event.type==KEYUP and event.key==K_DOWN:
                self.koala.velocity=(0,0)
                
            if  event.type==KEYDOWN and event.key==K_UP:
                self.koala.velocity=(0,-30)
            if event.type==KEYUP and event.key == K_UP:
                self.koala.velocity=(0,0)
                
            if event.type==KEYDOWN and event.key == K_LEFT:
                self.koala.velocity=(-30,0)
            if event.type==KEYUP and event.key==K_LEFT:
                self.koala.velocity=(0,0)
            if event.type==KEYDOWN and event.key==K_RIGHT:
                self.koala.velocity=(30,0)
            if event.type==KEYUP and event.key==K_RIGHT:
                self.koala.velocity=(0,0)
            if event.type==KEYDOWN and event.key == K_q:
                self.lose()
            
            

    def render (self, surface):
##        Surface=display.set_mode((1024,768))
        surface.fill(Color(0,0,0))
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


