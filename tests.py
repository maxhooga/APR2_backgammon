from dice import Dice
from board import Board
from rock import Rock
from stack import Stack
from inspect import currentframe, getframeinfo

def compare(message, value, value2):
	return value == value2, message

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
	print(compare('create_stack', 'Small', stack3.find(1).name), getframeinfo(currentframe()).lineno)
	print(compare('create_stack', 'Fragile', stack3.find(2).name), getframeinfo(currentframe()).lineno)
	print(compare('create_stack', None, stack3.find(3)), getframeinfo(currentframe()).lineno)

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

	value = stack.find(0)
	print(compare('find', 'Evan', value.name), getframeinfo(currentframe()).lineno)
	value = stack.find(1)
	print(compare('find', 'Artur', value.name), getframeinfo(currentframe()).lineno)
	value = stack.find(2)
	print(compare('find', 'Dima', value.name), getframeinfo(currentframe()).lineno)
	value = stack.find(4)
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
	board = Board()
	print(compare('create_board', 26, len(board.stacks)), getframeinfo(currentframe()).lineno)
	print(board.get_state())
	print(compare('create_board', board.move_rock(1, 2), True), getframeinfo(currentframe()).lineno)
	print(compare('create_board', board.find_stack_by_i(2).head.color, 'R'), getframeinfo(currentframe()).lineno)
	print(compare('create_board', board.move_rock(1, -1), None), getframeinfo(currentframe()).lineno)
	print(board.get_state())



def test():
	roll_dice()
	create_stack()
	stack_get_last()
	pop()
	find()
	shift()
	create_board()

test()