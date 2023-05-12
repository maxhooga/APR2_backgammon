from dice import Dice
from board import Board
from rock import Rock
from stack import Stack
from game import Game
from inspect import currentframe, getframeinfo
import json

def compare(message, value, value2):
	if value != value2:
		raise Exception("values not equal", value, value2)
	else:
		return True, message

def roll_dice():
	dice = Dice()
	print('random numer =', dice.roll())
	print('random numer =', dice.roll())
	print('random numer =', dice.roll())

def create_stack():
	stack = Stack('1', Rock('white', 'Peter'))
	stack.add(Rock('white', 'Pasha'))
	print(compare('create_stack', 'Peter', stack.head.name), getframeinfo(currentframe()).lineno)
	print(compare('create_stack', 'Pasha', stack.head.next.name), getframeinfo(currentframe()).lineno)
	value = stack.head.next
	print(compare('create_stack', 'Peter', value.previous.name), getframeinfo(currentframe()).lineno)

	stack2 = Stack('2')
	stack2.add(Rock('red', 'Misha'))
	print(compare('create_stack', 'Misha', stack2.head.name), getframeinfo(currentframe()).lineno)
	print(compare('create_stack', None, stack2.head.next), getframeinfo(currentframe()).lineno)

	stack3 = Stack('3')
	stack3.add(Rock('red', 'Big'))
	stack3.add(Rock('red', 'Small'))
	stack3.add(Rock('red', 'Fragile'))
	print(compare('create_stack', 'Big', stack3.head.name), getframeinfo(currentframe()).lineno)
	print(compare('create_stack', 'Small', stack3.find(2).name), getframeinfo(currentframe()).lineno)
	print(compare('create_stack', 'Fragile', stack3.find(3).name), getframeinfo(currentframe()).lineno)
	print(compare('create_stack', None, stack3.find(4)), getframeinfo(currentframe()).lineno)

def stack_get_last():
	stack = Stack('1', Rock('white', 'Vasa'))
	print(compare('stack_get_last', 'Vasa', stack.get_last().name), getframeinfo(currentframe()).lineno)

	stack.add(Rock('white', 'Serhej'))
	print(compare('stack_get_last', 'Serhej', stack.get_last().name), getframeinfo(currentframe()).lineno)

	stack.add(Rock('white', 'Zoho'))
	print(compare('stack_get_last', 'Zoho', stack.get_last().name), getframeinfo(currentframe()).lineno)

def pop():
	stack = Stack('1', Rock('white', 'Kal'))
	stack.add(Rock('white', 'Evjen'))
	stack.add(Rock('white', 'Bot'))

	poped_value = stack.pop()
	print(compare('pop', 'Bot', poped_value.name), getframeinfo(currentframe()).lineno)
	print(compare('pop', None, poped_value.previous), getframeinfo(currentframe()).lineno)
	print(compare('pop', None, poped_value.next), getframeinfo(currentframe()).lineno)

	poped_value = stack.pop()
	print(compare('pop', 'Evjen', poped_value.name), getframeinfo(currentframe()).lineno)
	print(compare('pop', None, poped_value.previous), getframeinfo(currentframe()).lineno)
	print(compare('pop', None, poped_value.next), getframeinfo(currentframe()).lineno)

	poped_value = stack.pop()
	print(compare('pop', 'Kal', poped_value.name), getframeinfo(currentframe()).lineno)
	print(compare('pop', None, poped_value.previous), getframeinfo(currentframe()).lineno)
	print(compare('pop', None, poped_value.next), getframeinfo(currentframe()).lineno)

	poped_value = stack.pop()
	print(compare('pop', None, poped_value), getframeinfo(currentframe()).lineno)

def find():
	stack = Stack('1', Rock('white', 'Evan'))
	stack.add(Rock('white', 'Artur'))
	stack.add(Rock('white', 'Dima'))

	value = stack.find(1)
	print(compare('find', 'Evan', value.name), getframeinfo(currentframe()).lineno)
	value = stack.find(2)
	print(compare('find', 'Artur', value.name), getframeinfo(currentframe()).lineno)
	value = stack.find(3)
	print(compare('find', 'Dima', value.name), getframeinfo(currentframe()).lineno)
	value = stack.find(5)
	print(compare('find', None, value), getframeinfo(currentframe()).lineno)

def shift():
	stack = Stack('1', Rock('white', 'Brian'))
	stack.add(Rock('white', 'Elizoveta'))
	stack.add(Rock('white', 'D.Brian'))

	shifted_value = stack.shift()
	print(compare('shift', 'Brian', shifted_value.name), getframeinfo(currentframe()).lineno)
	print(compare('shift', None, shifted_value.next), getframeinfo(currentframe()).lineno)
	print(compare('shift', None, shifted_value.previous), getframeinfo(currentframe()).lineno)
	print(compare('shift', None, stack.head.previous), getframeinfo(currentframe()).lineno)
	
	shifted_value = stack.shift()
	print(compare('shift', 'Elizoveta', shifted_value.name), getframeinfo(currentframe()).lineno)
	print(compare('shift', None, shifted_value.next), getframeinfo(currentframe()).lineno)
	print(compare('shift', None, shifted_value.previous), getframeinfo(currentframe()).lineno)
	print(compare('shift', None, stack.head.previous), getframeinfo(currentframe()).lineno)
	
	shifted_value = stack.shift()
	print(compare('shift', 'D.Brian', shifted_value.name), getframeinfo(currentframe()).lineno)
	print(compare('shift', None, shifted_value.next), getframeinfo(currentframe()).lineno)
	print(compare('shift', None, shifted_value.previous), getframeinfo(currentframe()).lineno)
	print(compare('shift', None, stack.head), getframeinfo(currentframe()).lineno)
	
	shifted_value = stack.shift()
	print(compare('shift', None, shifted_value), getframeinfo(currentframe()).lineno)

