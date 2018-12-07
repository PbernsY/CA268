from stack import Stack
# READ IN A STRING AND DETERMINE 
# IF PARENTHESIS ARE BALANCED 
# USING A STACK
# IGNORE ANYTHING THAT ISNT PUNCTUATIONAL

stack = Stack()
opening = ["(", "[", "{"]
closing = [")", "]", "}"]
pairs = ["()", "{}", "[]"]
def balanced(string):
	for character in string:
		if character not in opening and character not in closing:
			continue
		if character character in opening:
			stack.push(character)
		else:
			if stack.isempty():
				return False
			else:
				if stack.pop() + character not in stack:
					return False
	return stack.isempty()
	
