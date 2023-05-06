from rock import Rock
from enum import Enum

class State(Enum):
	FULL = 1
	EMPTY = 2
	HAS_ELEMENTS = 3
	OVERFLOW = 4
	
class Stack:
	def __init__(self, name, head = None, state = State.HAS_ELEMENTS):
		if isinstance(head, list):
			self.head = head[0]
			head.pop(0)
			if len(head) != 0:
				previous_element = self.head
				for element in head:
					previous_element.next = element
					element.previous = previous_element
					previous_element = element
		else:
			self.name = name
			self.head = head

		self.state = state

	def check_state(self):
		if self.head == None:
			return self.state.EMPTY
		if self.find(6):
			return self.state.OVERFLOW
		if self.find(5):
			return self.state.FULL
		
		return self.state.HAS_ELEMENTS

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
			while flag != index:

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
