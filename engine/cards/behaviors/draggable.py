class Draggable:
	def __init__(self):
		self.dragging = False
		self.offset = (0, 0)

	def start_drag(self, mouse_pos, obj_pos):
		self.dragging = True
		self.offset = (obj_pos[0] - mouse_pos[0], obj_pos[1] - mouse_pos[1])

	def drag(self, mouse_pos):
		return (mouse_pos[0] + self.offset[0], mouse_pos[1] + self.offset[1])
	
	def stop_drag(self):
		self.dragging = False