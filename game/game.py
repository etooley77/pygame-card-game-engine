from pygame.image import load
from pygame.transform import scale_by

from engine.cards.card import Card

class Game:
	def __init__(self):
		self.window_size = (1200, 900)
		self.title = "Test Game"

		self.background = None
		self.cards = []

		self.game_context = {"window_size": self.window_size}

	def initialize_context(self, engine_context):
		self.asset_manager = engine_context.asset_manager

		self.background = self.asset_manager.scale_to_screen_size(engine_context.renderer.surface, load("game/assets/menu.png").convert_alpha())

		# State (temporary)
		self.asset_manager.load_default_cards()

		# temp
		aos = Card(self.asset_manager.get("ace_of_spades"), (400, 300))
		self.cards.append(aos)

		aoc = Card(self.asset_manager.get("ace_of_clubs"), (200, 300))
		self.cards.append(aoc)

		aod = Card(self.asset_manager.get("ace_of_diamonds"), (600, 300))
		self.cards.append(aod)

	def update(self, dt, event_context):
		# if (len(event_context.events) > 0):
		# 	print(event_context.events)

		for card in self.cards:
			card.update(event_context, self.game_context)

		self.cards = Card.reorder(self.cards)

	def render(self, surface):
		if self.background:
			surface.blit(self.background, (0, 0))

		for card in self.cards:
			card.render(surface)