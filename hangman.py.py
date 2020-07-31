import random

def main():
    welcome = ["lets play hangman:"]


     play_again = True

     while play_again:

         words = ["pineapple","strawberry","coconut","avacado","banana","apple",
         "computer"]

         chosen_word = random.choice(words).lower()

         player_guess = None
         guessed_letters = []
         word_guessed = []


         for letter in chosen_word:
             word_guessed.append("_")

             joined_word = None


HANGMAN = (
"""

-----
|   |
|
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|  /
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|  /=
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|  /=/
|   |
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|  /=/
|   |
|   |
|
|
|
--------
""",
"""
-----
|   |
|   0
|  /=/
|   |
|   |
|  |
|
|
--------
""",
"""
-----
|   |
|   0
|  /=/
|   |
|   |
|  |
|  |
|
--------
""",
"""
-----
|   |
|   0
|  /=/
|   |
|   |
|  | |
|  |
|
--------
""",
"""
-----
|   |
|   0
|  /=/
|   |
|   |
|  | |
|  | |
|
--------
""",
"""
-----
|   |
|   0
|  /=/
|   |
|   |
|  | |
|  | |
|
--------
""")




print(HANGMAN[0])
attempts = len(HANGMAN) - 1


    while attempts != 0 and "_" in word_guessed:
        print("\n You have {} attempts remaining").format(attempts)
            joined_word = "".join(word_guessed)
            print(joined_word)
            player_guess = str(input("\nPlease select a letter between A-Z" + "\n> ")).lower()
            if not player_guess.isalpha():
                print("That is not a letter. Please try again")
            elif len(player_guess) > 1:
                print("that is more than one letter. Please try again")
            elif player_guess in guessed_letters:
                print("you have already guessed that letter. Please try again")
            else:
                pass

                guessed_letters.append(player_guess)

                for letter in range(len(chosen_word)):
                    if player_guess == chosen_word(letter):
                        player_guess = word_guessed(letter)

                        for player_guess in chosen_word:
                            attempts -= -1
                            print([HANGMAN(len(HANGMAN) -1) - attempts])

                            if "_" not in word_guessed:
                                print("\nCongratulations {} was the word").format(chosen_word)
                            else:
                                print("\nUnlucky! The word was {}.").format(chosen_word)

                                print("would you like to play again?")

                                response = input("> ").lower()

                                if response not in ("yes", "y"):
                                    play_again = False

                                    if response == "quit":
                                        player_guess = False
if __name__ == '__main__':
    main()
