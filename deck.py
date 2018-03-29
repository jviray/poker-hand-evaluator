class Deck():
	"""Represents standard 52-card deck of playing cards."""
	
	def __init__(self):
		"""Initialize deck object with attributes."""
		self.suits = ['H', 'D', 'C', 'S']
		self.ranks = [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
		self.cards = [Card(rank, suit) for suit in self.suits 
									   for rank in self.ranks
		]
		
	def __str__(self):
		"""Modify str method to display proper Deck object values."""
		result = '['
		for i, card in enumerate(self.cards):
			if i == 0:
				result += str(card)
			else:
				result += ', ' + str(card)
		result += ']'
		return result
		

class Card():
	"""Represents a playing card."""
	
	def __init__(self, rank, suit):
		"""Initialize playing card."""
		self.rank = rank
		self.suit = suit
	
	def __str__(self):
		"""Modify str method to displpay proper Card object values.""" 
		return '(' + str(self.rank) + ', ' + self.suit + ')'
