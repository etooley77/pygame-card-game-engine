from pygame.rect import Rect

class SnapZone(Rect):
    def __init__(self, single_arg):
        super().__init__(single_arg)
        self.rect = Rect(single_arg)

    def get_pos(self):
        return self.rect.topleft