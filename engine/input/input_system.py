import pygame

from engine.input.event_handler import EventHandler

class InputSystem:
	def __init__(self):
		self.input_queue = []
		self.event_handler = EventHandler()

	def monitor(self):
		self.input_queue.clear()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()
			else:
				self.input_queue.append(event)

		return self.event_handler.decode(self.input_queue)