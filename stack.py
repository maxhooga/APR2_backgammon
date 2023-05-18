from enum import Enum

class State(Enum):
	FULL = 1
	EMPTY = 2
	HAS_ELEMENTS = 3
	OVERFLOW = 4
	HAS_ONE = 5
	BAR = 6
	
class Stack:
	def __init__(self, name, head = None, state = State.EMPTY):		
		self.head = head
		self.name = name
		self.state = state
		self.check_state()

	def check_state(self):
		if self.name == 'bar':
			self.state = State.BAR
			return
		if self.rock_count() == 1:
			self.state = State.HAS_ONE
			return
		if self.head == None:
			self.state = State.EMPTY
			return
		if self.find(6):
			self.state = State.OVERFLOW
			return
		if self.find(5):
			self.state = State.FULL
			return
		
		self.state = State.HAS_ELEMENTS
		return

	def change_state(self, state_name):
		self.state = State[state_name]
		return self.state

	def get_last(self):
		if self.head:
			value = self.head
			while value.next!= None:
				value = value.next

			return value
		
		return None
		# raise Exception('Stack is empty')
	
	def find(self, index):
		if self.head:
			value = self.head
			flag = 0
			while flag != index - 1:

				if value.next == None:
					return None
				value = value.next
				flag += 1
			return value
		
		return self.head

	def add(self, rock = None):
		if self.head:
			last_rock = self.get_last()
			last_rock.next = rock
			rock.previous = last_rock
			self.check_state()
			return
		self.head = rock
		self.check_state()

	def pop(self):
		if self.head == None:
			self.check_state()
			return None
		if self.head.next:
			poped_value = self.get_last()
			previous_value = poped_value.previous
			poped_value.previous = None
			previous_value.next = None
			self.check_state()
			return poped_value
		if self.head:
			poped_value = self.head
			self.head = None
			self.check_state()
			return poped_value
	
	def shift(self):
		if self.head == None:
			self.check_state()
			return None
		if self.head.next:
			shifted_value = self.head
			self.head = self.head.next
			self.head.previous = None
			shifted_value.next = None
			self.check_state()
			return shifted_value
		if self.head:
			shifted_value = self.head
			self.head = None
			self.check_state()
			return shifted_value
		
	def rock_count(self):
		result = 0
		element = self.head
		while element:
			result += 1
			element = element.next
		return result
	
	def stack_monolith_color(self):
		if self.rock_count() < 2:
			return True
		
		rock = self.head
		while rock.next:
			temp = rock.next
			if rock.color != temp.color:
				return False
			rock = temp
		return True