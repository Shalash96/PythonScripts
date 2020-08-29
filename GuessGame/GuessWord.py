import random
from GameAssist import word_list, stages

print("""
██     ██ ███████ ██       ██████  ██████  ███    ███ ███████     ████████  ██████      ██   ██  █████  ███    ██  ██████  ███    ███  █████  ███    ██ 
██     ██ ██      ██      ██      ██    ██ ████  ████ ██             ██    ██    ██     ██   ██ ██   ██ ████   ██ ██       ████  ████ ██   ██ ████   ██ 
██  █  ██ █████   ██      ██      ██    ██ ██ ████ ██ █████          ██    ██    ██     ███████ ███████ ██ ██  ██ ██   ███ ██ ████ ██ ███████ ██ ██  ██ 
██ ███ ██ ██      ██      ██      ██    ██ ██  ██  ██ ██             ██    ██    ██     ██   ██ ██   ██ ██  ██ ██ ██    ██ ██  ██  ██ ██   ██ ██  ██ ██ 
 ███ ███  ███████ ███████  ██████  ██████  ██      ██ ███████        ██     ██████      ██   ██ ██   ██ ██   ████  ██████  ██      ██ ██   ██ ██   ████ 
                                                                                                                                                        
                                                                                                                             created by MAHMOUD SHALASH

""")

name = input("What is your name: ")
total = 0
wins = 0
loss = 0


def game():
    global total, wins, loss
    total += 1
    word_to_guess = random.choice(word_list).upper()
    guessed_letters = []
    guessed_words = []
    guessed = False
    word_completion = '_' * len(word_to_guess)
    number_of_tries = 6
    print(f'{name} you have {number_of_tries} tries to guess the correct word'
          f'\nThe word consists of {len(word_to_guess)} characters\n')
    print(stages[number_of_tries])
    print('\t\t\t\t' + word_completion)
    while number_of_tries > 0 and not guessed:
        guess = input('\nguess a character or a word: ').upper()
        if guess == 'hint'.upper():
            if number_of_tries > 2:
                rand_pos = random.randint(0, len(word_to_guess))
                print("HINT ---------> " + word_to_guess[rand_pos])
                number_of_tries -= 2
            else:
                print('YOU CANT USE HINT BECAUSE YOUR TRIES IS LESS OR EQUAL TO 2')

        elif len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f'you guessed ( {guess} ) before')
            elif guess not in word_to_guess:
                number_of_tries -= 1
                print(f'{guess} not in the word')
                guessed_letters.append(guess)
            else:
                print(f'Good job!, {guess} is in the word')
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                letter_position = [place for place, letter in enumerate(word_to_guess) if letter == guess]
                for place in letter_position:
                    word_as_list[place] = guess
                word_completion = ''.join(word_as_list)
                if '_' not in word_completion:
                    guessed = True

        elif len(guess) > 1 and guess.isalpha():
            if guess in guessed_words:
                print('You guessed this word before')
            elif guess == word_to_guess:
                guessed = True
                word_completion = word_to_guess
            elif guess != word_to_guess:
                print(f'{guess} is not the correct word')
                number_of_tries -= 1
                guessed_words.append(guess)

        else:
            print('\tENTER ONLY LETTERS')

        print(f'\t\t\t\tYou have {number_of_tries} tries left')
        print(stages[number_of_tries])
        print('\t\t\t\t\t' + word_completion)
        print('NOTE YOU CAN USE HINT TO SHOW YOU A LETTER IN THE WORD BUT THIS COST YOU TWO TRIES')

    if guessed:
        print("Congratulation you guessed the word")
        wins += 1

    else:
        print(f'Sorry you failed to guess the word. The word is {word_to_guess}. Try again the next time')
        loss += 1


game()
while input("Do you want to play another game (Y/N)? ").upper() == 'Y':
    game()

print(f"You played {total} games in total"
      f"\nYou won {wins}"
      f"\nYou lost {loss}")
