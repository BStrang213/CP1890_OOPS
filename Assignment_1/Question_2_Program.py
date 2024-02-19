from Question_2_Classes import Deck


def main():
    print("Card Dealer \n")
    deck = Deck()
    print("I have shuffled a deck of 52 cards.\n")

    num = int(input("\nHow many cards would you like?: "))
    if num <= 0 or num > deck.count_cards():
        print("Invalid Number. Try Again.")
    else:
        hand = []
        for i in range(num):
            cards = deck.deal_card()
            hand.append(cards)
        print("\nHere are your cards:")
        for card in hand:
            print(f"{card[0]} of {card[1]}")

        print(f"\nThere are {deck.count_cards()} cards left in the deck.\n")
        print("Good Luck!")


if __name__ == "__main__":
    main()
