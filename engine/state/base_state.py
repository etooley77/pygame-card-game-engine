

class BaseState:
	def __init__(self, game_context):
		self.game_context = game_context

	def enter(self, engine_context):
		self.engine_context = engine_context

		self.background = None

		print("Entering state: " + self)

	def exit(self):
		print("Exiting state: " + self)

	def update(self, dt, event_context):
		pass

	def render(self, surface):
		if self.background:
			surface.blit(self.background, (0, 0))