from stack import Stack
from rock import Rock

class Board:
	def __init__(self):
		self.stacks = []
		for i in range(0, 26):
			self.stacks.append(Stack(i))

		self.stacks[1].add(Rock('R', '1'))
		self.stacks[1].add(Rock('R', '1'))

		self.stacks[12].add(Rock('R', '1'))
		self.stacks[12].add(Rock('R', '1'))
		self.stacks[12].add(Rock('R', '1'))
		self.stacks[12].add(Rock('R', '1'))
		self.stacks[12].add(Rock('R', '1'))

		self.stacks[17].add(Rock('R', '1'))
		self.stacks[17].add(Rock('R', '1'))
		self.stacks[17].add(Rock('R', '1'))

		self.stacks[19].add(Rock('R', '1'))
		self.stacks[19].add(Rock('R', '1'))
		self.stacks[19].add(Rock('R', '1'))
		self.stacks[19].add(Rock('R', '1'))
		self.stacks[19].add(Rock('R', '1'))
			
		self.stacks[24].add(Rock('W', '1'))
		self.stacks[24].add(Rock('W', '2'))
		self.stacks[13].add(Rock('W', '3'))
		self.stacks[13].add(Rock('W', '4'))
		self.stacks[13].add(Rock('W', '5'))
		self.stacks[13].add(Rock('W', '6'))
		self.stacks[13].add(Rock('W', '7'))
		self.stacks[8].add(Rock('W', '8'))
		self.stacks[8].add(Rock('W', '9'))
		self.stacks[8].add(Rock('W', '10'))
		self.stacks[6].add(Rock('W', '11'))
		self.stacks[6].add(Rock('W', '12'))
		self.stacks[6].add(Rock('W', '13'))
		self.stacks[6].add(Rock('W', '14'))
		self.stacks[6].add(Rock('W', '15'))
		

	def find_by_i(self, index):
		return self.stacks[index]
	
	def state(self):
		result = ''
		indent = ' ' + ' ' + ' '
		for rock_index in reversed(range(0, 5)):
			for stack in self.stacks:
				if (stack.name == 0 or stack.name == 25) and rock_index == 0:
					if stack.rock_count() < 10:
						result += str(stack.rock_count()) + indent
					else:
						result += str(stack.rock_count()) + ' ' + ' '
					continue
				if stack.find(rock_index):
					result += stack.find(rock_index).color + indent
				else:
					result += '.' + indent

			result += '\n'
		
		for stack in self.stacks:
			if stack.name < 10:
				result += str(stack.name) + indent
			else:
				result += str(stack.name) + ' ' + ' ' 
				
		print(result)