from stack import Stack
import sys
#READ INPUT FROM A FILE
#REVERSE IT 

stack = Stack()
def reverse_input(stack_instance):
	for line in sys.stdin:
		stack_instance.push(line.strip())
	while not stack_instance.isempty():
		print(stack_instance.pop())

reverse_input(stack)

