from pygame.rect import Rect

from engine.cards.behaviors import draggable, hoverable, snappable

from engine.input.mouse_handler import MouseHandler

class CardView:
	#: The currently active card being dragged, or None if no card is active.
	active = None
	#: The card currently being hovered over, or None if no card is hovered.
	hovered = None

	@staticmethod
	def reorder(card_list):
		if CardView.active == None:
			return card_list
		else:
			if CardView.active in card_list:
				card_list.append(card_list.pop(card_list.index(CardView.active)))
				return card_list

	def __init__(self, image, pos):
		self.draggable = draggable.Draggable()
		self.hoverable = hoverable.Hoverable()
		self.snappable = snappable.Snappable()

		self.image = image
		self.hoverable.scale_factor = 1.1 # override default scale factor

		self.pos = pos
		self.rect = self.image.get_rect(center=pos)
		self.draggable_rect = Rect(0, 0, self.rect.width // 1.25, self.rect.height // 1.5)

	def update(self, input_context, game_context):
		# hovered = self.rect.collidepoint(input_context["mouse"]["mouse_pos"])
		can_be_dragged = self.draggable_rect.collidepoint(input_context["mouse"]["mouse_pos"])

		# Set currently active and hovered cards
		if can_be_dragged:
			CardView.hovered = self
			if input_context["mouse"]["mouse_pressed"]:
				CardView.active = self
		else:
			if CardView.hovered == self:
				CardView.hovered = None

		if self == CardView.hovered and (CardView.active == None or CardView.active == self):
			self.hoverable.start_hover()
		else:
			self.hoverable.stop_hover()

		if self == CardView.active and not self.snappable.is_snapped:
			if MouseHandler.check_inside_screen(input_context["mouse"]["mouse_pos"], game_context["window_size"]):
				if input_context["mouse"]["mouse_pressed"]:
					self.draggable.start_drag(input_context["mouse"]["mouse_pos"], self.pos)

				if self == CardView.active and input_context["mouse"]["mouse_down"]:
					self.pos = self.draggable.drag(input_context["mouse"]["mouse_pos"])

				if self == CardView.active and input_context["mouse"]["mouse_released"]:
					self.draggable.stop_drag()
					CardView.active = None

		# Update position
		self.rect.topleft = self.pos
		self.draggable_rect.center = self.rect.center

	def render(self, surface):
		if self.hoverable.hovering and self == CardView.hovered:
			scaled_image = self.hoverable.scale_on_hover(self.image, self.pos)
			surface.blit(scaled_image[0], scaled_image[1])
		else:
			surface.blit(self.image, self.pos)