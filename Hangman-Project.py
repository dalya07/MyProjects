# Step 1
print(''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    ''')

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

import random
word_list = ["monkey", "camel", "lion", "fox", "rabbit", "wolf", "fish", "dolphin", "whale", "shark",
             "bird", "crow", "tiger", "dog", "cat"]

chosen_word = random.choice(word_list)
#print(chosen_word)
display = []
#Anzahl der Buchstaben des chosen word
world_len = len(chosen_word)
# drucken einen strich mit der anzahl der Buchstaben (von 0 bis die länge des wortes)
for _ in range(world_len):
    display += "_"

# Printen die striche ohne "" und []
print(f"{' '.join(display)}")

end_of_game = False
lives = 6
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")
# wir drucken das Buchstabe, wenn es richtig ist, anstadt das strich
    for position in range(world_len):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        print(f"You guess {guess}, that's not in the word, you lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")
        else:
            print("You win!")

    # Drucken das bild mit der aktuellen anzahl von lives
    print(stages[lives])




