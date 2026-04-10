import pygame
from sys import exit

class InputSystem:
	def __init__(self):
		self.input_queue = []
		print("InputSystem initialized!")

	def monitor(self):
		self.input_queue.clear()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()
			if event.type == pygame.KEYDOWN:
				self.input_queue.append(event)
			if event.type == (pygame.MOUSEBUTTONDOWN or pygame.MOUSEBUTTONUP):
				self.input_queue.append(event)

		return self.input_queue