def create_board():
	with open("/Users/maxhoga/studing/python/project/json/init.json") as f:
		data = json.load(f)
	board = Board(data)
	print(compare('create_board', 26, len(board.stacks)), getframeinfo(currentframe()).lineno)
	print(compare('create_board', board.move_rock(1, 2), True), getframeinfo(currentframe()).lineno)
	print(compare('create_board', board.find_stack_by_i(2).head.color, 'R'), getframeinfo(currentframe()).lineno)
	print(compare('create_board', board.move_rock(1, -1), None), getframeinfo(currentframe()).lineno)

def check_state():
	with open("/Users/maxhoga/studing/python/project/json/init.json") as f:
		data = json.load(f)
	expected_states = ['BAR', 'HAS_ELEMENTS', 'EMPTY', 'EMPTY', 'EMPTY', 'EMPTY', 'FULL', 'EMPTY', 'HAS_ELEMENTS', 'EMPTY', 'EMPTY', 'EMPTY', 'FULL', 'FULL', 'EMPTY', 'EMPTY', 'EMPTY', 'HAS_ELEMENTS', 'EMPTY', 'FULL', 'EMPTY', 'EMPTY', 'EMPTY', 'EMPTY', 'HAS_ELEMENTS', 'BAR']
	board = Board(data)
	
	for i, stack in enumerate(board.stacks):
		print(compare('stack name = ' + str(stack.name), stack.state.name, expected_states[i]), getframeinfo(currentframe()).lineno)

def check_rock_count():
	with open("/Users/maxhoga/studing/python/project/json/init.json") as f:
		data = json.load(f)
	expected_counts = [0, 2, 0, 0, 0, 0, 5, 0, 3, 0, 0, 0, 5, 5, 0, 0, 0, 3, 0, 5, 0, 0, 0, 0, 2, 0]
	board = Board(data)
	for i, stack in enumerate(board.stacks):
		print(compare('stack name = ' + str(stack.name), stack.rock_count(), expected_counts[i]), getframeinfo(currentframe()).lineno)

def game():
	with open("/Users/maxhoga/studing/python/project/json/init.json") as f:
		data = json.load(f)
	game = Game(data)
	dice_roll = [1, 3]
	print(game.board.get_visual())
	print(compare('posible moves', game.posible_moves('R', 1, dice_roll), [2, 4, 5]), getframeinfo(currentframe()).lineno)
	print(compare('can i move there', game.can_i_move_there('R', 1, 2, dice_roll), True), getframeinfo(currentframe()).lineno)
	print(compare('can i move there', game.can_i_move_there('R', 1, 4, dice_roll), True), getframeinfo(currentframe()).lineno)
	print(compare('can i move there', game.can_i_move_there('R', 1, 5, dice_roll), True), getframeinfo(currentframe()).lineno)
	print(compare('can i move there', game.can_i_move_there('R', 1, 6, dice_roll), False), getframeinfo(currentframe()).lineno)
	print(compare('can i move there', game.can_i_move_there('R', 1, 0, dice_roll), False), getframeinfo(currentframe()).lineno)
	print(compare('can i move there', game.can_i_move_there('R', 1, 7, dice_roll), False), getframeinfo(currentframe()).lineno)

	print(game.posible_moves('W', 24, dice_roll))
	print(compare('posible moves', game.posible_moves('W', 24, dice_roll), [20, 21, 23]), getframeinfo(currentframe()).lineno)
	
	print(compare('can i move there', game.can_i_move_there('W', 24, 20, dice_roll), True), getframeinfo(currentframe()).lineno)
	print(compare('can i move there', game.can_i_move_there('W', 24, 21, dice_roll), True), getframeinfo(currentframe()).lineno)
	print(compare('can i move there', game.can_i_move_there('W', 24, 23, dice_roll), True), getframeinfo(currentframe()).lineno)
	print(compare('can i move there', game.can_i_move_there('W', 24, 19, dice_roll), False), getframeinfo(currentframe()).lineno)
	print(compare('can i move there', game.can_i_move_there('W', 24, 25, dice_roll), False), getframeinfo(currentframe()).lineno)
	print(compare('can i move there', game.can_i_move_there('W', 24, 15, dice_roll), False), getframeinfo(currentframe()).lineno)

def test():
	roll_dice()
	create_stack()
	stack_get_last()
	pop()
	find()
	shift()
	create_board()
	check_state()
	check_rock_count()
	game()

test()