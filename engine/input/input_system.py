import pygame
from sys import exit

from engine.input.input_context import InputContext
from engine.input.event_handler import EventHandler

class InputSystem:
	def __init__(self):
		self.input_queue = []

		self.input_context = InputContext()

	def monitor(self):
		self.input_queue.clear()
		self.input_context.clear()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()

			if event.type == pygame.KEYDOWN:
				self.input_queue.append(event)

			# KEYUP event implementation for held keys
			
			if event.type == pygame.MOUSEBUTTONDOWN:
				self.input_context.mouse_pressed = True
				self.input_context.mouse_down = True

			if event.type == pygame.MOUSEBUTTONUP:
				self.input_context.mouse_down = False
				self.input_context.mouse_released = True

		self.input_context.events = EventHandler.decode(self.input_queue)
		self.input_context.mouse_pos = pygame.mouse.get_pos()

		return self.input_context