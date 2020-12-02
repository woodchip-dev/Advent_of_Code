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

