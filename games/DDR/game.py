import pygame, pygame.mixer
import pygame
from pygame import Surface
from pygame.image import load
from pygame.locals import *
from pygame.mixer import music
from pygame.rect import Rect
from pygame.sprite import Group, Sprite, OrderedUpdates, LayeredUpdates
from pygame.color import Color
from random import randint, choice
from pygame.font import Font
from os.path import join
from pygame.transform import rotate
import locals
from microgame import Microgame
import pyganim

def make_game():
    return DDR()

def title():
    return 'Dance Dance Revolution: SAAST Edition'

def thumbnail():
    return join('games','DDR','DDR_Images','downclear.png')

def hint():
    'Dance'

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

class arrow(Sprite):

    def __init__(self,game,direction, x, y,vx,vy):
        Sprite.__init__(self)
        self.image, self.rect=_load_image(join('games','DDR','DDR_Images','upclear.png'),x,y)
        self.direction=direction
        
        if self.direction=='left':
            self.image, self.rect=_load_image(join('games','DDR','DDR_Images','leftclear.png'), x, y)
        
        elif self.direction=='down':
            self.image, self.rect=_load_image(join('games','DDR','DDR_Images','downclear.png'), x, y)
            

        elif self.direction=='right':
            self.image, self.rect=_load_image(join('games','DDR','DDR_Images','rightclear.png'), x, y)
    
        else:
            self.image=self.image
    

        self.area=game.rect
        self.game=game

    def update(self):
        self.rect=self.rect.move(0,0)

class Background(Sprite):
    def __init__(self):
        Sprite. __init__(self)
        self.image, self. rect= _load_image(join('games','DDR','DDRGIFS','GalacticBreakoutWall.png'),0,0)



class moving_arrow(Sprite):

    def __init__(self,game,direction,x,y,vx,vy):
        Sprite.__init__(self)

        
        self.direction=direction
        
        if self.direction=='right':
            
            self.image, self.rect=_load_image(join('games','DDR','DDR_Images','rightreal.png'), x, y)

        elif self.direction=='down':
            
            self.image, self.rect=_load_image(join('games','DDR','DDR_Images','downreal.png'), x, y)


        elif self.direction=='left':
            
            self.image, self.rect=_load_image(join('games','DDR','DDR_Images','leftreal.png'), x, y)


        else:
            
            self.image, self.rect=_load_image(join('games','DDR','DDR_Images','upreal.png'), x, y)

            
        self.vx=vx
        self.vy=vy
        self.area=game.rect
        self.game=game

    def update(self):
        self.rect=self.rect.move(self.vx,self.vy)

        

        

        for event in pygame.event.get():
            if event.type==KEYDOWN or event.type==KEYUP:
                if event.key==K_LEFT:
    
                    
                    
                    if (self.rect.center[1]-self.game.arrow1.rect.center[1])<=25 and self.direction=='left':
                        self.kill()


                        
                elif event.key==K_DOWN:

                    if (self.rect.center[1]-self.game.arrow2.rect.center[1])<=25 and self.direction=='down':                          
                        self.kill()
                        
                elif event.key==K_UP:

                    if (self.rect.center[1]-self.game.arrow3.rect.center[1])<=25 and self.direction=='up':
                        self.kill()
                        

                elif event.key==K_RIGHT:

                    if (self.rect.center[1]-self.game.arrow4.rect.center[1])<=25 and self.direction=='right':
                        self.kill()
                        
       
        if self.rect.y<10:
             
            self.game.lose()
        
                    
                       
                    
                    
                        

            


