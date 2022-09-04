"""One Shot Wordle"""

__author__: "730478163"

SECRET: str = "python"
secret_letter_counter: len(SECRET)

user_guess: input(f"What is your {secret_letter_counter}-letter guess? ")

while len(user_guess) != secret_letter_counter:
    print(input(f"That was not {int(secret_letter_counter)} letters! Try again: "))

if user_guess == SECRET:
    print("Woo! You got it! ")
else:
    print("Not quite. Play again soon! ") 