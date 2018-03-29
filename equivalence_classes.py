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