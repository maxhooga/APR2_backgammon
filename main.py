from game import Game
from dice import Dice
import os
from bot import Bot
import json

######## RULES
#1 if 'rock' 'W/R' is under rock 'R/W' then 'W/R' go to 'bar'
#2 if 'rock' went to 'bar' by moving. 'rock' goes to 'out stack'
#3 if 'stack' 'has elements' only 'rock' with the same color can go there
#4 cant be more then 5 rocks in stack
#5 cant move 'rock' to the 'full stack'
#6 cant move 'rock' without 'dice roll'
#7 who moves all 15 rocks out of board wins
#8 if dice has same roll. roll doubles
######## RULES

def format(title, content = ''):
	print(title) 
	print(content)
	if content:
		print('\n')

def comunication(question):
	print(question)
	return input()

def cycle(game, dice):
	game.save("json/save.json")
	os.system("clear")
	format(f"{game.players[game.current_playing]} playing as {game.board.colors[game.current_playing]}", "NOW MOVE!")
	format(f"{game.players[0]}:{game.players[1]}", f"{game.board.left_score.rock_count()}:{game.board.right_score.rock_count()}")
	
	dice_rolls = dice.roll()
	format(f"Player {game.players[game.current_playing]} rolled: ", f"{dice_rolls}")

	format(f"All posible moves for {game.board.colors[game.current_playing]}", game.all_posible_moves(game.board.colors[game.current_playing], dice_rolls))

	format(game.board.get_visual())
	format(f"make your move {game.players[game.current_playing]}")
	format(f"previous step: ", f"from {game.previous_moves[0]} to {game.previous_moves[1]}")
	
	p = []
	
	if game.players[game.current_playing] == "bot":
		bot = Bot()
		p = bot.pick_random(game, dice_rolls)
		if not game.make_move(game.board.colors[game.current_playing], p[0], p[1], dice_rolls):
			raise Exception("bot failed")
	else:	
		p.append(int(comunication("from").replace(" ", "")))
		p.append(int(comunication("to").replace(" ", "")))

		while not game.make_move(game.board.colors[game.current_playing], p[0], p[1], dice_rolls):
			if not game.make_move(game.board.colors[game.current_playing], p[0], p[1], dice_rolls):
				print("Something went wrong, i cant move there. Try again")
				p = []
				p.append(int(comunication("from").replace(" ", "")))
				p.append(int(comunication("to").replace(" ", "")))

	game.previous_moves[0] = p[0]
	game.previous_moves[1] = p[1]
	
	game.check_board()

def show_win(game):
	format(f"CONGRATS {game.players[game.get_winner()]} WON")
	format("STATISTICS")
	print("score:")
	format(f"{game.players[0]}:{game.players[1]}", f"{game.board.left_score.rock_count()}:{game.board.right_score.rock_count()}")
	format(f"LEFT BAR = {game.board.find_stack_by_i(0).rock_count()}")
	format(f"RIGHT BAR = {game.board.find_stack_by_i(game.board.board_size.stop - 1).rock_count()}")

def init_game():
	path = ""
	game = ""
	
	os.system("clear")
	format("Do you want to start new game or continue.", "Print new or continue.")
	p = input().lower()

	if p == "new":
		path = "json/init.json"

	if p == "continue":
		path = "json/save.json"

	with open(path) as f:
		data = json.load(f)
	
	if p == "continue":
		game = Game(data)

	if p == "new":
		game = Game(data)
		os.system("clear")
		print("Do you want to play a game?")
		game.players.append(comunication("First player name:"))
		os.system("clear")
		game.players.append(comunication("Second player name:"))

	return game


def main():
	game = init_game()

	dice = Dice()
	session = True

	while session:
		if game.current_playing == 0:
			cycle(game, dice)
			game.current_playing = 1
		else:
			cycle(game, dice)
			game.current_playing = 0
		
		if game.check_win_condition():
			os.system("clear")
			show_win(game)
			session = False

main()