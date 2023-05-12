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

	dice_rolls = dice.roll()
	format(f"Player {player_name[player]} rolled: ", f"{dice_rolls}")

	format(f"All posible moves for {colors[player]}", game.all_posible_moves(colors[player], dice_rolls))

	format(game.board.get_visual())
	format(f"make your move {player_name[player]}", "To make a move print index of a rock you want to move and index you want to move it to")
	
	p = []
	p.append(int(comunication("from")))
	p.append(int(comunication("to")))

	while not game.make_move(colors[player], p[0], p[1], dice_rolls):
		if not game.make_move(colors[player], p[0], p[1], dice_rolls):
			print("Something went wrong, i cant move there. Try again")
			p = []
			p.append(int(comunication("from")))
			p.append(int(comunication("to")))
	
	game.check_board()


def main():
	with open("/Users/maxhoga/studing/python/project/json/init.json") as f:
		data = json.load(f)
	colors = ['R', 'W']
	player_name = []
	player = 0

	session = True
	game = Game(data)
	dice = Dice()

	os.system("clear")
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


		

main()

		# print("Do you want to play a game?")
		# print("Choose: [YES] or [NO]")
		# if input().lower() == 'yes':
		# 	os.system("clear")
		# 	print("Then let\'s play")
			







		# else:
		# 	session = False