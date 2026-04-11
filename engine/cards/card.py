from pygame.transform import scale_by

from engine.cards.behaviors.draggable import Draggable

class Card(Draggable):
	def __init__(self, image, pos):
		super().__init__()
		self.image = image
		self.scale_image = False
		self.scale_factor = 1.1 # Must be greater than one

		self.pos = pos
		self.rect = self.image.get_rect(topleft=pos)

		self.is_active = False
		self.do_scale_on_hover = True

	def update(self, input_context):
		mouse_pos = input_context.mouse_pos
		hovered = self.rect.collidepoint(mouse_pos)

		# Use scaled image
		if hovered:
			self.scale_image = True

		# Start dragging
		if hovered and input_context.mouse_pressed:
			self.start_drag(mouse_pos, self.pos)
			self.is_active = True

		# Change position via dragging
		if self.dragging and input_context.mouse_down:
			self.pos = self.drag(mouse_pos)

		# Stop dragging
		if self.dragging and input_context.mouse_released:
			self.stop_drag()
			self.is_active = False

		# Stop scaling the image
		if not hovered:
			self.scale_image = False

		self.rect.topleft = self.pos

		return hovered

	def render(self, surface):
		if self.scale_image and self.do_scale_on_hover:
			surface.blit(scale_by(self.image, self.scale_factor), self.calculate_scaled_pos())
		else:
			surface.blit(self.image, self.pos)

	def calculate_scaled_pos(self):
		w = self.image.get_width()
		h = self.image.get_height()
		s = self.scale_factor
	
		return (self.pos[0] - 0.5 * w * (s - 1), self.pos[1] - 0.5 * h * (s - 1))