# num of winning myNums (n) gives a copy of the next n cards

# goal: get total num of scratch cards

# approach: I can calc num of wins per card
# keep track of number of copies of each card (starting with 1). I only need to run it for each card once and then just add a copy to each following card for each copy of the current card


file = open('4.txt', 'r')
lines = file.readlines()


def transformNumsToList(line):
	return line.strip().replace("  ", " ").split(" ")

def mapIncr(numCards, j, numCopies):
	# increment the count of card j by numCopies
	if j not in numCards.keys():
		numCards[j] = 1
	numCards[j] += numCopies

def run():
	numCards = {}
	for i, line in enumerate(lines):
		if i not in numCards.keys():
			numCards[i] = 1

		# process
		nums = (line.split(":")[1]).split("|")
		winningNums = transformNumsToList(nums[0])
		myNums = transformNumsToList(nums[1])

		# count wins
		count = sum([1 for x in myNums if x in winningNums])
		for j in range(1, count + 1):
			mapIncr(numCards, i + j, numCards[i])

	print(sum(numCards.values()))

run()