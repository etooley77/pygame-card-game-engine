import json
import pygame

class EventHandler:
	keybinds = None

	@staticmethod
	def load_config(keybinds):
		EventHandler.keybinds = keybinds

	def __init__(self):
		self.actions = {"keys": [], "mouse": {"mouse_pressed": False, "mouse_down": False, "mouse_released": False, "mouse_pos": (0, 0)}}

	def decode(self, events):
		self.actions["keys"].clear()
		self.actions["mouse"]["mouse_pressed"] = False
		self.actions["mouse"]["mouse_released"] = False

		for event in events:
			match event.type:
				case pygame.MOUSEBUTTONDOWN:
					match event.button:
						case pygame.BUTTON_LEFT:
							self.actions["mouse"]["mouse_pressed"] = True
							self.actions["mouse"]["mouse_down"] = True

				case pygame.MOUSEBUTTONUP:
					match event.button:
						case pygame.BUTTON_LEFT:
							self.actions["mouse"]["mouse_released"] = True
							self.actions["mouse"]["mouse_down"] = False

				case pygame.KEYDOWN:
					try:
						self.actions["keys"].append(EventHandler.keybinds[f"{event.key}"])
					except:
						continue

				case _:
					continue

		self.actions["mouse"]["mouse_pos"] = pygame.mouse.get_pos()

		return self.actions