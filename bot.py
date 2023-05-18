import random

class Bot:
	def __init__(self):
		self.name = "bot"

	def pick_random(self, game, dice_rolls):
		all_posible_moves = game.all_posible_moves(game.board.colors[game.current_playing], dice_rolls)
		start = random.choice(list(all_posible_moves))
		# if not all_posible_moves[start].empty:
		destination = random.choice(all_posible_moves[start])
		return [start, destination]