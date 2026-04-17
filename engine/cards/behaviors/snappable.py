

class Snappable:
    def __init__(self):
        self.is_snapped = False
        self.is_locked = False
        self.curr_zone = None

    def snap(self, zone):
        if self.curr_zone:
            return self.curr_zone.topleft