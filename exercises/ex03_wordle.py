"""Structured Wordle."""
__author__ = "703478163"


def contains_char(word: str, character: str) -> bool:
    """Matches indicies of letter in user guess to indices of character in secret word."""
    assert len(character) == 1
    i: int = 0
    while i < len(word):
        if word[i] == character:
            return True
        i += 1
    return False


def emojified(user_guess: str, secret: str) -> str:
    """Shows matching characters (yellow), matching characters at indicies (green), and neither (white)."""
    assert len(user_guess) == len(secret)
    i: int = 0
    emoji: str = ""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    while i < len(user_guess):
        if user_guess[i] == secret[i]:
            emoji += GREEN_BOX
        elif contains_char(secret, user_guess[i]):
            emoji += YELLOW_BOX
        else: 
            emoji += WHITE_BOX
        i += 1
    return emoji


def input_guess(expected_length: int) -> str:
    """The guess and the secret word have to be the same length."""
    user_guess: str = str(input(f"Enter a {expected_length} character word: "))
    while len(user_guess) != expected_length:
        print(f"That wasn't {expected_length} chars! ")
        user_guess = str(input("Try again: "))
    return user_guess
    

def main() -> None:
    """The entrypoint of the program and main game loop."""
    turns: int = 1
    secret_word: str = "codes"
    emoji: str = ""
    while turns <= 6:
        print(f"=== Turn {turns}/6 === ")
        user_guess = input_guess(len(secret_word))
        emoji = emojified(user_guess, secret_word)
        print(emoji)
        if user_guess == secret_word:
            print(f"You won in {turns}/6 turns! ")
            return
        else:
            turns += 1
    print("X/6 - Sorry, try again tomorrow! ")


if __name__ == "__main__":
    main()