from pygame.transform import scale_by

class Hoverable:
	def __init__(self):
		self.hovering = False
		self.do_hover = False
		self.scale_factor = 2

	def start_hover(self):
		self.hovering = True

	def stop_hover(self):
		self.hovering = False

	def set_hover(self, is_hovering):
		self.hovering = is_hovering

	def scale_on_hover(self, image, pos):
		return [scale_by(image, self.scale_factor), self.calculate_scaled_pos(image, pos)]

	def calculate_scaled_pos(self, image, pos):
		w = image.get_width()
		h = image.get_height()
		s = self.scale_factor
	
		return (pos[0] - 0.5 * w * (s - 1), pos[1] - 0.5 * h * (s - 1))