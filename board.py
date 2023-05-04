from stack import Stack
from rock import Rock

class Board:
	def __init__(self):
		self.columns = []
		for i in range(0, 26):
			if i == 1:
				self.columns.append(Stack(i, [
					Rock('red', 'Steave'),
					Rock('red', 'Mark')
				]))
			if i == 12:
				self.columns.append(Stack(i, [
					Rock('red', 'Karl'),
					Rock('red', 'Evan'),
					Rock('red', 'Evan'),
					Rock('red', 'Michal'),
					Rock('red', 'Luci'),
					Rock('red', 'Lily')
				]))
			if i == 17:
				self.columns.append(Stack(i, [
					Rock('red', 'Scara'),
					Rock('red', 'Brian'),
					Rock('red', 'Kal')
				]))
			if i == 19:
				self.columns.append(Stack(i, [
					Rock('red', 'Karen'),
					Rock('red', 'M.Brian'),
					Rock('red', 'Karles'),
					Rock('red', 'Marie'),
					Rock('red', 'Bot')
				]))
			self.columns.append(Stack(i))

		self.columns[24].add(Rock('white', '1'))
		self.columns[24].add(Rock('white', '2'))
		self.columns[13].add(Rock('white', '3'))
		self.columns[13].add(Rock('white', '4'))
		self.columns[13].add(Rock('white', '5'))
		self.columns[13].add(Rock('white', '6'))
		self.columns[13].add(Rock('white', '7'))
		self.columns[8].add(Rock('white', '8'))
		self.columns[8].add(Rock('white', '9'))
		self.columns[8].add(Rock('white', '10'))
		self.columns[6].add(Rock('white', '11'))
		self.columns[6].add(Rock('white', '12'))
		self.columns[6].add(Rock('white', '13'))
		self.columns[6].add(Rock('white', '14'))
		self.columns[6].add(Rock('white', '15'))
		

	def find_by_i(self, index):
		return self.columns[index]
	