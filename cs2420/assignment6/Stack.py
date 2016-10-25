class Stack:
	def __init__(self):
		self.data = []

	def Push(self, item):
		self.data.append(item)

	def Pop(self):
		returnMe = self.data[-1]
		self.data.remove(self.data[-1])
		return returnMe

	def IsEmpty(self):
		return len(self.data) == 0

	def Top(self):
		if not self.IsEmpty():
			return self.data[-1]
		else:
			return "Stack is empty"