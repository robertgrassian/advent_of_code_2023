# any number adjacent to a symbol (not . or number) is a part number
# need to sum all part numbers

# this reduces to just finding all the part numbers
# since they can be diagonal to a symbol we need to be smart

# ---

# Algorithm:
# iterate right->left, up->down in search of symbol
# if found, search each adjacent spot for part number (can be a helper func)
# that helper func: needs to look if the digit is a number, and then read left/right to get the full number

# we need to make sure we dont over-count, since a part number could be adjacent to 2 symbols
# so we will keep track of all indicies with already found part numbers (we could use this to not explore certain indicies too as an optimization)

file = open('3.txt', 'r')
lines = file.readlines() # list of strings (each row)
total = 0
found = []

def run():
	print(len(lines))
	for i, line in enumerate(lines):
		for j in range(len(line)):
			# check if is symbol
			if isSymbol(line[j]):
				# explore all adjacent indicies
				explore(i, j)
	print(total)

def isSymbol(c):
	return (not isNumber(c)) and (c != ".") and (c != '\n')

def explore(i,j):
	# check for words on each adjacent square
	findPart(i-1, j-1)
	findPart(i-1, j)
	findPart(i-1, j+1)
	findPart(i, j-1)
	findPart(i, j+1)
	findPart(i+1, j-1)
	findPart(i+1, j)
	findPart(i+1, j+1)


def findPart(i, j):
	# print("finding: " + str(i) + "," + str(j))
	if i < 0 or i >= len(lines) or j < 0 or j >= len(lines[i]):
		return
	if (i,j) in found:
		# print("repeat")
		return
	# explore if this index is part of a part
	# if it is, add the number to total and mark the indices in found
	if isNumber(lines[i][j]):
		# its a number, so defintiely a part but need to explore to the left and right

		# explore left
		left_index = j
		while left_index - 1 >= 0 and isNumber(lines[i][left_index - 1]):
			left_index -= 1

		# explore right
		right_index = j
		while right_index + 1 < len(lines[i]) and isNumber(lines[i][right_index + 1]):
			right_index += 1

		# number is found
		print("FOUND: " + str(i) + "," + str(left_index) + " to " + str(right_index))
		print("adding: " + lines[i][left_index:right_index + 1])
		global total
		total += int(lines[i][left_index:right_index + 1])
		# add it to found
		for k in range(left_index, right_index + 1):
			found.append((i,k))


def isNumber(d):
	try:
		int(d)
		return True
	except ValueError:
		return False

run()

