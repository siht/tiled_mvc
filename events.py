'''
Events of system copied of sjbrown
'''

# SECURITY NOTE (of sjbrown): anything in here can be created simply by
# sending the class name over the network. This is a potential vulnerability
# I wouldn't suggest letting any of these classes DO anything, especially
# things like file system access, or allocating huge amounts of memory

class Event(object):
    """this is a superclass for any events that might be generated by an
    object and sent to the EventManager"""
    name = "Generic Event"

class TickEvent(Event):
    def __init__(self, aps):
        self.name = "CPU Tick Event"
        self.aps = aps

class SecondEvent(Event):
    def __init__(self):
        self.name = "Clock One Second Event"

class QuitEvent(Event):
    def __init__(self):
        self.name = "Program Quit Event"

class MapBuiltEvent(Event):
    def __init__(self, map):
        self.name = "Map Finished Building Event"
        self.map = map

class GameStartRequest(Event):
    def __init__(self):
        self.name = "Game Start Request"

class GameStartedEvent(Event):
    def __init__(self, game):
        self.name = "Game Started Event"
        self.game = game

class IWillMoveToEvent(Event):
    def __init__(self, charactor, new_sector):
        self.name = "I will move to event"
        self.charactor = charactor
        self.new_sector = new_sector

class CharactorMoveRequest(Event):
    def __init__(self, direction):
        self.name = "Charactor Move Request"
        self.direction = direction

class CharactorFaceEvent(Event):
    def __init__(self, direction):
        self.name = "Charactor Face Eventt"
        self.direction = direction

class CharactorMoveEvent(Event):
    def __init__(self, charactor):
        self.name = "Charactor Move Event"
        self.charactor = charactor

class CharactorPlaceRequest(Event):
    """..."""
    def __init__(self, player, charactor, sector):
        self.name = "Charactor Placement Request"
        self.player = player
        self.charactor = charactor
        self.sector = sector

class CharactorPlaceEvent(Event):
    """this event occurs when a Charactor is *placed* in a sector, 
    ie it doesn't move there from an adjacent sector."""
    def __init__(self, charactor):
        self.name = "Charactor Placement Event"
        self.charactor = charactor
