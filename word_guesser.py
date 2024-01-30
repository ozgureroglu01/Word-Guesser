import random

def main():
    print("Welcome to Word Guesser")
    print("You have 6 guesses use them wisely")
    game()
    while True:
        play_again = input("Play again ?").lower()
        if play_again == "a":
            game()
        else:
            break


def game():
    word = get_word()
    hidden_word = print_underscore_for_letters_in_word(word)
    life = 10
    while life != 0:
        guess = get_guess()
        hidden_check=check_guess(guess,word,hidden_word)
        hidden_word = hidden_check
        if guess == word:
            break
            print("Congratulations you won!!")
        print(hidden_word)
        print(hidden_check)
        if check_win(word,hidden_word):
            break
            print("Congratulations you won!!")
        life -= 1
    print("You lost :(")
    print(word)
    print("Press a to play again")
    print("Press any key to exit")
    

def get_word():
    words = []
    with open("words.txt") as file:
        for line in file:
            words.append(line.rstrip())
    return random.choice(words)


def print_underscore_for_letters_in_word(word):
    new_word = []
    for letter in word:
        new_word.append("_")
    return "".join(new_word)


def get_guess():
    return input("Guess: ")


def check_guess(guess,word,hidden_word):
    hidden_word_list = list(hidden_word)
    for index,letter in enumerate(word):
        if letter == guess:
            hidden_word_list[index] = letter
    return "".join(hidden_word_list)


def check_win(word,hidden_word):
    return word == hidden_word


if __name__ == "__main__":
    main()