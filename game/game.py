from pygame.image import load

class Game:
	def __init__(self):
		self.window_size = (800, 600)
		self.title = "Test Game"

	def update(self, dt, events):
		if (len(events) > 0):
			print(events)

	def render(self, context):
		menu_image = load("game/assets/menu.png").convert_alpha()
		context.renderer.surface.blit(menu_image, (0, 0))

		# 
		aos = context.asset_manager.get("ace_of_diamonds")
		if aos is not None: context.renderer.surface.blit(aos, (400, 300))