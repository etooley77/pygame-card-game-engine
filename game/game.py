from pygame.image import load

class Game:
	def __init__(self):
		self.window_size = (800, 600)
		self.title = "Test Game"

	def update(self, dt, input_system):
		pass

	def render(self, renderer):
		menu_image = load("game/assets/menu.png").convert_alpha()
		renderer.surface.blit(menu_image, (0, 0))