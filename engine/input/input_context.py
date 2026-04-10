class InputContext:
	def __init__(self):
		self.events = []

		self.mouse_pos = (0, 0)
		self.mouse_pressed = False
		self.mouse_released = False
		self.mouse_down = False

	def clear(self):
		self.events.clear()
		self.mouse_pressed = False
		self.mouse_released = False