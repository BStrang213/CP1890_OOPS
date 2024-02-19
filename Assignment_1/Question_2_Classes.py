# Import Random module to get Shuffle Module
from random import shuffle


# Create a class for Card with attributes suit and value to make the cards
class Card:
    suit: list
    value: list

    # initialize two lists to store the suits and the values to use to make the cards
    def __init__(self):
        self.suit = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
        self.value = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']

    # use set all values in value to v and all values in suit to s and use (v, s) to join the two to make the card and
    # return it
    @property
    def get_card(self):
        cards = [(v, s) for v in self.value for s in self.suit]
        return cards


# create a class for deck and create an attribute for deck_cards as list
class Deck:
    deck_cards: list

    # Get the Card class for use in the Deck class and use get_card to make the deck_cards list and set a
    # shuffle_deck module
    def __init__(self):
        card = Card()
        self.deck_cards = card.get_card
        self.shuffle_deck()

    # create a module to count all the cards on the list using the len function
    def count_cards(self):
        return len(self.deck_cards)

    # set a module to shuffle the deck using random shuffle
    def shuffle_deck(self):
        shuffle(self.deck_cards)

    # set a module to deal the cards to the user by popping the card out of the list to be used elsewhere
    def deal_card(self):
        return self.deck_cards.pop()
