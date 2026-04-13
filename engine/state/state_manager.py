

class StateManager:
	def __init__(self, engine_context):
		self.states = []
		self.engine_context = engine_context

	def enter_state(self, state):
		self.states.insert(0, state)

		state.enter(self.engine_context)

	def exit_state(self):
		self.states.pop(0).exit()