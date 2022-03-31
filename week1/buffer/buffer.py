class Buffer:
	def __init__(self):
		self.buffer = []

	def _print_five_first(self):
		sum = 0
		for i in range(5):
			sum += self.buffer.pop(0)
		print(sum)
	
	def add(self, *a):
		sum = 0
		for elem in a:
			self.buffer.append(elem)
		while len(self.buffer) >= 5:
			self._print_five_first()
	
	def get_current_part(self):
		return self.buffer