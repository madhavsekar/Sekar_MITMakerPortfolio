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
from pygame.transform import rotate
import locals
from microgame import Microgame

def make_game():
    return DDR()

def title():
    return 'Dance Dance Revolution: SAAST Edition'

def thumbnail():
    pass

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
        self.image, self.rect=_load_image(name, x, y)(join('games','DDR','DDR_Images','upclear.png')
        if self.direction=='right':
            self.transform.rotate(self.image,90)

        elif self.direction=='down':
            self.transform.rotate(self.image,180)

        elif self.direction=='left':
            self.transform.rotate(self.image,270)

        else:
            self.image=self.image

        self.area=game.rect
        self.game=game

    def update(self):
        self.rect=self.rect.move(0,0)

class moving_arrow(Sprite):

    def __init__(self,game,direction,x,y,vx,vy):
        Sprite.__init__(self)
        self.image, self.rect=_load_image(join('games','DDR','DDR_Images','up.gif'), x, y)
        
        
        if self.direction=='right':
            self.transform.rotate(self.image,90)
            event.type==K_Right

        elif self.direction=='down':
            self.transform.rotate(self.image,180)
            event.type=K_DOWN

        elif self.direction=='left':
            self.transform.rotate(self.image,270)
            event.type=K_LEFT

        else:
            self.image=self.image
            event.type=K_UP
            
        self.vx=vx
        self.vy=vy
        self.area=game.rect
        self.game=game

    def update(self):
        self.rect=self.rect.move(self.vx,self.vy)
        if self.rect==self.game.arrow.rect:
            for event in pygame.event.get():
                if event.type==self.direction.event.type:
                    self.kill()
                else:
                    self.game.lose()
        elif self.rect.y<0:
            self.game.lose()

##    def num_arrows(self):
####        time=pygame.time.get_ticks()
##        num=randint(0,3):
##            if num==0:
                
        


class DDR(Microgame):

    def __init__(self):
        Microgame.__init__(self)
        self.rect=Rect(0,0, locals.WIDTH, locals.HEIGHT)
        self.arrow1=arrow(self,'left',50,80,0,0)
        self.arrow2=arrow(self,'down',100,80,0,0)
        self.arrow3=arrow(self,'up', 150, 80,0,0)
        self.arrow4=arrow(self,'right',200,80,0,0)
        self.sprites=OrderedUpdates(self.arrow1,self.arrow2,self.arrow3)

    def start(self):
        pass

    def stop(self):
        pass

    def update(self):
        self.sprites.update()

    def render(self,surface):
        surface.fill(Color(0,0,0))
        self.sprites.draw(surface)
        
        
        
                    
        
                    
                
        
        

        
            


                                           
