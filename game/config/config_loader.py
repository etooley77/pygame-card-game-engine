from json import load

class ConfigLoader:
	keybinds_path = "game/config/keybinds.json"

	@staticmethod
	def load_keybinds():
		try:
			with open(ConfigLoader.keybinds_path, 'r') as f:
				return load(f)
		except:
			print("Unable to find keybinds config!")