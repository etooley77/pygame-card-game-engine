from pygame.image import load
from pygame.transform import scale_by

from engine.cards.card import Card

class Game:
	def __init__(self):
		self.window_size = (1200, 900)
		self.title = "Test Game"

		self.background = None
		self.cards = []

	def initialize_context(self, engine_context):
		self.asset_manager = engine_context.asset_manager

		self.background = load("game/assets/menu.png").convert_alpha()

		# State (temporary)
		self.asset_manager.load_default_cards()

		# temp
		aos = Card(self.asset_manager.get("ace_of_spades"), (400, 300))
		self.cards.append(aos)

		aoc = Card(self.asset_manager.get("ace_of_clubs"), (200, 300))
		self.cards.append(aoc)

	def update(self, dt, event_context):
		# if (len(event_context.events) > 0):
		# 	print(event_context.events)

		for card in self.cards:
			is_hovered = card.update(event_context)

			if card.is_active:
				self.cards.append(self.cards.pop(self.cards.index(card)))

	def render(self, surface):
		if self.background:
			surface.blit(self.background, (0, 0))

		for card in self.cards:
			card.render(surface)