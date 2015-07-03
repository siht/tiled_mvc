from patterns import FlyWeight, typewrapper, AbsListener
from utils import load_img, Surfaces
from preferences import SIZE_TILE
import pygame
from preferences import DIRECTION_UP, DIRECTION_DOWN, DIRECTION_LEFT, DIRECTION_RIGHT
from events import *

@typewrapper(pygame.surface.Surface, '_surf')
class SurfaceImage(object):
    '''wrapper of a basic Surface of pygame only for images'''
    __metaclass__ = FlyWeight
    def __init__(self, path):
        self._surf = load_img(path)

    wrap = property(lambda self: self._surf)

class SectorSprite(pygame.sprite.Sprite):
    '''sprite of a void sector'''
    def __init__(self, sector, group=None):
        pygame.sprite.Sprite.__init__(self, group)
        grounds = SurfaceImage('Tileset- ground.png')
        default_ground = Surfaces.listSurface(grounds, (13, 8))[19]
        self.image = Surfaces.scale(default_ground, (SIZE_TILE, SIZE_TILE))
        self.rect = self.image.get_rect()
        self.sector = sector

class CharactorSprite(pygame.sprite.Sprite, AbsListener):
    '''sprite of the main character'''
    STAND = 1
    VELOCITY_CHANGE = 1

    def __init__(self, ev_manager, charactor, group = None):
        pygame.sprite.Sprite.__init__(self, group)
        self.ev_manager = ev_manager
        self.ev_manager.registerListener(self)
        self.charactor = charactor
        aux = Surfaces.listSurface(SurfaceImage('walk_front2.png'), (3,1))
        self.images = {DIRECTION_DOWN : aux}
        aux = Surfaces.listSurface(SurfaceImage('walk_sleft2.png'), (3,1))
        self.images.update({DIRECTION_LEFT : aux})
        aux = Surfaces.listSurface(SurfaceImage('walk_sright2.png'), (3,1))
        self.images.update({DIRECTION_RIGHT : aux})
        aux = Surfaces.listSurface(SurfaceImage('walk_back2.png'), (3,1))
        self.images.update({DIRECTION_UP : aux})
        self.rect = aux[0].get_rect()
        self.image = self.images[DIRECTION_DOWN][self.STAND]
        self.last_direction = DIRECTION_DOWN
        self.last_move = 1
        self.is_moving = 0

    def move(self, direction):
        self.is_moving = 1
        if direction == self.last_direction:
            if self.last_move == 2:
                self.image = self.images[self.last_direction][0]
                self.last_move = 0
            else:
                self.image = self.images[self.last_direction][2]
                self.last_move = 2
        else:
            self.image = self.images[direction][0]
            self.last_direction = direction
            self.last_move = 0

    def stand(self):
        self.image = self.images[self.last_direction][self.STAND]
        self.is_moving = 0

    def facingTo(self, direction):
        self.last_direction = direction
        self.stand()

    def notify(self, event):
        if not self.is_moving and isinstance(event, CharactorMoveRequest):
            self.move(event.direction)
        elif isinstance(event, CharactorPlaceEvent):
            self.stand()
        elif isinstance(event, CharactorMoveEvent):
            self.stand()
        elif isinstance(event, CharactorFaceEvent):
            self.facingTo(event.direction)
