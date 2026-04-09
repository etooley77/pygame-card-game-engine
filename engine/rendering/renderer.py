from pygame.display import flip

CLEAR_COLOR = (0, 0, 0)

class Renderer:
	def __init__(self, window):
		self.surface = window.get_surface()

	def clear(self):
		self.surface.fill(CLEAR_COLOR)

	def update(self):
		flip()