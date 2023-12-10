# naive approach

def transform(original_list):
	new_list = []
	for i in range(1, len(original_list)):
		new_list.append(original_list[i] - original_list[i - 1])
	return new_list


def getPrevVal(vals):
	if all(x == 0 for x in vals):
		# all 0s
		return 0
	else:
		return vals[0] - getPrevVal(transform(vals))



lines = open('9.txt', 'r').readlines()
total = 0
for line in lines:
	# transform
	vals = [int(x) for x in line.replace("\n", "").strip().split(" ")]
	total += getPrevVal(vals)
print("Total: ", total)