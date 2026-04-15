from pygame.image import load

from engine.state.base_state import BaseState

from engine.cards.card import Card

class SandboxState(BaseState):
	def __init__(self, game_context):
		super().__init__(game_context)

	def enter(self, engine_context):
		self.background = self.game_context["asset_manager"].scale_to_screen_size(engine_context.renderer.surface, load("game/assets/menu.png").convert_alpha())

		self.load_cards()

	def exit(self):
		pass

	def update(self, dt, input_context):
		# DEBUG
		if len(input_context["keys"]) > 0:
			print(input_context["keys"])
		# DEBUG

		for card in self.cards:
			card.update(input_context, self.game_context)

		self.cards = Card.reorder(self.cards)

	def render(self, surface):
		super().render(surface)

		for card in self.cards:
			card.render(surface)

	# ---------------------------------------------

	def load_cards(self):
		self.cards = []

		self.game_context["asset_manager"].load_default_cards()

		aos = Card(self.game_context["asset_manager"].get("ace_of_spades"), (400, 300))
		self.cards.append(aos)

		aoc = Card(self.game_context["asset_manager"].get("ace_of_clubs"), (200, 300))
		self.cards.append(aoc)

		aod = Card(self.game_context["asset_manager"].get("ace_of_diamonds"), (600, 300))
		self.cards.append(aod)