import json

class EventHandler:
	keybinds = None

	@staticmethod
	def load_config(keybinds):
		EventHandler.keybinds = keybinds

	@staticmethod
	def decode(events):
		actions = []

		for event in events:
			try:
				actions.append(EventHandler.keybinds[f"{event.key}"])
			except:
				continue

		return actions