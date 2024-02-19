# Import from the Question_2_Classes module to use in the main program. the Deck class is the only one needed because
# the Card class only needed through the Deck class
from Question_2_Classes import Deck


# set a main function.
def main():
    # set the Deck class as deck to be used in the function
    print("Card Dealer \n")
    deck = Deck()
    # use the count_cards method to call the number of cards in the deck
    print(f"I have shuffled a deck of {deck.count_cards()} cards.\n")
    # get number input from the user for how many cards they want
    num = int(input("\nHow many cards would you like?: "))
    # set an error so if the user puts in malicious inputs it will return an error
    if num <= 0 or num > deck.count_cards():
        print("Invalid Number. Try Again.")
    else:
        # set a list for the users cards
        hand = []
        # set a loop to give the amount of cards requested
        for i in range(num):
            # set a variable for the cards called to be appended in the hand list
            cards = deck.deal_card()
            hand.append(cards)
        print("\nHere are your cards:")
        # set a loop to print all the cards
        for card in hand:
            print(f"{card[0]} of {card[1]}")

        # call the count_cards method to return the cards left in the deck
        print(f"\nThere are {deck.count_cards()} cards left in the deck.\n")
        print("Good Luck!")


if __name__ == "__main__":
    main()
