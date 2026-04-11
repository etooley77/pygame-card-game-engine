class Hoverable:
	def __init__(self):
		self.hovering = False
		self.scale_factor = 2
		self._private = "hidden"

	def start_hover(self):
		pass

	def scale_on_hover():
		pass

	def calculate_scaled_pos(self):
		w = self.image.get_width()
		h = self.image.get_height()
		s = self.scale_factor
	
		return (self.pos[0] - 0.5 * w * (s - 1), self.pos[1] - 0.5 * h * (s - 1))