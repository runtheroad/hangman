import random


def start_new_game(prompt):
    while True:
        user_choice = input(prompt).upper()
        if user_choice in "NQ":
            return user_choice
        else:
            pass


def get_word_and_hint():
    with open("hangman_words.txt", "r") as file:
        lines = file.readlines()
        random_line = random.choice(lines).strip()
        word, hint = random_line.split("-")
        word = word.strip().upper()
        hint = hint.strip()
    return word, hint


def prompt_user_letter():
    user_guess = input("Enter a letter: ").upper()
    return user_guess


def validate_user_letter():
    while True:
        user_letter = prompt_user_letter()
        if ("A" <= user_letter <= "Z") and len(user_letter) == 1:
            return user_letter
        else:
            pass


def validate_repeat_entry(letters_entered):
    while True:
        user_letter = validate_user_letter()
        if user_letter not in letters_entered:
            letters_entered.add(user_letter)
            return user_letter
        else:
            print(f"You have previously entered letter {user_letter}")
            pass


def start_game():
    letter_entered = set()
    errors = 0
    game_word, game_hint = get_word_and_hint()
    print("Welcome to the game of HANGMAN, anon!")
    print(f"\033[93mLet me give you a hint: {game_hint}\033[0m")
    masked_word = ["_"] * len(game_word)

    while errors <= 6:
        show_word = "".join(c for c in masked_word)
        if game_word == show_word:
            print("Congrats, anon!")
            print(f"Word: {game_word}")
            break
        else:
            print(f"Word: {show_word}")
            print(f"Errors: {errors}")
            user_guess = validate_repeat_entry(letter_entered)
            if user_guess not in game_word:
                print("Wrong!")
                errors += 1
            else:
                for index, char in enumerate(game_word):
                    if char == user_guess:
                        masked_word[index] = char
    else:
        print("You are dead")
        print(f"The word was {game_word}")


def main():
    while True:
        action = start_new_game("Start (N)ew Game or (Q)uit? ")
        if action != "Q":
            start_game()
        else:
            break


if __name__ == "__main__":
    main()
