import math

"""
can find largest distance away if we traversed from both ends at the same time,
and then when they meet, thats the farthest. can keep a count as we go

If one dead ends, we can pause and try a different potential path
That path might right the existing one at a different count,
if so we can still calculate the farthest difference as 
B - A + 1 where B is larger number

---

coordinates i,j is

	j=0	j=1	j=2
i=0
i=1
i-2

---

I wonder if putting this in a class would be better
make a graph class that parses input, 
- saves starting location
- getNearbyPipes()
- traversePipe

nah no need for a class
"""


lines = open('10.txt', 'r').readlines()

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


def run():
	start = findStart() # (i, j)
	possible_paths = findNearPipes(start) # list of (i,j)
	print("start: ", start)
	print('*******************')
	# print(possible_paths)
	for pipe in possible_paths:
		print('pipe', pipe)
		# try this pipe
		# print("trying pipe: ", pipe)
		prev = start
		cur = pipe
		count = 1
		while True:
			# print("cur ", cur)
			if cur[0] < 0 or cur[1] < 0 or cur[0] > len(lines) or cur[1] > len(lines[cur[0]]):
				# out of bouds
				# print("out of bounds")
				break
			cur_val = lines[cur[0]][cur[1]]

			if cur_val == "S":
				# found
				return math.ceil(count / 2)
			elif cur_val == ".":
				# dead end
				print("dead end")
				break

			# print("traverse")
			# else traverse again
			count += 1
			cur_temp = cur
			cur = traverse(prev, cur)
			prev = cur_temp

print(run())










