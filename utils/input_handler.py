# AoC inputs may come in a variety of formats;
# functions to handle cases will be added as needed

# expect: file w/ one value per line
def lines_to_lists(file_name):
	# open file
	file_in = open(file_name, 'r')
	lines = file_in.readlines()
	
	# strip whitespace
	data = []
	for line in lines:
		if not line.strip() == '':
			data.append(line.strip())
	
	# expect: list of line values w/o whitespace
	return data

# expect: file w/ multiple values per line
def delimited_lines_to_lists(file_name, delimiter):
	# open file
	file_in = open(file_name, 'r')
	lines = file_in.readlines()
	
	# strip whitespace
	data = []
	for line in lines:
		if not line.strip() == '':
			data.append(line.strip().split(delimiter))
	
	# expect: list of line values w/o whitespace
	return data

# expect: file w/ one value per line
def lines_to_ints(file_name):
	# open file
	file_in = open(file_name, 'r')
	lines = file_in.readlines()
	
	# strip whitespace
	data = []
	for line in lines:
		if not line.strip() == '':
			data.append(int(line.strip()))
	
	# expect: list of line values w/o whitespace
	return data

def lines_to_grid(file_name):
	# open file
	file_in = open(file_name, 'r')
	lines = file_in.readlines()
	
	# strip whitespace
	data = []
	for line in lines:
		if not line.strip() == '':
			data.append([num for num in [*line.strip()]])
	
	# expect: list of line values w/o whitespace
	return data

def lines_to_int_grid(file_name):
	# open file
	file_in = open(file_name, 'r')
	lines = file_in.readlines()
	
	# strip whitespace
	data = []
	for line in lines:
		if not line.strip() == '':
			data.append([int(num) for num in [*line.strip()]])
	
	# expect: list of line values w/o whitespace
	return data

# expect: file w/ one comma-separated line
def commas_to_lists(file_name):
	# open file
	file_in = open(file_name, 'r')
	line = file_in.readline()
	
	# strip whitespace, split
	data = line.strip().split(',')
	
	# expect: list of line values w/o whitespace
	return data

# expect: file w/ same groups of lines separated by blank line
def congruous_groups(file_name):
	# open file
	file_in = open(file_name, 'r')
	lines = file_in.readlines()
	lines.append('\n')

	# strip whitespace
	data, temp = [], ''
	for line in lines:
		if not line.strip() == '':
			temp += '{} '.format(line.strip())
		else:
			data.append(temp[:-1])
			temp = ''
	
	# expect: list of values w/o whitespace
	return data

# expect: file w/ same groups of lines separated by blank line
def congruous_groups_to_lists(file_name):
	# open file
	file_in = open(file_name, 'r')
	lines = file_in.readlines()

	# strip whitespace, format as lists
	data, items, temp = [], [], ''
	for line in lines:
		if not line.strip() == '':
			temp += '{} '.format(line.strip())
		else:
			items.append(temp[:-1])
			temp = ''
	for item in items:
		data.append(item.split())
	
	# expect: lists of lists of values w/o whitespace
	return data

# expect: file w/ different groups of lines separated by blank line
def different_groups(file_name):
	# open file
	file_in = open(file_name, 'r')
	lines = file_in.readlines()
	lines.append('\n')

	# strip whitespace
	data, temp = [], []
	for line in lines:
		if not line.strip() == '':
			temp.append(line.rstrip())
		else:
			data.append(temp)
			temp = []
	
	# expect: list of values w/o whitespace
	return data

