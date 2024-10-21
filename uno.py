# Sebastian soto
# im am going to implement "saying uno" to the code 



import random

def start_game():
    # the setup of uno
    colours = ("red", "yellow", "green", "blue")
    ranks = tuple(range(0, 11)) 

    deck = [(colour, rank) for colour in colours for rank in ranks]

    # shuffle the deck

    random.shuffle(deck)

    p1 = deck[:7]
    p2 = deck[7:14]
    deck = deck[14:]
    
    # each player has 7 cards
    
    p1 = [deck.pop(0) for _ in range(7)]
    p2 = [deck.pop(0) for _ in range(7)]

    # central card

    central_card = deck.pop(0)    
    
    whose_turn = p1

    # we choose how this information is encoded
    # we decide 0 = player 1, 1 = player 2 

    main_loop(p1, p2, deck, central_card, 0)

def main_loop(p1, p2, deck, central_card, whose_turn):

    while p1 and p2:
        p1_uno_protection = 0
        p2_uno_protection = 0

        print(f"\nplayer {whose_turn + 1}'s turn, here is your hand: {p1} ")
        print(f"\ncentral card is: {central_card}")

        # give the user a choice
        if len(p1) > 1 or len(p2) > 1:
            ans = int(input("you have a choice. you can (0) draw or (1) play: "))
            print(f"User input: {ans}")

        elif len(p1) == 1 or len(p2) == 1:
            ans = int(input("you have a choice. you can (0) draw, (1) play, (3) call uno or (4) call out player: "))
        print(f"User input: {ans}")
        
        if ans == 0:
            drawn_card = deck.pop(0)
            p1.append(drawn_card)
            if whose_turn == 0:
                p1_uno_protection == False
            if whose_turn == 1:
                p2_uno_protection == False 
            print(f"you drew a card: {drawn_card}")
        elif ans == 1:
            # ask the user for a card to play
            player_choice = int(input("which card to play? ")) - 1

            if player_choice < 0 or player_choice >= len(p1):
                print("invalid card choice!")
                continue

            valid = valid_play(central_card, p1[player_choice])
            if valid:
                central_card = p1.pop(player_choice)
                print(f"you played: {central_card}")
            else:
                print("you can't put that card!")

        elif ans == 3:
            if whose_turn == 0:
                p1_uno_protection += 1
                print("\n player 1 has called uno!")
            elif whose_turn == 1:
                p2_uno_protection += 1
                print("\n player 2 has called uno!")

        elif ans == 4:
            if whose_turn == 0 and p2_uno_protection != 1:
                print("player 1 called out player 2 for forgetting to say uno! he must now pick three cards!")
                for _ in range(3):
                    p2_call_out_cards = deck.pop(0)
                    p2.append(p2_call_out_cards)
            elif whose_turn == 1 and p1_uno_protection != 1:
                print("player 2 called out player 1 for forgetting to say uno! he must now pick three cards!")
                for _ in range(3):
                    p1_call_out_cards = deck.pop(0)
                    p1.append(p1_call_out_cards)
            else:
                print("the player has said uno! you can't call him out!")

        # switch players
        p1, p2 = p2, p1
        whose_turn = (whose_turn + 1) % 2

        if len(p1) == 0:
            print("player 1 has won!")
            break
        elif len(p2) == 0:
            print("player 2 has won!")
            break

    
    # chances are, at the end of the ai_turn, they will have modified the central_card
    # thsi function should return the new central_card
    # Is there a playable card in the ai_hand
    # loop over all the cards in the ai_hand
    # if we find a valid card (using valid_card)
        # replace player 1 hand with player 2

            # the code that deals with drawing 

def valid_play(card1, card2):
    # return true if the number or the colour of the cards in the game
    return card1[0] == card2[0] or card1[1] == card2[1]

start_game()
