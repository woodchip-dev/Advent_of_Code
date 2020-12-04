# AoC inputs may come in a variety of formats;
# functions to handle cases will be added as needed

# expect: file w/ one value per line
def line_to_list(file_name):
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

def separated_by_blanks(file_name):
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

