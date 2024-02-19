from random import shuffle


class Card:
    suit: list
    value: list

    def __init__(self):
        self.suit = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
        self.value = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']

    @property
    def get_card(self):
        cards = [(v, s) for v in self.value for s in self.suit]
        return cards


class Deck:
    deck_cards: list

    def __init__(self):
        card = Card()
        self.deck_cards = card.get_card
        self.shuffle_deck()

    def count_cards(self):
        return len(self.deck_cards)

    def shuffle_deck(self):
        shuffle(self.deck_cards)

    def deal_card(self):
        return self.deck_cards.pop()
