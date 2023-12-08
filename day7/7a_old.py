from functools import cmp_to_key

# we are going to need to sort by hand eventually, that means a comparator,
# but if we assign a numerical value from the begining itll be easy

FIVE_OF_A_KIND = 6
FOUR_OF_A_KIND = 5
FULL_HOUSE = 4
THREE_OF_A_KIND = 3
TWO_PAIR = 2
ONE_PAIR = 1
HIGH_CARD = 0

CARD_VALUES = {"2":0, "3":1, "4":2, "5":3, "6":4, "7":5, "8":6, "9":7, "T":8, "J":9, "Q":10, "K":11, "A":12}

class Hand:
	def __init__(self, hand, handType, bid):
		self.hand = hand
		self.handType = handType
		self.bid = bid


def run():
	file = open('7.txt', 'r')
	lines = file.readlines() # list of strings (each row)
	hands = []
	for line in lines:
		hand, bid = parse(line)

		handType = getType(hand)

		handObj = Hand(hand, handType, bid)
		hands.append(handObj)

	# need to rank them
	hands.sort(key=lambda x: x.handType)
	# now they are sorted from lowest to highest
	# i need to assign a rank to each, starting with 1 and going up
	# but if two (or more) hands have the same type, i need to special compare them (will probably be a recursive function)


	# go through each and see how many in a row share a handType, then sort those, repeat

	finalSort = []
	curHands = []
	curType = -1
	for hand in hands:
		print("final sort: ", finalSort)
		print("sorting hand: ", hand.hand)
		if curType == -1 or curType == hand.handType:
			curHands.append(hand)
			print("trying")
		else:
			# the next type is different then this
			print("break")
			finalSort.extend(sortSameType(curHands))
			curHands = [hand]
		print("----------")
		curType = hand.handType
	if len(curHands) != 0:
		finalSort.extend(sortSameType(curHands))

	# now they are properly sorted, so score them
	total = 0
	rank = 1
	for hand in finalSort:
		total += rank * int(hand.bid)
		rank += 1
	return total



def sortSameType(hands):
	if len(hands) == 1:
		return hands
	else:
		# sort them
		# maybe a custom comparator on the card types
		return sorted(hands, key=cmp_to_key(secondOrder))

def secondOrder(hand1, hand2):
	return secondOrderCardHand(hand1.hand, hand2.hand)
	



def secondOrderCardHand(cardHand1, cardHand2):
	# compare each letter
	handSize = len(cardHand1)
	for i in range(handSize):
		card1 = cardHand1[i]
		card2 = cardHand2[i]
		comped = cardCompare(card1, card2)
		if comped != 0:
			return comped
		else:
			# same, so move on
			if handSize == 1:
				return 0
			# TODO bug here because its expecting cards 
			return secondOrderCardHand(cardHand1[1:], cardHand2[1:])




def cardCompare(card1, card2):
	if CARD_VALUES[card1] < CARD_VALUES[card2]:
		return -1
	elif CARD_VALUES[card1] > CARD_VALUES[card2]:
		return 1
	else:
		return 0
	



def getType(hand):
	# reutrn if five of a kind, four of a kind, etc (NUMBERS)
	# can do this by finding what is similar
	handSorted = sorted(hand)
	kinds = {}  # handSize -> count
	curHand = ""
	for char in handSorted:
		if curHand != "" and char != curHand[-1]:
			handSize = len(curHand)
			if handSize != 1:
				kinds[handSize] = 1 + kinds.get(handSize, 0)
			curHand = char
		else:
			# char is same as last
			curHand += char
	if curHand != "" and len(curHand) > 1:
		kinds[len(curHand)] = 1 + kinds.get(len(curHand), 0)

	print(hand)
	print(kinds)
	print("--------")

	# now determine type
	# five of a kind
	if kinds.get(5, 0) != 0:
		return FIVE_OF_A_KIND
	elif kinds.get(4, 0) != 0:
		return FOUR_OF_A_KIND
	elif kinds.get(3, 0) != 0 and kinds.get(2, 0) != 0:
		return FULL_HOUSE
	elif kinds.get(3, 0) != 0:
		return THREE_OF_A_KIND
	elif kinds.get(2, 0) == 2:
		return TWO_PAIR
	elif kinds.get(2, 0) == 1:
		return ONE_PAIR
	else:
		return HIGH_CARD



				




def parse(line):
	return line.replace("\n", "").split(" ")





print("Total", run())
