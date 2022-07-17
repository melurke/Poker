from functions import value_5

cards = []
numbers = []
symbols = []
for i in range(0,4):
	symbols.append(str(i))
for i in range(1,14):
	numbers.append(str(i))
for b in symbols:
	for i in numbers:
		
		cards.append((b,i))
combinations = []
for xi, i in enumerate(cards):
	for xb, b in enumerate(cards):
		if xi > xb:
			combinations.append((b,i))

table = []
table_combinations = []
print(cards)
for xa, a in enumerate(cards):
	print(a)
	for xb, b in enumerate(cards):
		if xa < xb:
			for xc, c in enumerate(cards):
				if xb < xc:
					for xd, d in enumerate(cards):
						if xc < xd :
							for xe, e in enumerate(cards):
								if xd < xe:
										table_combinations.append((a,b,c,d,e))
values = []
for c in combinations:
	for t in table_combinations:
		not_possible = False
		for card in c:
			if card in t:
				not_possible = True
		if not not_possible:
			print(a)
			a = list(c+t)
			k = value_5(a)
			values.append(k)
print(values)