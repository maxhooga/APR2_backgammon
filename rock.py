from enum import Enum

class State(Enum):
	READY = 1
	IN_BAR = 2
	OUT = 3
	CANT_MOVE = 4

class Rock:
	def __init__(self, color, name = '', state = State.CANT_MOVE, next = None, previous = None):
		self.color = color
		self.name = name
		self.next = next
		self.previous = previous
		self.state = state
	
	def change_state(self, state_name):
		self.state = State[state_name]
		return self.state
	