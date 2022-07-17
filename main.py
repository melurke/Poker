from functions import generate_combinations, println, value, value_5

combinations = generate_combinations()

hand = []
table = []

print("Hand:")
for i in range(2):
	hand.append((input("What is the symbol of the card? "), int(input("What is the value of the card? "))))

for c in combinations.copy():
	if (hand[0] in c or hand[1] in c) and not (hand[0] in c and hand[1] in c):
		combinations.remove(c)

try:
	probability = (combinations.index((value(hand[0], hand[1]), hand[0], hand[1]))+1)/len(combinations)
except ValueError:
	probability = (combinations.index((value(hand[0], hand[1]), hand[1], hand[0]))+1)/len(combinations)
if probability < 0.1:
	probability = ("0" +str(probability*100))[0:5] + "%"
else:
	probability = str(probability*100)[0:5] + "%"

print(probability)

print("Table:")
for i in range(3):
	table.append((input("What is the symbol of the card? "), int(input("What is the value of the card? "))))

for c in combinations.copy():
	if (table[0] in c or table[1] in c or table[2] in c) and not (table[0] in c and table[1] in c) and not (table[1] in c and table[2] in c) and not (table[0] in c and table[2] in c):
		combinations.remove(c)

table_values = []

for c in combinations:
	cards = table
	cards.append(c[1])
	cards.append(c[2])
	table_values.append(value_5(cards))
	print(table_values[-1])