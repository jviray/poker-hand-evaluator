import deck as d

# Generating the Equivalence Class Table 

deck = d.Deck()
cards = deck.cards
ranks = deck.ranks
suits = deck.suits

ec_table = {}
	
# GENERATE Royal & Straight Flushes (10):
straight_flushes = []
for i, card in enumerate(cards[:10]):
	straight_flushes.append(cards[i:i+5])

# POPULATE ec_table w/ Royal & Straight Flushes 
i = 1
for flush in straight_flushes:
	key = str(i)
	ec_table[key] = flush
	
	i += 1
	
# GENERATE Four of a Kinds (156):
fours = []
for i, card in enumerate(cards[:13]):
	four = [card, cards[i+13], cards[i+26], cards[i+39]]
	
	for i2 in range(13):
		if cards[i2].rank == card.rank:
			continue
		
		four.append(cards[i2])
		fours.append(four)
		# Why won't del four[4] work?
		four = [card, cards[i+13], cards[i+26], cards[i+39]]

# POPULATE ec_table w/ Four of a Kinds
i = 11
for four in fours:
	key = str(i)
	ec_table[key] = four
	
	i += 1

# GENERATE Full Houses (156):
full_houses = []
for i, card in enumerate(cards[:13]):
	house = [card, cards[i+13], cards[i+26]]
	
	for i2 in range(13):
		if cards[i2].rank == card.rank:
			continue
		
		house.append(cards[i2])
		house.append(cards[i2+13])
		full_houses.append(house)
		house = [card, cards[i+13], cards[i+26]]

# POPULATE ec_table w/ Full Houses:
i = 167
for house in full_houses:
	key = str(i)
	ec_table[key] = house
	
	i += 1

# GENERATE Flushes (1277):
def gen_flushes():
	result = []
	for i in range(0, 9):
		flushes = []
		flush = [cards[i]]
		end = 9 if i == 0 else 10
		for i2 in range(i+1, end):
			flush.append(cards[i2])
			for i3 in range(i2+1, 11):
				flush.append(cards[i3])
				for i4 in range(i3+1, 12):
					flush.append(cards[i4])
					for i5 in range(i4+1, 13):
						flush.append(cards[i5])
						flushes.append(flush)
						flush = flush[:-1]
					flush = flush[:-1]
				flush = flush[:-1]	
			flush = flush[:-1]
		
		for num, flush in enumerate(flushes):
			if num == 0:
				continue
			else:
				result.append(flush)
	
	return result

# POPULATE ec_table w/ Flushes:
i = 323
flushes = gen_flushes()
for flush in flushes:
	key = str(i)
	ec_table[key] = flush
	
	i += 1

# GENERATE Straights (10):
def gen_straights():
	straights = []
	for i, card in enumerate(cards[:10]):
		straights.append(cards[i+14:i+18])
		straights[-1].insert(0, card)
	
	return straights

# POPULATE ec_table w/ Straights:
i = 1600 
straights = gen_straights()
for straight in straights:
	key = str(i)
	ec_table[key] = straight
	
	i += 1 

# GENERATE Three of a Kinds (858):
def gen_threes():
	threes = []
	for i, card in enumerate(cards[:13]):
		three = [card, cards[i+13], cards[i+26]]
		
		for i2 in range(12):
			if cards[i2].rank == card.rank:
				continue
			else:
				three.append(cards[i2])
				
				for i3 in range(i2+1,13):
					if cards[i3].rank == card.rank:
						continue
					else:
						three.append(cards[i3])
						threes.append(three)
					
						three = three[:-1]
				three = three[:-1]
		three = []
	
	return threes

# POPULATE ec_table w/ Three of a Kinds:
i = 1610
threes = gen_threes()
for three in threes:
	key = str(i)
	ec_table[key] = three
	
	i += 1 

# Prints entire ec_table:
for k, v in ec_table.items():
	for card in v:
		print(card, end=' ')
	print()