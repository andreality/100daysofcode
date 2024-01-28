from random import randint

logo = '''
  _______  __    __   _______     _______.     _______.___________. __    __       ___      .______     ____    ____ 
 /  _____||  |  |  | |   ____|   /       |    /       |           ||  |  |  |     /   \     |   _  \    \   \  /   / 
|  |  __  |  |  |  | |  |__     |   (----`   |   (----`---|  |----`|  |  |  |    /  ^  \    |  |_)  |    \   \/   /  
|  | |_ | |  |  |  | |   __|     \   \        \   \       |  |     |  |  |  |   /  /_\  \   |      /      \_    _/   
|  |__| | |  `--'  | |  |____.----)   |   .----)   |      |  |     |  `--'  |  /  _____  \  |  |\  \----.   |  |     
 \______|  \______/  |_______|_______/    |_______/       |__|      \______/  /__/     \__\ | _| `._____|   |__|     
'''

EASY_TURNS = 10
HARD_TURNS = 5
# Number Guessing Game Objectives:

# Include an ASCII art logo.
print(logo)
print("Welcome to Guesstuary!")
target = randint(1, 100)
# Allow the player to submit a guess for a number between 1 and 100.

# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.

def get_number_of_turns():
    difficulty_level = input("Select easy (E) or hard (H) mode.").lower()
    if difficulty_level == "e":
        return EASY_TURNS
    else:
        return HARD_TURNS

def run_turn(num_turns, max_turns):
    if num_turns == max_turns:
        print("You are out of turns!")
        return
    num_turns_remaining = max_turns - num_turns - 1
    guess = input("Select a number between 1 and 100")
    guess = int(guess)
    if guess == target:
        print(f"Correct! The number was {target}.")
    elif guess > target:
        print(f"Too high! You have {num_turns_remaining} turns left.")
    else:
        print(f"Too low! You have {num_turns_remaining} turns left.")
    if guess != target:
        num_turns += 1
        run_turn(num_turns, max_turns)

starting_turns = get_number_of_turns()
run_turn(num_turns=0, max_turns=starting_turns)