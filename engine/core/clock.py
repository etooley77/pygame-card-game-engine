from pygame import time

MILLISECONDS_PER_SECOND = 1000
DEFAULT_FPS = 60

class EngineClock:
	def __init__(self):
		self.clock = time.Clock()

		self.fps = DEFAULT_FPS

		self.engine_time = 0
		self.accumulator = 0

	def tick_engine(self) -> float:
		dt = self.clock.tick(self.fps)

		self.accumulator += dt
		if self.accumulator >= MILLISECONDS_PER_SECOND:
			self.accumulator -= MILLISECONDS_PER_SECOND
			self.engine_time += 1

		return dt
	
	def get_engine_time(self) -> int:
		return self.engine_time
	
	def get_fps(self) -> int:
		return self.fps
	
	def set_fps(self, new_fps):
		self.fps = new_fps