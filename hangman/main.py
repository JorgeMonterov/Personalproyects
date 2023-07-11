#Step 1 
import random

end_of_game = False

#word_list = ["demonslayer", "clover", "shippuden","onepiece", "jujutsukaisen"]

from words import word_list
chosen_word = random.choice(word_list)
lives = 6

from art import logo
print(logo)
#print(f'Pssst, the solution is {chosen_word}.')

display = []
word_length = len(chosen_word)
for letter in chosen_word:
    display.append("_")

    
while not end_of_game:
    print(display)
    print(f"You have {lives} lives.")

    guess = input("Choose a letter:  ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
        
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"The secret word was {chosen_word}")
            
        

    
    if "_" not in display:
        end_of_game = True
        print(display)
        print("You won!")

    from art import stages
    print(stages[lives])


