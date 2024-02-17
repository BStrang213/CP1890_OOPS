from random import shuffle, choice


class Card:
    suit: list
    value: list

    def __init__(self):
        self.suit = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
        self.value = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']

    @property
    def get_card(self):
        card = zip([f"{self.value} of {self.suit}"])
        return card

    def cards(self):
        return self.get_card


class Deck:
    deck_cards: list

    def __init__(self):
        self.deck_cards = []

    def count_cards(self):
        deck_num = self.deck_cards.count(Card)
        return deck_num

    def shuffle_deck(self):
        return shuffle(self.deck_cards)

    def deal_card(self, shuffle_deck):
        return choice(shuffle_deck)
