from board import Board
import json

class Game:
	def __init__(self, init_data):
		self.board = Board(init_data)
		self.players = init_data["players"]
		self.previous_moves = init_data["previous_moves"]
		self.current_playing = 0

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
			if color == self.board.colors[0]:
				all_posible_moves.append(current_position + number)
			if color == self.board.colors[1]:
				all_posible_moves.append(current_position - number)
		
		return set(self.board.board_size) - set(all_posible_moves)

	
	def get_elements_behind(self, color, current_position):
		results = []
		if color == self.board.colors[0]:
			for i, _ in enumerate(self.board.stacks):
				if current_position >= i:
					results.append(i)
		if color == self.board.colors[1]:
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
		if color == self.board.colors[0]:
			for roll in dice_rolls:
				if current_position + roll == self.board.board_size.stop - 1:
					results.append(self.board.board_size.stop - 1)

		if color == self.board.colors[1]:
			for roll in dice_rolls:
				if current_position - roll == self.board.board_size.start:
					results.append(self.board.board_size.start)

		return set(results)
	
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
	
	def make_move(self, color, start, destination, dice_rolls):
		if self.can_i_move_there(color, start, destination, dice_rolls):
			return self.board.move_rock(start, destination) 
		else:
			return None
		
	def check_first_rule(self, stack):
		return stack.stack_monolith_color()

	def check_second_rule(self):
		return self.board.find_stack_by_i(self.board.board_size.start).stack_monolith_color() or self.board.find_stack_by_i(self.board.board_size.stop - 1).stack_monolith_color()

	def check_board(self):
		left_bar = self.board.find_stack_by_i(self.board.board_size.start)
		if left_bar.rock_count():
			if not left_bar.stack_monolith_color() or left_bar.head.color == self.board.colors[1]:
				self.board.right_score.add(left_bar.pop())

		right_bar = self.board.find_stack_by_i(self.board.board_size.stop - 1)
		if right_bar.rock_count():
			if not right_bar.stack_monolith_color() or right_bar.head.color == self.board.colors[0]:
				self.board.left_score.add(right_bar.pop())

		for stack in self.board.stacks:
			if not self.check_first_rule(stack):
				self.board.move_to_bar(stack.shift())
		
	def check_win_condition(self):
		return self.board.left_score.rock_count() >= 15 or self.board.right_score.rock_count() >= 15
	
	def get_winner(self):
		if self.board.left_score.rock_count() >= 15:
			return 0
		if self.board.right_score.rock_count() >= 15:
			return 1
		return 0
		
	def save(self, path):
		stacks = []
		for stack in self.board.stacks:
			rock_color = "None"
			if stack.rock_count():
				rock_color = stack.head.color
			stacks.append(
				{
					"name": stack.name,
					"rock_color": rock_color,
					"rock_count": stack.rock_count()
				}
			)
			
		data = {
			"left_score": self.board.left_score.rock_count(),
			"right_score": self.board.right_score.rock_count(),
			"players": self.players,
			"previous_moves": self.previous_moves,
			"rock_colors": [self.board.colors[0], self.board.colors[1]],
			"stacks": stacks
		}
		with open(path, "w") as f:
			f.write(json.dumps(data, indent = 2))