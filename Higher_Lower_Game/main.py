print('''
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
''')
vs = '''
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
'''


from data import Data
import random
data = Data
score = 0

"""1) From the account data into printable format"""#Wo ich stehen geblieben bin!!!
def format_data(account):
    """Takes the account data and return the printable format"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return print(f"{account_name}, a {account_descr}, from {account_country}.")

def check_answer(guess, a_follower, b_follower):
    """Take users guess and follower counts and returns if they got it right"""
    if a_follower > b_follower:
        # If Guess == to "a" than it will return True.
        # But if Guess != to "a" than it will return False
        return guess == "a"
    else:
        return guess == "b  "

account_b = random.choice(data)

"""7) Make the game repeatable"""
game_should_continue = True

while game_should_continue:
    """2) Generate a random account from the game data"""

    """8) Making account at position B become the next account at position A"""
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A:")
    print(format_data(account_a))
    print(vs)
    print(f"Against B:")
    print(format_data(account_b))

    """3) Ask user for a guess"""
    guess = input("Who has more followers? 'A' or 'B': ").lower()

    """4) Check if user is correct.
          Get follower count of each account."""
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    """5) Give user feedback on their guess"""
    """6) Score keeping"""
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        game_should_continue = False
        print(f"Sorry that's wrong. Final {score}.")



