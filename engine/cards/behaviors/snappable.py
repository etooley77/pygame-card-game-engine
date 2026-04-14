

class Snappable:
    def __init__(self):
        self.is_snapped = False
        self.curr_snap_zone = None

    def snap(self, zone):
        if self.curr_snap_zone:
            return self.curr_snap_zone.topleft