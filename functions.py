def value(one, two):
	v = one[1] + two[1]

	if one[1] == two[1]:
		v += 10
	return v

def royal_flush(cards):
	indices = []
	for card in cards:
		indices.append(card[0])
	if straight_flush(cards) and 14 in indices:
		return True
	return False

def straight_flush(cards):
	if flush(cards) and straight(cards):
		return True
	return False

def four_of_a_kind(cards):
	list = cards.copy()
	cards = []
	for i in list:
		cards.append(i[1])
	for card in cards:
		card_list = cards.copy()
		card_list.remove(card)
		if card in card_list:
			card_list.remove(card)
			if card in card_list:
				card_list.remove(card)
				if card in card_list:
					card_list.remove(card)
					if not card in card_list:
						cards = list
						return [True, card]
	cards = list
	return [False]

def full_house(cards):
	triplets = three_of_a_kind(cards)
	if triplets[0]:
		list = cards.copy()
		for i in range(3):
			print(i)
			list.remove(triplets[1])
		if list[0] == list[1]:
			return True
	return False

def flush(cards):
	list = cards.copy()
	cards = []
	for i in list:
		cards.append(i[0])
	cards.sort()
	for i in range(0, 5):
		if cards[i+1] != cards[i]:
			if len(cards) == 5:
				cards = list
				return False
			else:
				for j in range(1, 6):
					if cards[j+1] != cards[j]:
						if len(cards) == 6:
							cards = list
							return False
						else:
							for k in range(2, 7):
								if cards[k+1] != cards[k]:
									cards = list
									return False
								cards = list
								return True

def straight(cards):
	list = cards.copy()
	cards = []
	for i in list:
		cards.append(i[1])
	cards.sort()
	for i in range(0, 5):
		if cards[i+1] - cards[i] != 1:
			if len(cards) == 5:
				cards = list
				return False
			else:
				for j in range(1, 6):
					if cards[j+1] - cards[j] != 1:
						if len(cards) == 6:
							cards = list
							return False
						else:
							for k in range(2, 7):
								if cards[k+1] - cards[k] != 1:
									cards = list
									return False
								cards = list
								return True

def three_of_a_kind(cards):
	list = cards.copy()
	cards = []
	for i in list:
		cards.append(i[1])
	for card in cards:
		card_list = cards.copy()
		card_list.remove(card)
		if card in card_list:
			card_list.remove(card)
			if card in card_list:
				card_list.remove(card)
				if not card in card_list:
					cards = list
					return [True, card]
	cards = list
	return [False]

def two_pairs(cards):
	one_pair = pair(cards)
	list = cards.copy()
	try:
		list.remove(one_pair[1])
	except ValueError:
		pass
	if one_pair[0] and pair(list)[0]:
		return True
	return False

def pair(cards=[]):
	list = cards.copy()
	cards = []
	for i in list:
		cards.append(i[1])
	for card in cards:
		card_list = cards.copy()
		card_list.remove(card)
		if card in card_list:
			card_list.remove(card)
			if not card in card_list:
				cards = list
				return [True, card]
	cards = list
	return [False]

def high_card(cards):
	max = (0, 0)
	for i, card in enumerate(cards):
		if card[1] > max[0]:
			max = (card[1], i)
	return max[0]/100

def value_5(cards):
	if royal_flush(cards):
		return 10
	if straight_flush(cards):
		return 9
	if four_of_a_kind(cards)[0]:
		return 8
	if full_house(cards):
		return 7
	if flush(cards):
		return 6
	if straight(cards):
		return 5
	if three_of_a_kind(cards)[0]:
		return 4
	if two_pairs(cards):
		return 3
	if pair(cards)[0]:
		return 2
	return high_card(cards)

def println(list):
	for i in list:
		print(i)

def generate_combinations():
	symbols = ["h", "k", "p", "+"]
	indices = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
	cards = []

	for s in symbols:
		for i in indices:
			cards.append((s, i))

	combinations = []

	for one in cards:
		for two in cards:
			if one != two:
				v = value(one, two)
				if not (v, two, one) in combinations:
					combinations.append((v, one, two))
	combinations.sort()

	return combinations