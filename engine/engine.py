import pygame, sys

from engine.engine_context import EngineContext

from engine.core.clock import EngineClock
from engine.core.window import Window

from engine.rendering.asset_manager import AssetManager
from engine.rendering.renderer import Renderer

class Engine:
	def __init__(self, game):
		pygame.init()
		self.clock = EngineClock()
		
		self.window = Window(game.window_size, game.title)
		self.renderer = Renderer(self.window)

		self.asset_manager = AssetManager()
		self.asset_manager.load_default_cards()

		# Inject game and create engine context
		self.engine_context = EngineContext(self.asset_manager, self.renderer, None)
		self.game = game

	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			# Tick clock and gather input
			dt = self.clock.tick_engine()
			# input here

			# clear screen
			self.renderer.clear()

			# game loop here
			self.game.render(self.engine_context)

			# update screen (flip)
			self.renderer.update()