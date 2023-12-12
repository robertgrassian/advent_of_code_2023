import math

"""
strategy: when im at a pipe, explore neighboring .s and find all of them, adding cooridinates to a list.
if it touches the outside, add them to a outside list. If they dont, add them to an inside list.

At the end, sum the coordinates in the inside list
"""


lines = open('10.txt', 'r').readlines()
lines = [l.replace("\n", "") for l in lines]

def isAbove(start, end):
	return start[0] + 1 == end[0]

def isBelow(start, end):
	return start[0] - 1 == end[0]

def isLeft(start, end):
	return start[1] + 1 == end[1]

def isRight(start, end):
	return start[1] - 1 == end[1]

def getVal(coordinate):
	return lines[coordinate[0]][coordinate[1]]

def traverse(prev, cur):
	# TODO: probably shouldbe start, pipe, returns destination
	# returns next coordinate after pipe
	val = getVal(cur)
	if val == "|":
		# up or down
		if isAbove(prev, cur):
			return cur[0] + 1, cur[1]
		elif isBelow(prev, cur):
			return cur[0] - 1, cur[1]
	elif val == "-":
		# left or right
		if isLeft(prev, cur):
			return cur[0], cur[1] + 1
		elif isRight(prev, cur):
			return cur[0], cur[1] - 1
	elif val == "L":
		# up or right
		if isAbove(prev, cur):
			return cur[0], cur[1] + 1
		elif isRight(prev, cur):
			return cur[0] - 1, cur[1]
	elif val == "J":
		# up or left
		if isAbove(prev, cur):
			return cur[0], cur[1] - 1
		elif isLeft(prev, cur):
			return cur[0] - 1, cur[1]
	elif val == "7":
		# left or down
		if isLeft(prev, cur):
			return cur[0] + 1, cur[1]
		elif isBelow(prev, cur):
			return cur[0], cur[1] - 1
	elif val == "F":
		# right or down
		if isRight(prev, cur):
			return cur[0] + 1, cur[1]
		elif isBelow(prev, cur):
			return cur[0], cur[1] + 1
	return None


def findStart():
	for i, line in enumerate(lines):
		for j, char in enumerate(line):
			if char == "S":
				return (i,j)


def findNearPipes(coordinate):
	i, j = coordinate
	possible = [(i-1, j), (i+1, j), (i, j+1), (i, j-1)]
	finals = []
	for possible_pipe in possible:
		if traverse(coordinate, possible_pipe) != None:
			finals.append(possible_pipe)
	return finals

def replaceHorizontal(pipes):
	# TOOD test
	new = ""
	prev = None
	for i in range(1, len(pipes)):
		prev = pipes[i-1]
		cur = pipes[i]
		if (prev == "L" and cur == "J") or (prev == "F" and cur == "7"):
			# skip these
			i += 1
			prev = None
		else:
			new += prev
	if prev != None:
		new += prev
	return new

def replaceVertical(pipes):
	# TOOD test
	new = ""
	prev = None
	for i in range(1, len(pipes)):
		prev = pipes[i-1]
		cur = pipes[i]
		if (prev == "F" and cur == "L") or (prev == "7" and cur == "J"):
			# skip these
			i += 1
			prev = None
		else:
			new += prev
	if prev != None:
		new += prev
	return new



def isInside(cur, edges, direction_to_check):
	# TODO: I have a bug. If a point is on the same axis as an edge it doesnt work correcty
	# check if cur is inside the loop
	count = 0
	specials = ""
	# l_count = 0
	# f_count = 0
	# seven_count = 0
	# j_count = 0

	if direction_to_check == "up":
		for i in range(cur[0]):
			val = lines[i][cur[1]]
			if (i, cur[1]) in edges and val != "|":
				if val == "7" or val == "L" or val == "F" or val == "J":
					specials += val
				else:
					count += 1
		# add counts of special
		if len(specials) % 2 != 0:
			print('wrong assumption')
		# specials = specials.replace("FL", "").replace("7J", "")
		specials = replaceVertical(specials)
		count += len(specials) / 2
	elif direction_to_check == "down":
		for i in range(cur[0] + 1, len(lines)):
			val = lines[i][cur[1]]
			if (i, cur[1]) in edges and val != "|":
				if val == "7" or val == "L" or val == "F" or val == "J":
					specials += val
				else:
					count += 1
		# add counts of special
		if len(specials) % 2 != 0:
			print('wrong assumption')
		# specials = specials.replace("FL", "").replace("7J", "")
		specials = replaceVertical(specials)
		count += len(specials) / 2
	elif direction_to_check == "left":
		for j in range(cur[1]):
			val = lines[cur[0]][j]
			if (cur[0], j) in edges and val != "-":
				if val == "7" or val == "L" or val == "F" or val == "J":
					specials += val
				else:
					count += 1
		# add counts of special
		if len(specials) % 2 != 0:
			print('wrong assumption')
		# specials = specials.replace("LJ", "").replace("F7", "")
		specials = replaceHorizontal(specials)
		count += len(specials) / 2
	elif direction_to_check == "right":
		for j in range(cur[1] + 1, len(lines[cur[0]])):
			val = lines[cur[0]][j]
			if (cur[0], j) in edges and val != "-":
				if val == "7" or val == "L" or val == "F" or val == "J":
					specials += val
				else:
					count += 1
		# add counts of special
		if len(specials) % 2 != 0:
			print('wrong assumption')
		# specials = specials.replace("LJ", "").replace("F7", "")
		specials = replaceHorizontal(specials)
		count += len(specials) / 2
	else:
		print("something went wrong")
		return None

	# print(count)
	# print(l_count)
	# print(j_count)
	# print(f_count)
	# print(seven_count)
	return count % 2 == 1

