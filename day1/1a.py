# for each line: val is first and last digit concated
#  if only one val, repeat

# Goal: sum the values


# ---
# approach, iterate from left, when found first digit then okay
# approach from right, when found first digit then okay


file1 = open('1.txt', 'r')
lines = file1.readlines()


total = 0

for line in lines:
	for i in range(len(line)):
		# left
		try:
			left = int(line[i])
			break
		except ValueError:
			continue


	for i in range(len(line) - 1, -1, -1):
		# left
		try:
			right = int(line[i])
			break
		except ValueError:
			continue
	total += int(str(left) + str(right))

print(total)

# i could have improved this by not doing 2 pass throughs for the repeated digits 