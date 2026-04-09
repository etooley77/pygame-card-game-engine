from pygame import display

# Based on a singleton design pattern
class Window:
	def __new__(cls, *args, **kwargs):
		if not hasattr(cls, "instance"):
			instance = super().__new__(cls)
		return instance
	
	def __init__(self, window_size, title: str):
		self.surface = display.set_mode(window_size)
		display.set_caption(title)

	def get_surface(self):
		return self.surface