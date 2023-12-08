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

CARD_VALUES = {"J":0, "2":1, "3":2, "4":3, "5":4, "6":5, "7":6, "8":7, "9":8, "T":9, "Q":10, "K":11, "A":12}

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
		hands.append(Hand(hand, handType, bid))

	# need to sort them by rank
	finalSort = sorted(hands, key=cmp_to_key(compare))

	# now they are properly sorted by rank, so score them
	total = 0
	rank = 1
	for hand in finalSort:
		total += rank * int(hand.bid)
		rank += 1
	return total


def compare(hand1, hand2):
	if hand1.handType != hand2.handType:
		return hand1.handType - hand2.handType 
	else:
		return secondOrderCompare(hand1.hand, hand2.hand)


def secondOrderCompare(cardHand1, cardHand2):
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
			return secondOrderCompare(cardHand1[1:], cardHand2[1:])


def cardCompare(card1, card2):
	if CARD_VALUES[card1] < CARD_VALUES[card2]:
		return -1
	elif CARD_VALUES[card1] > CARD_VALUES[card2]:
		return 1
	else:
		return 0
	

def getType(hand):
	# return if five of a kind, four of a kind, etc (NUMBERS)
	# can do this by finding what is similar

	# count jacks and it will boost hands
	handSorted = sorted(hand)
	kinds = {}  # handSize -> count
	curHand = ""
	numJacks = 0
	for char in handSorted:
		if char == "J":
			numJacks += 1
		elif curHand != "" and char != curHand[-1]:
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
	# each jack will boost the score 
	if kinds.get(5, 0) != 0:
		return FIVE_OF_A_KIND
	elif kinds.get(4, 0) != 0:
		if numJacks == 1:
			return FIVE_OF_A_KIND
		else:
			return FOUR_OF_A_KIND
	elif kinds.get(3, 0) != 0 and kinds.get(2, 0) != 0:
		return FULL_HOUSE
	elif kinds.get(3, 0) != 0:
		if numJacks == 1:
			return FOUR_OF_A_KIND
		elif numJacks == 2:
			return FIVE_OF_A_KIND
		else:
			return THREE_OF_A_KIND
	elif kinds.get(2, 0) == 2:
		if numJacks == 1:
			return FULL_HOUSE
		else:
			return TWO_PAIR
	elif kinds.get(2, 0) == 1:
		if numJacks == 1:
			return THREE_OF_A_KIND
		elif numJacks == 2:
			return FOUR_OF_A_KIND
		elif numJacks == 3:
			return FIVE_OF_A_KIND
		else:
			return ONE_PAIR
	else:
		if numJacks == 1:
			return ONE_PAIR
		elif numJacks == 2:
			return THREE_OF_A_KIND
		elif numJacks == 3:
			return FOUR_OF_A_KIND
		elif numJacks >= 4:
			return FIVE_OF_A_KIND
		else:
			return HIGH_CARD


def parse(line):
	return line.replace("\n", "").split(" ")





print("Total", run())
