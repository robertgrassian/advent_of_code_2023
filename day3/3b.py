import math

# need to change implementation to have symbol just be *, and find parts return number and if found,

file = open('3.txt', 'r')
lines = file.readlines() # list of strings (each row)
total = 0
found = []

def run():
	for i, line in enumerate(lines):
		for j in range(len(line)):
			# check if is symbol
			if isSymbol(line[j]):
				# explore all adjacent indicies
				explore(i, j)
	print(total)

def isSymbol(c):
	return c == '*'

def explore(i,j):
	global total
	# check for words on each adjacent square
	results = []
	results.append(findPart(i-1, j-1))
	results.append(findPart(i-1, j))
	results.append(findPart(i-1, j+1))
	results.append(findPart(i, j-1))
	results.append(findPart(i, j+1))
	results.append(findPart(i+1, j-1))
	results.append(findPart(i+1, j))
	results.append(findPart(i+1, j+1))

	if sum([1 for x in results if x is not None]) == 2:
		# gear!
		total += math.prod([x for x in results if x is not None])


def findPart(i, j):
	# print("finding: " + str(i) + "," + str(j))
	if i < 0 or i >= len(lines) or j < 0 or j >= len(lines[i]):
		return None
	if (i,j) in found:
		# print("repeat")
		return None
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
		for k in range(left_index, right_index + 1):
			found.append((i,k))
		return int(lines[i][left_index:right_index + 1])
	return None


def isNumber(d):
	try:
		int(d)
		return True
	except ValueError:
		return False

run()

