
# Import necessary modules
import random
import time 

time.sleep(1)

# Define the ranks and suits
ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
suits = ("hearts", "diamonds", "clubs", "spades")

# Create a deck of cards

deck = [(suit, rank) for suit in suits for rank in ranks]

# Shuffle the deck 

random.shuffle(deck)

# Split the deck into two hands

deck_1 = deck[:26]

deck_2 = deck[26:]

p1_card = p1_deck.pop(0)
p2_card = p2_deck.pop(0)


def card_comparison(p1_card, p2_card):
    if ranks.index(p1_card[0]) > ranks.index(p2_card[0]): 
        print("player 1 has a stronger card") 
        return 1
    if ranks.index(p1_card[0]) < ranks.index(p2_card[0]):
        print("player 2 has a stronger card") 
        return 2
    return 0

result = card_comparison(p1_card , p2_card)
if result == 1: 
    p1_deck.append(p1_card)
    p1_deck.append(p2_card)


    """This is the logic that compares two cards to find the stronger card
		Return 1 if player 1's card is strong, 2 for player 2
		if the cards are equal, return 0.

		Hint, using the index function will make this very simple (one liner)"""
    # Your code here

def play_round(player1_hand, player2_hand):
    if :
    """Play a single round of the game.
		That is, each player flips a card, and the winner is determined using the card_comparison function
		if both players flip the same value card, call the war function
	"""
    # Your code here

def war(player1_hand, player2_hand):
    """Handle the 'war' scenario when cards are equal.
		recall the rules of war, both players put 3 cards face down, 
		then both players flip face up a 4th card. The player with the stronger
		card takes all the cards.		
	"""
    # Your code here

def play_game():
    """Main function to run the game."""
    # Your code here
def gameloop():
    while len(p1_deck) > 0 and len(p2_deck) > 0:
            
result = card_comparison(p1_card , p2_card)
if result == 1: 
    p1_deck.append(p1_card)
    p1_deck.append(p2_card)
# Call the main function to start the game
play_game()

