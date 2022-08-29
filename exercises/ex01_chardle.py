"""EX01 - Chardle - A Cute Step toward Wordle."""
__author__ = "730478163"


SECRET: str = "green"

print("Welcome to Chardle! ")
word_guess: str = input("Enter a five character word. ")
if len(word_guess) != 5:
    print("Error word must contain 5 letters. ")
    exit()
character_guess: str = input("Enter a single character. ")
if len(character_guess) != 1:
    print("Error: Character must be a single character.  ")
    exit()

if word_guess == SECRET: 
    print("You have guessed correctly! You're a Chardle master! ")
    exit()  

if word_guess != SECRET:
    print("Searching for " + character_guess + " in " + word_guess)

if character_guess == SECRET[0]:
    print(character_guess + " found at index 0. ")
if character_guess == SECRET[1]:
    print(character_guess + " found at index 1. " )
if character_guess == SECRET[2]:
    print(character_guess + " found at index 2. ")
if character_guess == SECRET[3]:
    print(character_guess + " found at index 3. ")
if character_guess == SECRET[4]:
    print(character_guess + " found at index 4. ")


instances: int = 0

if character_guess == word_guess[0]:
    instances: int = instances + 1
if character_guess == word_guess[1]:
    instances: int = instances + 1
if character_guess == word_guess[2]:
    instances: int = instances + 1
if character_guess == word_guess[3]:
    instances: int = instances + 1
if character_guess == word_guess[4]:
    instances: int = instances + 1

if instances > 1:
    print(str(instances) + " instances of " + str(character_guess) + " found in " + str(word_guess))
if instances == 1:
    print(str(instances) + " instance of " + str(character_guess) + "found in " + (word_guess))
if instances < 1:
    print("No instances of " + str(character_guess) + "found in " + str(word_guess))