class DDR(Microgame):

    def __init__(self):
        Microgame.__init__(self)
        self.rect=Rect(0,0, locals.WIDTH, locals.HEIGHT)
        self.arrow1=arrow(self,'left',50,50,0,0)
        self.arrow2=arrow(self,'down',150,50,0,0)
        self.arrow3=arrow(self,'up',250, 50,0,0)
        self.arrow4=arrow(self,'right',350,50,0,0)
        self.background=Background()
        self.sprites=LayeredUpdates([self.background,self.arrow1,self.arrow2,self.arrow3,self.arrow4])
        self.timesincearrow=0
        self.dancer=pyganim.PygAnimation([('games/DDR/DDRGIFS/TWERK/twerk1.png',0.1),
                                        ('games/DDR/DDRGIFS/TWERK/twerk2.png',0.1),
                                        ('games/DDR/DDRGIFS/TWERK/twerk3.png',0.1),
                                        ('games/DDR/DDRGIFS/TWERK/twerk4.png',0.1),
                                        ('games/DDR/DDRGIFS/TWERK/twerk5.png',0.1),
                                        ('games/DDR/DDRGIFS/TWERK/twerk6.png',0.1)])
        
        self.anim=pyganim.PygAnimation([('games/DDR/DDRGIFS/MUSIC_ANIMATION/music1.png',0.1),
                                        ('games/DDR/DDRGIFS/MUSIC_ANIMATION/music2.png',0.1),
                                        ('games/DDR/DDRGIFS/MUSIC_ANIMATION/music3.png',0.1),
                                        ('games/DDR/DDRGIFS/MUSIC_ANIMATION/music4.png',0.1),
                                        ('games/DDR/DDRGIFS/MUSIC_ANIMATION/music5.png',0.1),
                                        ('games/DDR/DDRGIFS/MUSIC_ANIMATION/music6.png',0.1),
                                        ('games/DDR/DDRGIFS/MUSIC_ANIMATION/music7.png',0.1),
                                        ('games/DDR/DDRGIFS/MUSIC_ANIMATION/music8.png',0.1),
                                        ('games/DDR/DDRGIFS/MUSIC_ANIMATION/music9.png',0.1),
                                        ('games/DDR/DDRGIFS/MUSIC_ANIMATION/music10.png',0.1),
                                        ('games/DDR/DDRGIFS/MUSIC_ANIMATION/music11.png',0.1),
                                        ('games/DDR/DDRGIFS/MUSIC_ANIMATION/music12.png',0.1),
                                        ('games/DDR/DDRGIFS/MUSIC_ANIMATION/music13.png',0.1),
                                        ('games/DDR/DDRGIFS/MUSIC_ANIMATION/music14.png',0.1)])

        self.disco=pyganim.PygAnimation([('games/DDR/DDRGIFS/DISCOBALL/disco3.png',0.1),
                                         ('games/DDR/DDRGIFS/DISCOBALL/disco4.png',0.1)])
    
        self.dancer.play()
        self.anim.play()
        self.disco.play()

    def time_elapsed(self):
        self.timesincearrow=pygame.time.get_ticks()
        
    def start(self):
        self.time_elapsed()
        music.load('games/DDR/geekin.ogg')
        music.play(2,0.0)

    def stop(self):
        music.stop()

    
        
    def update(self):
        self.sprites.update()
        time=pygame.time.get_ticks()
        if time-self.timesincearrow>350:
            num=randint(0,3)
            if num==0:
                self.sprites.add(moving_arrow(self,'left',50,768,0,-10))
            elif num==1:
                self.sprites.add(moving_arrow(self,'down',150,768,0,-10))
            elif num==2:
                self.sprites.add(moving_arrow(self,'up',250,768,0,-10))
            elif num==3:
                self.sprites.add(moving_arrow(self,'right',350,768,0,-10))
                
            self.time_elapsed()
            
        for event in pygame.event.get():
            if event.type==KEYDOWN or event.type==KEYUP:
                if event.key==K_q:
                    self.lose()
        

    def render(self,surface):
        surface.fill(Color(0,0,0))
        self.sprites.draw(surface)
        self.dancer.blit(surface,(800,100))
        self.anim.blit(surface,(550,500))
        self.disco.blit(surface,(600,50))
        
        
        
                    
        
                    
                
        
        

        
            


                                           
