# for each game, determine if it would be possible
# sum the ids of possible games

totals = {'red': 12, 'green': 13, 'blue': 14}


def run():
	file = open('2.txt', 'r')
	lines = file.readlines()

	total = 0
	for line in lines:
		gameId, colonIndex = getId(line)
		subGames = [x.strip() for x in line[colonIndex + 2:].split(';')]
		valid = True
		for subGame in subGames:
			counts = parse(subGame)
			if 'blue' in counts.keys() and counts['blue'] > totals['blue']:
				valid = False
				break
			if 'red' in counts.keys() and counts['red'] > totals['red']:
				valid = False
				break
			if 'green' in counts.keys() and counts['green'] > totals['green']:
				valid = False
				break
		if valid:
			total += gameId
	print(total)
		


def getId(string):
	# returns id num, and index of colon
	# starts at index 5
	i = 5
	while string[i+1] != ':':
		i += 1 
	return int(string[5:i+1]), i+1

def parse(game):
	# parse game and create map of counts
	counts = {}
	# get first 
	digit = getDigit(game)
	# check color
	end_index = len(str(digit)) + 1
	if game[end_index] == 'b':
		counts['blue'] = digit
		end_index += 4
	elif game[end_index] == 'r':
		counts['red'] = digit
		end_index += 3
	elif game[end_index] == 'g':
		counts['green'] = digit
		end_index += 5
	else:
		print("There is an error!")
	if (len(game) != end_index):
		# more to do!
		counts.update(parse(game[end_index+2:]))
	return counts

def getDigit(text):
	# get the digit of the text
	for i in range(1, len(text)):
		try:
			int(text[i])
		except ValueError:
			return int(text[:i])


run()