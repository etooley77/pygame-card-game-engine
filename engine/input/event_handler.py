import json
import pygame

class EventHandler:
	keybinds = None

	@staticmethod
	def load_config(keybinds):
		EventHandler.keybinds = keybinds

	@staticmethod
	def decode(events):
		actions = []

		for event in events:
			match event.type:
				case pygame.MOUSEBUTTONDOWN:
					actions.append(EventHandler.decode_mouse_down_event(event.button))

				case pygame.MOUSEBUTTONUP:
					actions.append(EventHandler.decode_mouse_up_event(event.button))

				case pygame.KEYDOWN:
					try:
						actions.append(EventHandler.keybinds[f"{event.key}"])
					except:
						continue

				case _:
					continue

		return actions
	
	@staticmethod
	def decode_mouse_down_event(button):
		match button:
			case 1: return "mouse_left_down"
			case 2: return "mouse_middle_down"
			case 3: return "mouse_right_down"

			case _: pass

	@staticmethod
	def decode_mouse_up_event(button):
		match button:
			case 1: return "mouse_left_up"
			case 2: return "mouse_middle_up"
			case 3: return "mouse_right_up"

			case _: pass

	@staticmethod
	def decode_keypress_event(dict):
		pass