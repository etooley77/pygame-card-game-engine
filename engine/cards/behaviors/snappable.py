

class Snappable:
    def __init__(self):
        self.is_snapped = False
        self.is_locked = False
        self.curr_zone = None

    def snap(self, zone):
        self.curr_zone = zone
        
    def unsnap(self):
        self.curr_zone.remove_card()
        self.is_snapped = False
        self.curr_zone = None