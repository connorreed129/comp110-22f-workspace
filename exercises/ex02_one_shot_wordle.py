"""One Shot Wordle"""

__author__: "730478163"
SECRET: str = "python"
secret_letter_counter: int = len(SECRET)

user_guess: str = input(f"What is your {int(secret_letter_counter)}-letter guess? ")

while len(user_guess) != secret_letter_counter:
    user_guess: str = input(f"That was not {int(secret_letter_counter)} letters! Try again: ")


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
character_existence: bool = False 
alternate_index_tracker: int = 0


index_tracker: int = 0
while index_tracker < len(SECRET):
    if user_guess[index_tracker] == SECRET[index_tracker]:
        print(GREEN_BOX, end = '')
    else: 
        character_existence = False
        alternate_index_tracker = 0
        while character_existence == False and alternate_index_tracker < len(SECRET):
            if user_guess[index_tracker] == SECRET[alternate_index_tracker]:
                character_existence = True
            else:
                alternate_index_tracker += 1 
        if character_existence == True:
            print(YELLOW_BOX, end = '')
        else:
            print(WHITE_BOX, end = '')
    index_tracker += 1

if user_guess == SECRET:
    print("\nWoo! You got it! ")
else:
    print("\nNot quite. Play again soon! ")
