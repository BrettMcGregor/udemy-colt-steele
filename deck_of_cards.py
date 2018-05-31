# OOP Exercise
#
# Introduction
#
# Your goal in this exercise is to implement two classes, Card  and Deck .
#
# Specifications
#
# Card
#
# Each instance of Card  should have a suit ("Hearts", "Diamonds", "Clubs", or "Spades").
# Each instance of Card  should have a value ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K").
# Card 's __repr__  method should return the card's value and suit (e.g. "A of Clubs", "J of Diamonds", etc.)
#
# ["Hearts", "Diamonds", "Clubs", "Spades"]
# ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

# Deck
#
# Each instance of Deck  should have a cards attribute with all 52 possible instances of Card .
#
# Deck  should have an instance method called count  which returns a count of how many cards remain in the deck.
#
# Deck 's __repr__  method should return information on how many cards are in the deck (e.g. "Deck of 52 cards",
#  "Deck of 12 cards", etc.)
#
#

# Deck  should have an instance method called _deal  which accepts a number and removes at most that many cards
# from the deck (it may need to remove fewer if you request more cards than are currently in the deck!). If there
#  are no cards left, this method should return a ValueError  with the message "All cards have been dealt".
#

# Deck  should have an instance method called shuffle  which will shuffle a full deck of cards. If there are
# cards missing from the deck, this method should return a ValueError  with the message "Only full decks can
# be shuffled".  shuffle should return the shuffled deck.
#
# Deck  should have an instance method called deal_card  which uses the _deal  method to deal a single card
# from the deck and return that single card.
#
# Deck  should have an instance method called deal_hand  which accepts a number and uses the _deal  method
# to deal a list of cards from the deck and return that list of cards.


from random import shuffle  # this import really should be at the top of the file


class Deck:
    def __init__(self):
        suit = ["Hearts", "Diamonds", "Clubs", "Spades"]
        value = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(s, v) for s in suit for v in value]

    def __repr__(self):
        return f"Deck of {self.count()} cards."

    def __iter__(self):  # implemented to allow iteration through the instance(deck of cards)
        return iter(self.cards)

    def count(self):
        return len(self.cards)

    def _deal(self, num_cards):
        if self.count() == 0:
            raise ValueError("All cards have been dealt")
        if self.count() < num_cards:
            cards = self.cards[-self.count():]
            self.cards = self.cards[:-self.count()]
        else:
            cards = self.cards[-num_cards:]
            self.cards = self.cards[:-num_cards]
        return cards

    def deal_card(self):
        return self._deal(1)[0] # return the zeroth element from the list

    def deal_hand(self, hand_size):
        return self.deal(hand_size) # returns all cards in a list

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)
        return self


d = Deck()
# print(d.cards)

# d._deal(52)
# print(d)
# d._deal(1)
# print(d)
d.shuffle()

for card in d:
    print(card)
