
file = open('4.txt', 'r')
lines = file.readlines()


def transformNumsToList(line):
	return line.strip().replace("  ", " ").split(" ")

def run():
	total = 0
	for i, line in enumerate(lines):
		nums = (line.split(":")[1]).split("|")
		winningNums = transformNumsToList(nums[0])
		myNums = transformNumsToList(nums[1])

		count = sum([1 for x in myNums if x in winningNums])
		if count != 0:
			# print("Total for row " + str(i+1) + ": " + str(2 ** (count - 1)))
			total += 2 ** (count - 1)
	print(total)

run()