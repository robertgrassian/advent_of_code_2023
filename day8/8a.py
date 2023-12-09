import sys
sys. setrecursionlimit(100000)
	

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
	startingNode = None # should be AAA when found
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
		if cur == "AAA":
			startingNode = curNode

		curNode.setNeighbors(labelToNode[left], labelToNode[right])
	return startingNode




def run():
	file = open('8.txt', 'r')
	lines = file.readlines()

	instructions = Instructions(lines)
	node = buildGraph(lines)

	print("Instructions: ", instructions.instructions)
	print("Starting Node: ", node.getValue())

	final = "ZZZ"

	# traverse the graph until we get to final

	def traverse(node, count):
		if node.getValue() == final:
			return count

		nextInstruction = instructions.nextInstruction()
		if nextInstruction == "L":
			return traverse(node.getLeft(), count + 1)
		else:
			return traverse(node.getRight(), count + 1)


	return traverse(node, 0)




print(run())