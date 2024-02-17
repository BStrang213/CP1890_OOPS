import random
from dataclasses import dataclass

class Card:
    def __init__(self, suit:list, value:list):
        self.suit = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
        self.value = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']

    # suit:list = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
    # value:list =['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']

    #suit = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
    #value =

    def get_card(self):
        card = [f"{self.value} of {self.suit}"]
        return card

    @property
    def cards(self):
        return self.card


class Deck:
    def __init__(self, Card):
        deck_cards = []
        deck_cards.append(Card)

    def count_cards(self, deck_cards):
        deck_num = deck_cards.count
        return int(deck_num)

    def shuffle_deck(self, deck_cards):
        ran_deck = random.shuffle(deck_cards)
        return ran_deck

    def deal_card(self, ran_deck):
        card = random.choice(ran_deck)
        return card
