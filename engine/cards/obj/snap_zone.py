from pygame.rect import Rect
from pygame import draw

class SnapZone(Rect):
    def __init__(self, pos, size):
        super().__init__(pos, size)

    def get_pos(self):
        return self.topleft
    
    def render(self, surface):
        draw.rect(surface, (255, 0, 0), self)