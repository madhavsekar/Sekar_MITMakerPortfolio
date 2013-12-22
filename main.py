import sys, traceback, pygame
import locals, tester

WIDTH  = 1280
HEIGHT = 720
FPS    = 30

def main(args):
    ''' Entry point of the microgames program '''
    pygame.init()
    try:
        surface = pygame.display.set_mode([locals.WIDTH, locals.HEIGHT])
        pygame.display.set_caption('Microgames Tester')
        clock = pygame.time.Clock()
        t = tester.Tester(surface)
        while not t.finished:
            clock.tick(locals.FPS)
            t.update()
            t.render()
            pygame.display.flip()
    except Exception as e:
        ty, v, tb = sys.exc_info()
        print 'An exception occurred.  Terminating the game!'
        print traceback.print_exception(ty, v, tb)
    pygame.quit()

if __name__ == '__main__':
    main(sys.argv)
