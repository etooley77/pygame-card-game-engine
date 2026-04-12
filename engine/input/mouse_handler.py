# A group of helpful mouse functions
class MouseHandler:
	@staticmethod
	def check_inside_screen(mouse_pos, window_size):
		if mouse_pos[0] > 0 and mouse_pos[0] < window_size[0] and mouse_pos[1] > 0 and mouse_pos[1] < window_size[1]:
			return True
		return False