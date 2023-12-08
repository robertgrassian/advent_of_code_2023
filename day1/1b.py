# for each line: val is first and last digit, or spelled out concated
#  if only one val, repeat

# Goal: sum the values


# ---
# approach, iterate from left, if digit then easy. 
# else, check if its a word
# this can be done with a helper function, it scans to the right to see if it spells a number

# the right version will be slightly more complicated, but not really, just reverse


file1 = open('1.txt', 'r')
lines = file1.readlines()


digits = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}



def run():
	total = 0
	for line in lines:
		for i in range(len(line)):
			# left
			try:
				left = int(line[i])
				break
			except ValueError:
				# check if its a digit
				spelledDigit = getDigit(line[i:])
				if spelledDigit is not None:
					left = spelledDigit
					break
				continue


		for i in range(len(line) - 1, -1, -1):
			# left
			try:
				right = int(line[i])
				break
			except ValueError:
				# check if its a digit
				spelledDigit = getDigitReversed(line[:i+1])
				if spelledDigit is not None:
					right = spelledDigit
					break 
				continue
				
		total += int(str(left) + str(right))

	print(total)


def getDigit(text):
	# returns a digit if its spelled out, or None
	for digit in digits:
		if text[0:len(digit)] == digit:
			return digits[digit]
	return None

def getDigitReversed(text):
	# returns a digit if its spelled out, or None
	for digit in digits:
		if text[len(text) - len(digit):len(text)] == digit:
			return digits[digit]
	return None


run()