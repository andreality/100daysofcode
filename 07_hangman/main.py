import random
from resources.images import stages, logo
from resources.words import word_list

print(logo)
chosen_word = random.choice(word_list)
display = ["_"] * len(chosen_word)

display_str = " ".join(display)
print(display_str)

stage_idx = len(stages) - 1

while "_" in display:

    print(stages[stage_idx])
    if stage_idx == 0:
        print(f"You lost! The word was {chosen_word}.")
        break
    guess = input("Select a new letter.").lower()
    if guess in display:
        print(f"You already guessed {guess.upper()}.")

    for idx, letter in enumerate(chosen_word):
        if letter == guess:
            display[idx] = letter.upper()
        else:
            continue

    if guess not in chosen_word:
        stage_idx -= 1
        print(f"The letter {guess.upper()} is not in the word.")

    display_str = " ".join(display)
    print(display_str)
    if "_" not in display:
        print("You won!")
