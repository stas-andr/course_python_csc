n = int(input())
dict_namespace = {'global': {'parent': None, 'vars': set()}}


def create(name_namespace, name_parent, dict_namespace):
	dict_namespace[name_namespace] = {'parent': name_parent, 'vars': set()}

def add(name_namespace, name_var, dict_namespace):
	dict_namespace[name_namespace]['vars'].add(name_var)

def get(name_namespace, name_var, dict_namespace):
	parent = dict_namespace[name_namespace]['parent']
	if name_var in dict_namespace[name_namespace]['vars']:
		return name_namespace
	elif not parent:
		return None
	else:
		return get(parent, name_var, dict_namespace)

def print_get(name_namespace, name_var, dict_namespace):
	print(get(name_namespace, name_var, dict_namespace))

for instruction in range(n):
	command, namespace, arg = input().split()
	if command == 'create':
		create(namespace, arg, dict_namespace)
	elif command == 'add':
		add(namespace, arg, dict_namespace)
	elif command == 'get':
		print_get(namespace, arg, dict_namespace)