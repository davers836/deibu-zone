from sys import argv

script, input_file, output_file = argv

print "Copying from %s to %s" % (input_file, output_file)
open(output_file, 'w').write(open(input_file).read())

def break_cards(cube_export):
	"""Breaks exported MTG cube into list of cards."""
	return cube_export.split('\n')

# get a list of cards in the cube
card_list = break_cards(open(output_file).read())

# remove blank lines
if card_list[-1] == "":
	print "trimming blank line at end"
	card_list.pop(-1)
else:
	print "no blank line at end detected"

prepended_list = []
	
# iterate through each card
for c in card_list:
	# prepend "1 " to each card
	c = "1 " + c
	prepended_list.append(c)
	
# flatten the list back into a big string
results = '\n'.join(prepended_list)

# write the results back to the file
open(output_file, 'w').write(results)