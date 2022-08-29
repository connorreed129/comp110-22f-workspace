"""EX01 - Chardle - A Cute Step toward Wordle."""
__author__ = "730478163"

word_guess: str = input("Enter a five character word: ")
character_guess: str = input("Enter a single character: ")
print("Searching for " + character_guess + " in " + word_guess)

if character_guess == word_guess[0]:
    print(character_guess + " found at index 0 ")
if character_guess == word_guess[1]:
    print(character_guess + " found at index 1 " )
if character_guess == word_guess[2]:
    print(character_guess + " found at index 2 ")
if character_guess == word_guess[3]:
    print(character_guess + " found at index 3 ")
if character_guess == word_guess[4]:
    print(character_guess + " found at index 4 ")

instances_counter: int = 0

if character_guess == word_guess[0]:
    instances_counter: int = instances_counter + 1
if character_guess == word_guess[1]:
    instances_counter: int = instances_counter + 1
if character_guess == word_guess[2]:
    instances_counter: int = instances_counter + 1
if character_guess == word_guess[3]:
    instances_counter: int = instances_counter + 1
if character_guess == word_guess[4]:
    instances_counter: int = instances_counter + 1

if instances_counter > 1:
    print(str(instances_counter) + " instances of " + str(character_guess) + " found in " + str(word_guess))
if instances_counter == 1:
    print(str(instances_counter) + " instance of " + str(character_guess) + " found in " + str(word_guess))
if instances_counter < 1:
    print("No instances of " + str(character_guess) + " found in " + str(word_guess))
if len(word_guess) != 5:
    print("Error word must contain 5 letters. ")
    exit() 
if len(character_guess) != 1:
    print("Error: Character must be a single character. ")
    exit()