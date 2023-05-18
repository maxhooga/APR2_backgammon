from stack import Stack
from rock import Rock

class Board:
	def __init__(self, init_data):
		self.stacks = []
		self.left_score = Stack("left score")
		self.right_score = Stack("right score")

		for i in range(0, init_data["left_score"]):
			self.left_score.add(Rock(init_data["rock_colors"][0]))
		for i in range(0, init_data["right_score"]):
			self.right_score.add(Rock(init_data["rock_colors"][1]))

		self.colors = init_data["rock_colors"]
		self.board_size = range(0, len(init_data["stacks"]))
		for stack in init_data["stacks"]:
			new_stack = Stack(stack["name"])
			for i in range(0, stack["rock_count"]):
				new_stack.add(Rock(stack["rock_color"], i))

			self.stacks.append(new_stack)

	def get_visual(self):
		state = ''
		indent = ' ' + ' ' + ' '
		for rock_index in reversed(range(1, 6)):
			for i, stack in enumerate(self.stacks):
				if (i == 0 or i == 25) and rock_index == 0:
					if stack.rock_count() < 10:
						state += str(stack.rock_count()) + indent
					else:
						state += str(stack.rock_count()) + ' ' + ' '
					continue
				
				if stack.find(rock_index):
					state += stack.find(rock_index).color + indent
				else:
					state += '.' + indent

			state += '\n'

		for i, stack in enumerate(self.stacks):
			if i < 10:
				state += str(i) + indent
			else:
				state += str(i) + ' ' + ' ' 
				
		return state

	def find_stack_by_i(self, index):
		return self.stacks[index]
	
	def move_rock(self, start, destination):
		if start in self.board_size and destination in self.board_size:
			start_stack = self.find_stack_by_i(start)
			rock = start_stack.pop()
			destination_stack = self.find_stack_by_i(destination)
			destination_stack.add(rock)
			return True
		else:
			return None
		
	def move_to_bar(self, rock):
		if rock.color == self.colors[0]:
			self.find_stack_by_i(0).add(rock)
		else:
			self.find_stack_by_i(self.board_size.stop - 1).add(rock)

