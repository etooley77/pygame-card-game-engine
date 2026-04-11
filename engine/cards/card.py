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
		self.pos = pos
		self.rect = self.image.get_rect(topleft=pos)

	def update(self, input_context):
		hovered = self.rect.collidepoint(input_context.mouse_pos)

		# Use scaled image and set currently hovered card
		if hovered:
			self.hoverable.start_hover()
			Card.hovered = self

		# Start dragging and set currently active card
		if hovered and input_context.mouse_pressed:
			self.draggable.start_drag(input_context.mouse_pos, self.pos)
			Card.active = self

		# Change position via dragging
		if self.draggable.dragging and input_context.mouse_down:
			self.pos = self.draggable.drag(input_context.mouse_pos)

		# Stop dragging and unset currently active card
		if self.draggable.dragging and input_context.mouse_released:
			self.draggable.stop_drag()
			if Card.active is self:
				Card.active = None
		# Stop scaling the image and unset currently hovered card
		if not hovered:
			self.hoverable.stop_hover()
			if Card.hovered is self:
				Card.hovered = None

		# Update position
		self.rect.topleft = self.pos

	def render(self, surface):
		if self.hoverable.hovering and self == Card.hovered:
			scaled_image = self.hoverable.scale_on_hover(self.image, self.pos)
			surface.blit(scaled_image[0], scaled_image[1])
		else:
			surface.blit(self.image, self.pos)