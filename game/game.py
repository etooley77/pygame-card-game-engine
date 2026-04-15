from pygame.image import load
from pygame.transform import scale_by

from engine.state.state_manager import StateManager

from engine.input.event_handler import EventHandler

from game.states import sandbox_state

from game.config.config_loader import ConfigLoader

class Game:
	def __init__(self):
		self.window_size = (1200, 900)
		self.title = "Test Game"
		self.game_context = {"window_size": self.window_size}

	def enter(self, engine_context):
		self.state_manager = StateManager(engine_context)
		self.game_context["asset_manager"] = engine_context.asset_manager
		EventHandler.load_config(ConfigLoader.load_keybinds())

		self.state_manager.enter_state(sandbox_state.SandboxState(self.game_context))

	def update(self, dt, input_context):
		self.state_manager.states[0].update(dt, input_context)

	def render(self, surface):
		self.state_manager.states[0].render(surface)