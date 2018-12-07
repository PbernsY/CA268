class Stack:
	def __init__(self):
		self.stack = []


	def push(self, item):
		self.stack.append(item)

	def pop(self):
		return self.stack.pop()
	def isempty(self):
		return True if not self.stack else False

	def peek(self):
		if self.isempty():
			raise Exception("Stack Underflow")
		return self.stack[-1]
	def size(self):
		return len(self.stack)

	def show_full_stack(self):
		for item in self.stack:
			print(item, end= " ")
		print()

# non obfuscated stack implementation 


