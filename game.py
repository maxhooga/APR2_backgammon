from board import Board

class Game:
	def __init__(self, init_data):
		self.board = Board(init_data)

	def get_empty(self):
		results = []
		for i, stack in enumerate(self.board.stacks):
			if stack.state.name == "EMPTY":
				results.append(i)
		return results
	
	def get_has_one(self):
		results = []
		for i, stack in enumerate(self.board.stacks):
			if stack.state.name == "HAS_ONE":
				results.append(i)
		return results
	
	def get_has_elements(self):
		results = []
		for i, stack in enumerate(self.board.stacks):
			if stack.state.name == "HAS_ELEMENTS":
				results.append(i)
		return results
	
	def get_same_color(self, color):
		results = []
		for i, stack in enumerate(self.board.stacks):
			if stack.head != None:
				if stack.head.color == color:
					results.append(i)
		return results
	





	def get_different_color(self, color):
		results = []
		for i, stack in enumerate(self.board.stacks):
			if stack.head != None:
				if stack.head.color != color:
					results.append(i)
		return results
	
	def get_full(self):
		results = []
		for i, stack in enumerate(self.board.stacks):
			if stack.state.name == "FULL":
				results.append(i)
		return results
	
	# def check_rules(self, dices, color, start, destination):
	# 	return self.get_same_color(color)