def getStartSide(start, pipe):
	if start[1] < pipe[1]:
		# right
		return "right"
	elif pipe[1] < start[1]:
		return "left"
	elif start[0] < pipe[0]:
		# down
		return "down"
	elif pipe[0] < start[0]:
		# up
		return "up"
	else:
		print("an error happened finding start side")

def translateBySides(direction1, direction2):
	# return val that touches the sides
	# they can be reflective
	if (direction1 == "up" and direction2 == "down") or (direction2 == "up" and direction1 == "down"):
		return "|"
	elif (direction1 == "up" and direction2 == "right") or (direction2 == "up" and direction1 == "right"):
		return "L"
	elif (direction1 == "up" and direction2 == "left") or (direction2 == "up" and direction1 == "left"):
		return "J"
	elif (direction1 == "down" and direction2 == "right") or (direction2 == "down" and direction1 == "right"):
		return "F"
	elif (direction1 == "down" and direction2 == "left") or (direction2 == "down" and direction1 == "left"):
		return "7"
	elif (direction1 == "left" and direction2 == "right") or (direction2 == "left" and direction1 == "right"):
		return "-"
	else:
		print("error when translating s")


def getEdges(start):
	global lines
	possible_paths = findNearPipes(start) # list of (i,j)
	print("start: ", start)
	print('*******************')
	for pipe in possible_paths:
		print('pipe', pipe)

		# get start side
		start_side = getStartSide(start, pipe)

		# try this pipe
		# print("trying pipe: ", pipe)
		prev = start
		cur = pipe
		edges = [start]
		while True:
			if cur[0] < 0 or cur[1] < 0 or cur[0] >= len(lines) or cur[1] >= len(lines[cur[0]]):
				# out of bouds
				# print("out of bounds")
				break
			cur_val = lines[cur[0]][cur[1]]

			if cur_val == "S":
				# found
				# translate S
				end_side = getStartSide(start, prev)
				translated_val = translateBySides(start_side, end_side)
				original_line = lines[cur[0]]
				new_line = original_line[:cur[1]] + translated_val + original_line[cur[1] + 1:]
				lines = [new_line if l == original_line else l for l in lines]
				return edges
			elif cur_val == ".":
				# dead end
				print("dead end")
				break

			edges.append(cur)
			# print("traverse")
			# else traverse again
			cur_temp = cur
			cur = traverse(prev, cur)
			prev = cur_temp


def exploreNeigbors(coordinate, edges, inside):
	"""
	for each of the 4 neighbors:
		check if it is a ".". not in inside list, and is inside polygon.
		if so, add it and every "." it touches to inside
	"""

	# up
	i = coordinate[0] - 1
	j = coordinate[1]
	if i >= 0 and j >= 0 and i < len(lines) and j < len(lines[i]):
		val = lines[i][j]
		if val == "." and (i, j) not in inside and isInside((i, j), edges, "down"):
			# inside! add this and all neighboring .s to inside list
			print("inside! down ", (i, j))
			inside = addToInside((i, j), inside)

	# down
	i = coordinate[0] + 1
	j = coordinate[1]
	if i >= 0 and j >= 0 and i < len(lines) and j < len(lines[i]):
		val = lines[i][j]
		if val == "." and (i, j) not in inside and isInside((i, j), edges, "up"):
			# inside! add this and all neighboring .s to inside list
			print("inside! up ", (i, j))
			inside = addToInside((i, j), inside)

	# left
	i = coordinate[0]
	j = coordinate[1] - 1
	if i >= 0 and j >= 0 and i < len(lines) and j < len(lines[i]):
		val = lines[i][j]
		if val == "." and (i, j) not in inside and isInside((i, j), edges, "right"):
			# inside! add this and all neighboring .s to inside list
			print("inside! right ", (i, j))
			inside = addToInside((i, j), inside)

	# right
	i = coordinate[0]
	j = coordinate[1] + 1
	if i >= 0 and j >= 0 and i < len(lines) and j < len(lines[i]):
		val = lines[i][j]
		if val == "." and (i, j) not in inside and isInside((i, j), edges, "left"):
			# inside! add this and all neighboring .s to inside list
			print("inside! left ", (i, j))
			inside = addToInside((i, j), inside)

def addToInside(coordinate, inside):
	# add this and all neigbboring ".s" to list
	i, j = coordinate
	if i >= 0 and j >= 0 and i < len(lines) and j < len(lines[i]) and lines[i][j] == "." and coordinate not in inside:
		# success! 
		inside.append(coordinate)
		# add neighbors
		inside = addToInside((i+1, j), inside)
		inside = addToInside((i-1, j), inside)
		inside = addToInside((i, j+1), inside)
		inside = addToInside((i, j-1), inside)
		return inside
	else:
		return inside



def run():
	start = findStart() # (i, j)
	edges = getEdges(start)
	print(lines)

	# now loop back over edges and explore
	inside = []
	for coordinate in edges:
		# explore the 4 neighbors
		exploreNeigbors(coordinate, edges, inside)

	return len(inside)
	

print(run())










