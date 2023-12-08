import re


def run():

	file = open('6.txt', 'r')
	lines = file.readlines()

	times = [int(x) for x in re.split(r" +", lines[0].split(":")[1].strip())]
	distances = [int(x) for x in re.split(r" +", lines[1].split(":")[1].strip())]
	print(times)
	print(distances)

	# naive apporach is to try out all possible amount of time we could hold the button
	# slightly better approach is to start in middle and work out

	total = 1
	for i in range(len(times)):
		# calc num of ways we can win
		time = times[i]
		distance = distances[i]
		num_ways = 0

		# first approach is iterate over all of them
		for j in range(1,time):
			if calcDistance(j, time) > distance:
				num_ways += 1
		total *= num_ways
		print(num_ways)
	return total

def calcDistance(toHold, total):
	# for evermy ms held, speed goes up by one
	return(total - toHold) * toHold


print(run())