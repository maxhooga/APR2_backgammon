from game import Game
from dice import Dice
import os
import time
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

def cycle(player, colors, player_name, game, dice):
	os.system("clear")
	format(f"{player_name[player]} playing as {colors[player]}", "NOW MOVE!")
	format(f"{player_name[0]}:{player_name[1]}", f"{game.board.left_score.rock_count()}:{game.board.right_score.rock_count()}")
	
	dice_rolls = dice.roll()
	format(f"Player {player_name[player]} rolled: ", f"{dice_rolls}")

	format(f"All posible moves for {colors[player]}", game.all_posible_moves(colors[player], dice_rolls))

	format(game.board.get_visual())
	format(f"make your move {player_name[player]}", "To make a move print index of a rock you want to move and index you want to move it to")
	
	p = []
	p.append(int(comunication("from").replace(" ", "")))
	p.append(int(comunication("to").replace(" ", "")))

	while not game.make_move(colors[player], p[0], p[1], dice_rolls):
		if not game.make_move(colors[player], p[0], p[1], dice_rolls):
			print("Something went wrong, i cant move there. Try again")
			p = []
			p.append(int(comunication("from").replace(" ", "")))
			p.append(int(comunication("to").replace(" ", "")))
	
	game.check_board()
	game.save("python/project/json/save.json")

def show_win(player_name, game):
	format(f"CONGRATS {player_name[game.get_winner()]} WON")

	format("STATISTICS")
	print("score:")
	format(f"{player_name[0]}:{player_name[1]}", f"{game.board.left_score.rock_count()}:{game.board.right_score.rock_count()}")
	format(f"LEFT BAR = {game.board.find_stack_by_i(0).rock_count()}")
	format(f"RIGHT BAR = {game.board.find_stack_by_i(game.board.board_size.stop - 1).rock_count()}")



def main():
	path = "python/project/json/init.json"

	os.system("clear")
	format("Do you want to start new game or continue.", "Print new or continue.")
	p = input().lower()

	if p == "continue":
		path = "python/project/json/save.json"

	with open(path) as f:
		data = json.load(f)

	colors = ['R', 'W']
	player_name = []
	player = 0
	dice = Dice()
	session = True

	game = Game(data)

	os.system("clear")
	print("Do you want to play a game?")
	player_name.append(comunication("First player name:"))
	os.system("clear")
	player_name.append(comunication("Second player name:"))

	while session:
		if player == 0:
			cycle(player, colors, player_name, game, dice)
			player = 1
		else:
			cycle(player, colors, player_name, game, dice)
			player = 0
		
		if game.check_win_condition():
			os.system("clear")
			show_win(player_name, game)
			session = False

main()

		# print("Do you want to play a game?")
		# print("Choose: [YES] or [NO]")
		# if input().lower() == 'yes':
		# 	os.system("clear")
		# 	print("Then let\'s play")
			

		# else:
		# 	session = False