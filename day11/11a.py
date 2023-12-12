from itertools import combinations

lines = open('11.txt', 'r').read().splitlines()

def prettyPrint(lines):
	for line in lines:
		print(line)

# first expand the universe
# expanding horizontaly shouldnt affect if vertical lines need to expand, so can check on same input
# then to expand it shouldnt affect numbers at all either

to_expand_horizontal = []
for i, line in enumerate(lines):
	if all([True if char == "." else False for char in line ]):
		to_expand_horizontal.append(i)

to_expand_vertical = []
for j in range(len(lines[0])):
	should_expand = True
	for i in range(len(lines)):
		if lines[i][j] != ".":
			should_expand = False
			break
	if should_expand:
		to_expand_vertical.append(j)

new_lines = []
for i, line in enumerate(lines):
	cur_line = []
	for j in range(len(lines[0])):
		cur_line.append(lines[i][j])
		# need to add an extra value to right if expand vertical
		if j in to_expand_vertical:
			cur_line.append(lines[i][j])
	# if add horixontal we copy this
	new_lines.append(cur_line)
	if i in to_expand_horizontal:
		new_lines.append(cur_line)


prettyPrint(new_lines)

# find galaxies
found_galaxies = []
for i, line in enumerate(new_lines):
	for j, char in enumerate(line):
		if char == "#":
			found_galaxies.append((i, j))

total_length = 0
pairs = list(combinations(found_galaxies, 2))
for pair in pairs:
	coord0 = pair[0]
	coord1 = pair[1]
	print("Pair: ", coord0, coord1)
	print("length: ", str(abs(coord0[0] - coord1[0]) + abs(coord0[1] - coord1[1])))
	print("******************")
	total_length += abs(coord0[0] - coord1[0]) + abs(coord0[1] - coord1[1])

print("total length: ", total_length) 



