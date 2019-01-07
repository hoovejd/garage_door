import time
from enum import Enum

from twisted.web.static import File

class DoorState(Enum):
    OPEN = 'open'
    OPENING = 'opening'
    CLOSED = 'closed'
    CLOSING = 'closing'

class Door(object):

    def __init__(self):
        self.open_time = time.time

    def get_state(self):
        return DoorState.OPEN

    def toggle_relay(self):
        state = self.get_state()

class Controller(object):

    def __init__(self):
        stuff = []

    def toggle_door(self):
        stuff = []

    def run(self):
        root = File('www')