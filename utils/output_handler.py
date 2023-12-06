# AoC outputs may come in a variety of formats;
# functions to handle cases will be added as needed

# expect: single value
def one_val_out(found, val):
	if found:
		print(val)
	else:
		print('not found')

# expect: list of values
def list_vals_out(found, vals):
	if found:
		for val in vals:
			print(val)
	else:
		print('not found')

