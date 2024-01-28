import random
import os

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


class Hand:
    def __init__(self, is_dealer: bool, card_list=None):
        if card_list is None:
            card_list = []
        self.card_list = card_list
        self.is_dealer = is_dealer

    def hit(self):
        self.card_list.append(random.choice(cards))

    def __str__(self):
        return str(self.total)

    @property
    def total(self):
        return sum(self.card_list)


class HandSet:
    def __init__(self, num_players, hand_dict=None):
        if hand_dict is None:
            hand_dict = {"dealer": Hand(is_dealer=True)}
            for i in range(0, num_players):
                hand_dict[f"player{i + 1}"] = Hand(is_dealer=False)

        self.hand_dict = hand_dict

    def deal(self, num_cards: int = 1):
        for key, hand in self.hand_dict.items():
            for i in range(0, num_cards):
                hand.hit()

    def hit(self, player_name):
        self.hand_dict[player_name].hit()

    def player_total(self, player_name="dealer"):
        return self.hand_dict[player_name].total

    def print_hand(self, player_name):
        if player_name == "dealer":
            print(self.hand_dict["dealer"].card_list[0])
        else:
            print(self.hand_dict[player_name].card_list)
        return

    def determine_outcome(self):
        dealer_total = self.player_total("dealer")
        player_total = self.player_total("player1")
        base_message = f"Dealer score is {dealer_total}; Your score is {player_total}: "

        if dealer_total > 21:
            if player_total > 21:
                extra_message = "No one wins."
            else:
                extra_message = "You win."
        else:
            if dealer_total > player_total or player_total > 21:
                extra_message = "You lose."
            elif dealer_total == player_total:
                extra_message = "You tie."
            else:
                extra_message = "You win."
        return base_message + extra_message


def play_game():
    print(logo)
    hands = HandSet(num_players=1)
    hands.deal(num_cards=2)

    # show user the hands
    # ask user whether to hit or stay
    keep_going = True
    while keep_going:
        print("Your hand is:")
        hands.print_hand("player1")
        print("Dealer's hand is:")
        hands.print_hand("dealer")
        player_move = input("Hit (H) or Stay (S)?").lower()
        # if hit, deal card and repeat
        if player_move == "h":
            hands.hit(player_name="player1")
            # if player's hand is over 21, stop
            if hands.player_total("player1") > 21:
                keep_going = False
        else:
            keep_going = False

    # when user picks stay, move to dealer

    while hands.player_total(player_name="dealer") < 17:
        hands.hit(player_name="dealer")
    print(hands.determine_outcome())


continue_playing = "y"
while continue_playing == "y":
    os.system("clear")
    play_game()
    continue_playing = input("Would you like to play again? Y/N").lower()


##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input
#and returns the score.
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

