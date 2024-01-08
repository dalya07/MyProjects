#################################Blackjack Project ########################################

import random

print("""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
""")

def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card


# Inside calculate_score() check for a black with only 2 cards: ace + 10)
# and return 0 instead of the actual score. 0 will represent a blackjack in our game.
def calculate_score(cards):
    """Take a list of cards and return the score calculate from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

# Inside calculate_score() check for an 11 (ace). If the score is already over 21,
# remove the 11 and replace it with a 1. You might need to look up append() and remove().
    if 11 in cards and sum(cards) > 21:
        #nehmen die 11 weg!!
        cards.remove(11)
        cards.append(1)
    return sum(cards)

"""To see who winn and who lose"""
def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"
    if computer_score == user_score:
        return "It's draw 🙃"
    elif computer_score == 0:
        return "You lose, the computer has a Blackjack 🙊"
    elif user_score == 0:
        return "You win, with a Blackjack 🥳"
    elif user_score > 21:
        return "You went over, you lose 😤"
    elif computer_score > 21:
        return "Computer went over, You win 😁"
    elif user_score > computer_score:
        return "You have a higher score, you win 😆"
    else:
        return "Computer have a higher score, you lose 😑"

# Deal the user and computer 2 cards each using deal_card() and append().
user_cards = []
computer_cards = []
is_game_over = False

for x in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

# Call calculate_score(). If the computer or the user has a blackjack (0) or if the
# user's score is over 21, then the game ends.
while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"    Your cards: {user_cards}, current score: {user_score}")
    print(f"    Computers first card: {computer_cards[0]}")

# If the game has not ended, ask the user if they want to draw another card.
# If yes, then use the deal_card() function to add another card to the user_cards List.
# If no, then the game has ended.
    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        user_should_deal = input("Type 'y' to get an other card or type 'n' to pass: ")
        if user_should_deal == "y":
             user_cards.append(deal_card())
        else:
            is_game_over = True

# Once the user is done, it's time to let the computer play.
# The computer should keep drawing cards as long as it has a score less than 17.
while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    #Um jedesmal zu gucken ob der computer einen Blackjack hat! sowas wie computer_score aktualesieren
    computer_score = calculate_score(computer_cards)

print(f"   Your final hand: {user_cards}, final score: {user_score}")
print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
print(compare(user_score, computer_score))


