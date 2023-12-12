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

found_galaxies = []
to_expand_vertical = []
for j in range(len(lines[0])):
	should_expand = True
	for i in range(len(lines)):
		if lines[i][j] != ".":
			found_galaxies.append((i, j))
			should_expand = False
	if should_expand:
		to_expand_vertical.append(j)

# new_lines = []
# for i, line in enumerate(lines):
# 	cur_line = []
# 	for j in range(len(lines[0])):
# 		cur_line.append(lines[i][j])
# 		# need to add an extra value to right if expand vertical
# 		if j in to_expand_vertical:
# 			cur_line.append(lines[i][j])
# 	# if add horixontal we copy this
# 	new_lines.append(cur_line)
# 	if i in to_expand_horizontal:
# 		new_lines.append(cur_line)

EXPANSION_NUMBER = 1000000 - 1  # 1 less than "time larger"
			

total_length = 0
pairs = list(combinations(found_galaxies, 2))
for pair in pairs:
	coord0 = pair[0]
	coord1 = pair[1]


	length = abs(coord0[0] - coord1[0]) + abs(coord0[1] - coord1[1])
	# factor in expansion
	# add extra vertical traversal
	# this is added for every horizontal line needed to be added in range
	length += sum([EXPANSION_NUMBER for i in to_expand_horizontal if i in range(min(coord0[0], coord1[0]), max(coord0[0], coord1[0]))])

	length += sum([EXPANSION_NUMBER for j in to_expand_vertical if j in range(min(coord0[1], coord1[1]), max(coord0[1], coord1[1]))])

	# print("Pair: ", coord0, coord1)
	# print("length: ", length)
	# print("expansion horizontal: ", sum([EXPANSION_NUMBER for j in to_expand_vertical if j in range(min(coord0[1], coord1[1]), max(coord0[0], coord1[0]))]))
	# print("expansion vertical: ", sum([EXPANSION_NUMBER for i in to_expand_horizontal if i in range(min(coord0[0], coord1[0]), max(coord0[1], coord1[1]))]))
	# print("******************")
	total_length += length


print("total length: ", total_length) 



