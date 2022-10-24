"""Choose Your Own Adventure: Chapel Hill Colors."""
__author__ = "730478163"

import random 
POSSIBLE_COLORS: list = ["blue", "white", "black"]
points: int = 5
player: str = ''
RAM_EMOJI: str = "\U0001F40F"
THUMBS_UP_EMOJI: str = "\U0001F44D"
CRYING_EMOJI: str = "\U0001f622"
ENDGAME_EMOJI: str = "\U0001F62D"
CELEBRATION_EMOJI: str = "\U0001F389"


def greet() -> None:
    """Welcome message user player variable."""
    global player
    player = input("Hello user! What is your name? ")
    print(f"Hello {player}! Welcome to Carolina Color Guesser!!! ")
    print(f"Guess the  Carolina Color I am thinking of! Your options are {POSSIBLE_COLORS}. ")
    print("You start the game with 5 points, for every color you guess correctly you will gain two points, and every color you guess incorrectly you lose a point. ")
    print("Make sure to answer the question with all lowercase alphabetical characters. ")
    print("You can elect go out at any time by typing quit. If your point total hits 0 you lose, but if your point total reaches 10, you win.")
    print("Goodluck! ")


def point_changes(initial_points: int, point_change: int) -> int:
    """Increases/ Decreases points of user."""
    return (initial_points + point_change)


def display_points() -> None:
    """Function is used to display player points."""
    global points
    print(f"You have {points}! ")


def main() -> None:
    """Entrypoint of the program and main game loop."""
    color: str = ''
    user_guess: str = ''
    global points 
    greet()
    while points > 0 and points < 10:
        color = random.choice(POSSIBLE_COLORS)
        display_points()
        user_guess = ''
        while user_guess == '':
            user_guess = input(f"What Carolina Color am I thinking of {player}? ")
            if user_guess == "quit":
                display_points()
                print(f"Goodbye Tarheel! {RAM_EMOJI} ")
                quit()
            if user_guess not in POSSIBLE_COLORS:
                print("That's not a Carolina Color! ")
                user_guess = ''
        if user_guess == color:
            points = point_changes(points, +2)
            print(color)
            print(f"You guessed correctly! {THUMBS_UP_EMOJI} ")
        else:
            points = point_changes(points, -1)
            print(f"You got it wrong, the correct answer was {color}. {CRYING_EMOJI} ")
    if points <= 0:
        print(f"Better luck next time {player}! {ENDGAME_EMOJI} ")
    else: 
        print(f"Great Job! You win {player}! You're a true Tarheel! {RAM_EMOJI}{CELEBRATION_EMOJI} ")
    display_points()


if __name__ == "__main__":
    main()