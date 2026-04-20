from pygame.rect import Rect
from pygame import draw

from engine.cards.card import Card

class SnapZone(Rect):
    DEFAULT_SIZE = (192, 256)

    def __init__(self, pos, size, max_cards, locked):
        if size is not None:
            super().__init__(pos, size)
        else:
            super().__init__(pos, SnapZone.DEFAULT_SIZE)

        self.color = (255, 0, 0)
        self.highlight_color = (255, 100, 0)
        self.border_radius = 10
        self.highlighted = False

        self.max_cards = max_cards
        self.cards = []
        self.locked = locked

    def snap(self, card):
        card.snappable.is_snapped = True
        self.cards.insert(0, card)

        card.rect.center = self.center
        card.pos = card.rect.topleft

    def unsnap(self):
        card = self.cards.pop(0)
        
        card.snappable.is_snapped = False
    
    def update(self, dt, input_context):
        # Check for inserted cards
        if Card.active is not None and self.colliderect(Card.active.draggable_rect):
            self.highlighted = True

            if input_context["mouse"]["mouse_released"] and len(self.cards) < self.max_cards:
                self.snap(Card.active)
        else:
            self.highlighted = False

        # Card removal
        if len(self.cards) > 0:
            if Card.hovered == self.cards[0] and input_context["mouse"]["mouse_pressed"]:
                self.unsnap()
    
    def render(self, surface):
        if self.highlighted:
            draw.rect(surface, self.highlight_color, self, border_radius=self.border_radius)
        else:
            draw.rect(surface, self.color, self, border_radius=self.border_radius)

    

    def get_pos(self):
        return self.topleft