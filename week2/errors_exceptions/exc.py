def check_parent(tree, base, derived):
	"""
	check: is base parent of derived
	tree is map of classes
	return: bool
	"""
	if base == derived:
		return True
	elif not tree[derived]:
		return False
	elif base in tree[derived]:
		return True
	else:
		for parent in tree[derived]:
			if check_parent(tree, base, parent):
				return True
		return False

def read_instructions(tree:dict):
	count_input = int(input())
	for i in range(count_input):
		instr = input()
		parents = None
	
		if ':' in instr:
			current_class, parents = instr.split(':')
			current_class = current_class.strip()
			parents = parents.split(' ')
			parents.pop(0)
		else:
			current_class = instr
		tree[current_class] = parents


def read_queries(tree):
	readed_exceptions = []
	count_query = int(input())
	for i in range(count_query):
		exception = input()
		for readed_exception in readed_exceptions:
			if check_parent(tree, readed_exception, exception):
				print(exception)
				break
		readed_exceptions.append(exception)

tree = dict()
read_instructions(tree)
read_queries(tree)
