from Question_2_Classes import Deck


def main():
    print("Card Dealer \n")
    print("I have shuffled a deck of 52 cards.\n")
    hand = []
    num = int(input("How many cards would you like?: "))
    if num < 0:
        print("Invalid Number. Try Again.")
    else:
        for i in range(num):
            cards = Deck.deal_card
            hand.append(cards)
        print("\nHere are your cards:")
        print(hand)

        left = 52 - num
        print(f"\nThere are {left} cards left in the deck.\n")
        print("Good Luck!")


if __name__ == "__main__":
    main()
