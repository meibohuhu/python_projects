
from random import shuffle
# Each instance of Card  should have a suit ("Hearts", "Diamonds", "Clubs", or "Spades").
# Each instance of Card  should have a value ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K").
# Card 's __repr__  method should display the card's value and suit (e.g. "A of Clubs", "J of Diamonds", etc.)

class Card:
	def __init__(self, value, suit):
		self.value = value
		self.suit = suit

	def __repr__(self):
		# return "{} of {}".format(self.value, self.suit)
		return f"{self.value} of {self.suit}"
class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = []
        # for suit in suits:
        #     for value in values:
        #         self.cards.append(Card(value, suit))
        # print(self.cards)
        ## we can use this statement:
        self.cards = [[Card(value, suit) for value in values] for suit in suits]

    def count(self):
        return len(self.cards)

## for internal usage so have underscore
    def _deal(self, num):
        count = len(self.cards)
        num = min(count, num)
        if num == 0:
            raise ValueError("All cards have been dealt")
        print(f"Let's make deal for total number {num}")
        cards_result = self.cards[-num:]     ## using slicing
        self.cards = self.cards[:-num]
        return cards_result

    def shuffle(self):
        print("Let's shuffle current cards")
        return shuffle(self.cards)

    ## Only deal for one card
    def deal_card(self):
        print(f"Let's make deal for one card")
        return self._deal(1)[0]     ## only grab first one of list

    ## deal for hand number of cards
    def deal_hand(self, hand_size):
        print(f"Let's make deal for {hand_size} of cards")
        return self._deal(hand_size)

# Each instance of Deck  should have a cards attribute with all 52 possible instances of Card .
# Deck  should have an instance method called count  which returns a count of how many cards remain in the deck.
# Deck 's __repr__  method should display information on how many cards are in the deck (e.g. "Deck of 52 cards", "Deck of 12 cards", etc.)
# Deck  should have an instance method called _deal  which accepts a number and removes at most that many cards from the deck (it may need to remove fewer if you request more cards than are currently in the deck!). If there are no cards left, this method should return a ValueError  with the message "All cards have been dealt".
# Deck  should have an instance method called shuffle  which will shuffle a full deck of cards. If there are cards missing from the deck, this method should return a ValueError  with the message "Only full decks can be shuffled".
# Deck  should have an instance method called deal_card  which uses the _deal  method to deal a single card from the deck.

the_deck = Deck()
print(the_deck.cards)
the_deck.shuffle()
print(the_deck.cards)

print(the_deck.deal_card())
print(the_deck.deal_hand(4))
