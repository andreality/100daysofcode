from data.art import logo, vs
from random import choice
from data.game_data import data

# notes from video
# 1. break problem into parts
# 2. pick easiest part
# 3. break that into concrete steps, write as comments
# 4. write code -> run code -> fix code


def generate_description_text(person_dict):
    txt = f"{person_dict['name']} is a {person_dict['description']} from {person_dict['country']}."
    print(txt)


def generate_follower_text(person_dict):
    txt = f"{person_dict['name']} has {person_dict['follower_count']} followers."
    print(txt)


def get_greater(item1, item2):
    if item1["follower_count"] > item2["follower_count"]:
        return 1
    else:
        return 2


def get_two_items(data_list, first_item=None):
    if first_item is None:
        first_item = choice(data_list)
    second_item = choice(data_list)
    while second_item == first_item:
        second_item = choice(data_list)
    return [first_item, second_item]

print(logo)

two_items = get_two_items(data)
not_wrong = True
score = 0

while not_wrong:
    generate_description_text(two_items[0])
    print(vs)
    generate_description_text(two_items[1])

    user_choice_int = int(input("Enter 1 for first option, 2 for second option."))
    user_choice_item = two_items[user_choice_int - 1]

    result = get_greater(two_items[0], two_items[1])
    if result == user_choice_int:
        score += 1
        print(f"Correct! Your score is now {score}.")
        generate_follower_text(two_items[0])
        generate_follower_text(two_items[1])
        two_items = get_two_items(data, first_item=user_choice_item)
        print("Next pair:\n")
    else:
        print(f"Wrong! Your final score is {score}.")
        not_wrong = False
        generate_follower_text(two_items[0])
        generate_follower_text(two_items[1])
