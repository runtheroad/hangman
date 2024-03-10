import random


def start_new_game(prompt):
    while True:
        user_choice = input(prompt).upper()
        if user_choice in "NQ":
            return user_choice
        else:
            pass


def build_word_list():
    return ['PYTHON', 'HANGMAN', 'PROGRAMMING', 'DEVELOPER', 'FUNCTION']


def prompt_user_letter():
    user_guess = input("Enter a letter: ").upper()
    return user_guess


def start_game():
    errors = 0
    word_list = build_word_list()
    game_word = random.choice(word_list)
    print("Welcome to the game of HANGMAN, anon!")
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
            user_guess = prompt_user_letter()
            if user_guess not in game_word:
                print("Wrong!")
                errors += 1
            else:
                for index, char in enumerate(game_word):
                    if char == user_guess:
                        masked_word[index] = char


def main():
    while True:
        action = start_new_game("Start (N)ew Game or (Q)uit? ")
        if action != "Q":
            start_game()
        else:
            break


if __name__ == "__main__":
    main()
