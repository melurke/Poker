def royal_flush(cards):
	indices = []
	for card in cards:
		indices.append(card[0])
	if straight_flush(cards) and 14 in indices and 10 in indices:
		return True
	return False

def straight_flush(cards):
	if flush(cards) and straight(cards):
		return True
	return False

def four_of_a_kind(cards):
	liste = cards.copy()
	cards = []
	for i in liste:
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
						cards = liste
						return [True, card]
	cards = liste
	return [False]

def full_house(cards):
	triplets = three_of_a_kind(cards)
	if triplets[0]:
		liste = cards.copy()
		for i in range(3):
			for c in liste:
				if c[1] == triplets[1]:
					card_to_remove = c
			liste.remove(card_to_remove)
		if list[0] == list[1]:
			return True
	return False

def flush(cards):
	liste = cards.copy()
	cards = []
	for i in liste:
		cards.append(i[0])
	cards.sort()
	for i in range(0, 5):
		if cards[i+1] != cards[i]:
			if len(cards) == 5:
				cards = liste
				return False
			else:
				for j in range(1, 6):
					if cards[j+1] != cards[j]:
						if len(cards) == 6:
							cards = liste
							return False
						else:
							for k in range(2, 7):
								if cards[k+1] != cards[k]:
									cards = liste
									return False
								cards = liste
								return True

def straight(cards):
	liste = cards.copy()
	cards = []
	for i in liste:
		cards.append(int(i[1]))
	cards.sort()
	for i in range(0, 5):
		if ((cards[i+1] - cards[i]) % 13) != 1:
			if len(cards) == 5:
				cards = liste
				return False
			else:
				for j in range(1, 6):
					if ((cards[j+1] - cards[j]) % 13) != 1:
						if len(cards) == 6:
							cards = liste
							return False
						else:
							for k in range(2, 7):
								if ((cards[k+1] - cards[k]) % 13) != 1:
									cards = liste
									return False
								cards = liste
								return True

def three_of_a_kind(cards):
	liste = cards.copy()
	cards = []
	for i in liste:
		cards.append(i[1])
	for card in cards:
		card_list = cards.copy()
		card_list.remove(card)
		if card in card_list:
			card_list.remove(card)
			if card in card_list:
				card_list.remove(card)
				if not card in card_list:
					cards = liste
					return [True, card]
	cards = liste
	return [False]

def two_pairs(cards):
	one_pair = pair(cards)
	liste = cards.copy()
	try:
		liste.remove(one_pair[1])
	except:
		pass
	if one_pair[0] and pair(liste)[0]:
		return True
	return False

def pair(cards=[]):
	liste = cards.copy()
	cards = []
	for i in liste:
		cards.append(i[1])
	for card in cards:
		card_list = cards.copy()
		card_list.remove(card)
		if card in card_list:
			card_list.remove(card)
			if not card in card_list:
				cards = liste
				return [True, card]
	cards = liste
	return [False]

def high_card(cards):
	maximum = 0
	for card in cards:
		if int(card[1]) > maximum:
			maximum = int(card[1])
	return maximum/100

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