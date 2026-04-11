from pygame import image, transform
from pygame import mixer

from os import listdir

class AssetManager:
	def __init__(self):
		self.assets = {}

	def load_image(self, name, filepath):
		self.assets[name] = image.load(filepath)

	def load_sound(self, name, filepath):
		self.assets[name] = mixer.Sound(filepath)

	def get(self, name):
		return self.assets.get(name)
	
	# Load the cards provided inherently by the engine
	def load_default_cards(self):
		default_cards_path = r"engine/assets/cards"

		for card_image in listdir(default_cards_path):
			self.load_image(card_image.split(".")[0], (default_cards_path + f"/{card_image}"))



	# Typically used to set a background
	def scale_to_screen_size(self, surface, image):
		return transform.scale_by(image, (surface.get_width() / image.get_width(), surface.get_height() / image.get_height()))