## DUNNO IF THATS HOW YOU SPELL IT
## REINVENTING THE WHEEL AGAIN WITH THIS CODE 

class Queue:
	def __init__(self, capacity = 10):
		self.data = [0] * capacity
		self.front = 0
		self.back = 0
	def count(self):
		if self.front >= self.back:
			return self.front - self.back
		else:
			return self.front - self.back + len(self.data)
	def is_empty(self):
		return self.front == self.back
	def enqueue(self, item):
		if self.count() < len(self.data) - 1:
			self.data[self.front] = item
			self.front = (self.front + 1) % len(self.data)
		else:
			raise Exception("Queue Full")
	def dequeue(self):
		item = self.data[self.back]
		self.back = (self.back + 1) % len(self.data)
		return item