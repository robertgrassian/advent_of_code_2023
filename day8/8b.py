import numpy as np

class Instructions:
	def __init__(self, lines):
		self.instructions = lines[0].replace("\n", "").strip()
		self.counter = 0

	def nextInstruction(self):
		cur = self.instructions[self.counter]
		self.counter = (self.counter + 1) % len(self.instructions)
		return cur

class Node:
	def __init__(self, value):
		self.value = value

	def setNeighbors(self, left: 'Node', right: 'Node'):
		self.left = left
		self.right = right

	def getLeft(self):
		return self.left

	def getRight(self):
		return self.right

	def getValue(self):
		return self.value


def buildGraph(lines):
	labelToNode = {}
	startingNodes = []
	for i in range(2, len(lines)):
		line = lines[i]
		cur = line.replace("\n", "").split(" = ")[0]

		# now we have cur, left, right
		# TODO: only care about cur right now
		labelToNode[cur] = Node(cur)

	# now construct neighbors
	for i in range(2, len(lines)):
		line = lines[i]
		cur, neigbors = line.replace("\n", "").split(" = ")
		left, right = neigbors.replace("(", "").replace(")", "").split(", ")

		curNode = labelToNode[cur]
		if cur[-1] == "A":
			startingNodes.append(curNode)

		curNode.setNeighbors(labelToNode[left], labelToNode[right])
	return startingNodes


def run():
	file = open('8.txt', 'r')
	lines = file.readlines()

	instructions = Instructions(lines)
	nodes = buildGraph(lines)

	print("Instructions: ", instructions.instructions)
	final = "Z"

	# traverse the graph until we get to final

	def traverse(node):
		count = 0
		while node.getValue()[-1] != final:
			nextInstruction = instructions.nextInstruction()
			if nextInstruction == "L":
				node = node.getLeft()
			else:
				node = node.getRight()
			count += 1
		return count

	counts = [traverse(node) for node in nodes]
	print(counts)
	return np.lcm.reduce(counts)


print(run())