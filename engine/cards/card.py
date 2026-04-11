from pygame.transform import scale_by

from engine.cards.behaviors.draggable import Draggable

class Card(Draggable):
	active_card = None
	hovered_card = None

	@staticmethod
	def reorder():
		pass

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

		# Use scaled image and set currently hovered card
		if hovered:
			self.scale_image = True
			Card.hovered_card = self

		# Start dragging and set currently active card
		if hovered and input_context.mouse_pressed:
			self.start_drag(mouse_pos, self.pos)
			Card.active_card = self

		# Change position via dragging
		if self.dragging and input_context.mouse_down:
			self.pos = self.drag(mouse_pos)

		# Stop dragging and unset currenly active card
		if self.dragging and input_context.mouse_released:
			self.stop_drag()
			Card.active_card = None

		# Stop scaling the image and unset currently hovered card
		if not hovered:
			self.scale_image = False
			Card.hovered_card = None

		# Update position
		self.rect.topleft = self.pos

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