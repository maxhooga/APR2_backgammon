from rock import Rock

class Stack:
	def __init__(self, name, head = None):
		self.name = name
		self.head = head

	def get_last(self):
		if self.head:
			value = self.head
			while value.next!= None:
				value = value.next
			return value
		raise Exception('Stack is empty')
	
	def find(self, index):
		if self.head:
			value = self.head
			flag = 0
			while flag != index:
				if value.next == None:
					return None
				value = value.next
				flag += 1
			return value
		return self.head

	def add(self, rock: Rock):
		if self.head:
			last_rock = self.get_last()
			last_rock.next = rock
			rock.previous = last_rock
			return
		self.head = rock

	def pop(self):
		poped_value = self.get_last()
		previous_value = poped_value.previous
		poped_value.previous = None
		previous_value.next = None
		return poped_value

