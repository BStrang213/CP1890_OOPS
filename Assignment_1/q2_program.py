from q2_classes import Card, Deck
def main():
    print("Card Dealer\n")
    deck = Deck()
    print("I have shuffled a deck of 52 cards.")

    num = int(input("\nHow many cards would you like?: "))
    if num <= 0 or num > deck.count_cards():
        print("Invalid Number. Try Again.")
    else:
        hand = []
        for _ in range(num):
            card = deck.deal_card()
            hand.append(card)
        print("\nHere are your cards:")
        for card in hand:
            print(f"{card[0]} of {card[1]}")

        print(f"\nThere are {deck.count_cards()} cards left in the deck.")
        print("Good Luck!")

if __name__ == "__main__":
    main()


