from pygame.rect import Rect
from pygame import draw

from engine.cards.behaviors import draggable, hoverable

class Card:
	#: The currently active card being dragged, or None if no card is active.
	active = None
	#: The card currently being hovered over, or None if no card is hovered.
	hovered = None

	@staticmethod
	def reorder(card_list):
		if Card.active == None:
			return card_list
		else:
			if Card.active in card_list:
				card_list.append(card_list.pop(card_list.index(Card.active)))
				return card_list

	def __init__(self, image, pos):
		self.draggable = draggable.Draggable()
		self.hoverable = hoverable.Hoverable()
		self.image = image
		self.hoverable.scale_factor = 1.1 # override default scale factor

		self.pos = pos
		self.rect = self.image.get_rect(center=pos)
		self.draggable_rect = Rect(0, 0, self.rect.width // 1.25, self.rect.height // 1.5)

	def update(self, input_context):
		hovered = self.rect.collidepoint(input_context.mouse_pos)
		can_be_dragged = self.draggable_rect.collidepoint(input_context.mouse_pos)

		# Set currently active and hovered cards
		if can_be_dragged:
			Card.hovered = self
			if input_context.mouse_pressed:
				Card.active = self
		else:
			if Card.hovered == self:
				Card.hovered = None

		if self == Card.hovered:
			self.hoverable.start_hover()

			if input_context.mouse_pressed:
				self.draggable.start_drag(input_context.mouse_pos, self.pos)

			if self == Card.active and input_context.mouse_down:
				self.pos = self.draggable.drag(input_context.mouse_pos)
			else:
				self.draggable.stop_drag()
		else:
			self.hoverable.stop_hover()

		# Update position
		self.rect.topleft = self.pos
		self.draggable_rect.center = self.rect.center

	def render(self, surface):
		if self.hoverable.hovering and self == Card.hovered:
			scaled_image = self.hoverable.scale_on_hover(self.image, self.pos)
			surface.blit(scaled_image[0], scaled_image[1])
		else:
			surface.blit(self.image, self.pos)