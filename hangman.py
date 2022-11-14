import random

# list of words
words = ["people", "dog", "cat", "mobile", "truck", "nurse", "coffee", "treasure", "clown", "school", "elephant",
         "desk", "guardian", "holiday", "giraffe", "table", "Canada", "telephone", "galaxy", "mouse",
         "chocolate", "vanilla", "football", "baseball", "boxing", "Greece", "India", "jacket", "pinguin",
         "earth", "rainbow"]

# choose a random word from the list
random_word = random.choice(words).lower()


# function of the hangman game
def hangman(word: str):
    """
    The known game hangman. Choose a letter. If it's in the word, it appears in its spot. If it's not, you lose a life!
    :param word: a random word from out words list
    """
    print("Welcome to hangman!")
    print("Find the hidden word!")
    answer = "_" * len(word)
    ans = []
    for a in answer:
        ans.append(a)
    print(ans)
    guessed_words = []  # Create a list with guessed words
    x = 0

    while True:
        letter = input("Choose a letter: ")
        if letter in guessed_words:
            print("You've already guessed that letter! Try an other one!")
            continue
        if letter == "":
            print("You must type a letter!")
            continue
        guessed_words.append(letter)  # add your letters into the list, so you don't repeat any same letters
        # you've already guessed
        if letter in word:
            # find the index of the letter with enumerate to replace multiple same letters in the word
            for i, c in enumerate(word):
                if c == letter:
                    ans[i] = letter
            print("You found a letter!")
            print(ans)
            if "_" not in ans:
                print(f"You won the game! You've guessed the word {word.upper()}! ")
                break
            else:
                continue
        else:
            print(f"Nope! You've guessed wrong! You have {7 - x} more tries!")
            x += 1
            if x == 8:
                print(f"You lost the game! The word was {word.upper()}")
                break


if __name__ == "__main__":
    hangman(random_word)
