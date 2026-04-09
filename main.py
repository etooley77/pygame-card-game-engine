from engine.engine import Engine
from game.game import Game

if __name__ == "__main__":
	game = Game()

	engine = Engine(game)
	engine.run()