from pygame.image import load
from pygame.transform import scale_by

from game.states import sandbox_state

class Game:
	def __init__(self):
		self.window_size = (1200, 900)
		self.title = "Test Game"
		self.game_context = {"window_size": self.window_size}

		self.states = []

	def enter(self, engine_context):
		self.game_context["asset_manager"] = engine_context.asset_manager

		self.states.append(sandbox_state.SandboxState(self.game_context))
		self.states[0].enter(engine_context)

	def update(self, dt, event_context):
		self.states[0].update(dt, event_context)

	def render(self, surface):
		self.states[0].render(surface)