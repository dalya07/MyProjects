print("""                                                                                                                                                                    
                                                                                                                                                                    
                          __.....__                                                        _..._              __  __   ___   /|              __.....__              
  .--./)              .-''         '.                                                    .'     '.           |  |/  `.'   `. ||          .-''         '.            
 /.''\\              /     .-''"'-.  `.                                                   .   .-.   .          |   .-.  .-.   '||         /     .-''"'-.  `. .-,.--.  
| |  | |            /     /________\   \                                __              |  '   '  |          |  |  |  |  |  |||  __    /     /________\   \|  .-. | 
 \`-' /      _    _ |                  |    _         _              .:--.'.            |  |   |  |   _    _ |  |  |  |  |  |||/'__ '. |                  || |  | | 
 /("'`      | '  / |\    .-------------'  .' |      .' |            / |   \ |           |  |   |  |  | '  / ||  |  |  |  |  ||:/`  '. '\    .-------------'| |  | | 
 \ '---.   .' | .' | \    '-.____...---. .   | /   .   | /          `" __ | |           |  |   |  | .' | .' ||  |  |  |  |  |||     | | \    '-.____...---.| |  '-  
  /'""'.\  /  | /  |  `.             .'.'.'| |// .'.'| |//           .'.''| |           |  |   |  | /  | /  ||__|  |__|  |__|||\    / '  `.             .' | |      
 ||     |||   `'.  |    `''-...... -'.'.'.-'  /.'.'.-'  /           / /   | |_          |  |   |  ||   `'.  |                |/\'..' /     `''-...... -'   | |      
 \'. __// '   .'|  '/                .'   \_.' .'   \_.'            \ \._,\ '/          |  |   |  |'   .'|  '/               '  `'-'`                      |_|      
  `'---'   `-'  `--'                                                 `--'  `"           '--'   '--' `-'  `--'                                                       """)
import random
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
answer = int(random.randint(1, 100))
print(f"Pssst, the correct answer is {answer} ")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")


# attemps -> محاولات
if difficulty == "easy":
    attemps = 10
    print(f"You have {attemps} attemps")
elif difficulty == "hard":
    attemps = 5
    print(f"You have {attemps} attemps")

end_of_game = False
while not end_of_game:
    guess = int(input("Make a guess: "))
    if attemps == 1:
        end_of_game = True
        print("You've run out of guesses, you lose.")
    elif answer > guess:
        print("Too low.")
        print("Guess again")
        attemps -= 1
        print(f"You have {attemps} attempts remaining to guess the number.")
    elif guess > answer:
        print("Too high")
        print("Guess again")
        attemps -= 1
        print(f"You have {attemps} attempts remaining to guess the number.")
    elif attemps == 0:
        end_of_game = True
        print("You lose")
    else:
        print(f"You got it! The answer was {answer}")
        end_of_game = True



















