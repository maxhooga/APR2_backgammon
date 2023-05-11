from board import Board

class Game:
	def __init__(self, init_data):
		self.board = Board(init_data)

	def get_empty(self):
		results = []
		for i, stack in enumerate(self.board.stacks):
			if stack.state.name == "EMPTY":
				results.append(i)
		return set(results)
	
	def get_has_one(self):
		results = []
		for i, stack in enumerate(self.board.stacks):
			if stack.state.name == "HAS_ONE":
				results.append(i)
		return set(results)
	
	def get_has_elements_same_color(self, color):
		results = []
		for i, stack in enumerate(self.board.stacks):
			if stack.state.name == "HAS_ELEMENTS" and stack.head.color == color:
				results.append(i)
		return set(results)
	
	def get_out_of_dice_range(self, color, dice_rolls, current_position):
		temp_list = dice_rolls.copy()
		all_posible_moves = []
		all_dice_throws = []
		all_dice_throws += temp_list
		while temp_list:
			all_dice_throws.append(sum(temp_list))
			temp_list.pop()

		for number in all_dice_throws:
			if color == 'R':
				all_posible_moves.append(current_position + number)
			if color == 'W':
				all_posible_moves.append(current_position - number)
		
		return set(self.board.board_size) - set(all_posible_moves)

	
	def get_elements_behind(self, color, current_position):
		results = []
		if color == 'R':
			for i, _ in enumerate(self.board.stacks):
				if current_position >= i:
					results.append(i)
		if color == 'W':
			for i, _ in enumerate(self.board.stacks):
				if current_position <= i:
					results.append(i)

		return set(results)
	
	def check_choosen_element(self, color, current_position):
		if self.board.find_stack_by_i(current_position).rock_count() > 0:
			if self.board.find_stack_by_i(current_position).head.color == color:
				return set()
		return set(self.board.board_size)

	def get_same_color(self, color):
		results = []
		for i, stack in enumerate(self.board.stacks):
			if stack.head != None:
				if stack.head.color == color:
					results.append(i)
		return set(results)
	
	def get_posible_out(self, color, current_position, dice_rolls):
		results = []
		if color == 'R':
			for roll in dice_rolls:
				if current_position + roll == self.board.board_size.stop - 1:
					results.append(self.board.board_size.stop - 1)

		if color == 'W':
			for roll in dice_rolls:
				if current_position - roll == self.board.board_size.start:
					results.append(self.board.board_size.start)

		return set(results)
	
	# def get_different_color(self, color):
	# 	results = []
	# 	for i, stack in enumerate(self.board.stacks):
	# 		if stack.head != None:
	# 			if stack.head.color != color:
	# 				results.append(i)
	# 	return set(results)
	
	# def get_full(self):
	# 	results = []
	# 	for i, stack in enumerate(self.board.stacks):
	# 		if stack.state.name == "FULL":
	# 			results.append(i)
	# 	return set(results)
	
	def posible_moves(self, color, current_position, dice_rolls):
		positive_set = (
			self.get_empty() |
			self.get_has_one() |
			self.get_has_elements_same_color(color) |
			self.get_posible_out(color, current_position, dice_rolls)
			)
		
		negative_set = (
			self.get_elements_behind(color, current_position) |
			self.check_choosen_element(color, current_position) |
			self.get_out_of_dice_range(color, dice_rolls, current_position)
			)

		results = list(positive_set - negative_set)
		 
		return results
	
	def can_i_move_there(self, color, current_position, destination, dice_rolls):
		return destination in self.posible_moves(color, current_position, dice_rolls)
	
	def all_posible_moves(self, color, dice_rolls):
		results = {}
		for current_position in list(self.get_same_color(color)):
			results[current_position] = self.posible_moves(color, current_position, dice_rolls)

		return results