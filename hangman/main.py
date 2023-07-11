#Step 1 
import random

#imported words from words module 
#made a random choise on wordlist from words module
#
from words import word_list
chosen_word = random.choice(word_list)

#imported the logo from art module
from art import logo
print(logo)
#print(f'Pssst, the solution is {chosen_word}.')

#created a list were "_" are being created according letters in chosen word
display = []
word_length = len(chosen_word)
for letter in chosen_word:
    display.append("_")

#created amount of lives and a loop to play until win or loose
lives = 6
end_of_game = False    

#loop to keep playing until finding word or losing 6 lives
while not end_of_game:
    print(display)
    print(f"You have {lives} lives.")

    guess = input("Choose a letter:  ").lower()

#changing the "_" into a letter if correct answer
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
        
 # - 1 live if answer not correct       
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"The secret word was {chosen_word}")
            
        

    
    if "_" not in display:
        end_of_game = True
        print(display)
        print(f"The secret word is {chosen_word}")
        print("You won!")

#adjutes to show the art according lives
    from art import stages
    print(stages[lives])


