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

        self.max_cards = max_cards
        self.cards = []
        self.locked = locked

    def add_card(self, card):
        if len(self.cards) < self.max_cards:
            self.cards.append(card)
            card.snappable.curr_zone = self
            Card.active == None

            card.rect.center = self.center
            card.pos = card.rect.topleft

            card.snappable.is_snapped = True
            if self.locked:
                card.snappable.is_locked = True

    def remove_card(self):
        self.cards.pop(0)
        
    def update(self, dt, input_context):
        if self.collidepoint(input_context["mouse"]["mouse_pos"]) and input_context["mouse"]["mouse_released"] and Card.active is not None:
            self.add_card(Card.active)

    
    def render(self, surface):
        draw.rect(surface, (255, 0, 0), self)

    

    def get_pos(self):
        return self.topleft