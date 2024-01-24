# Write your code below this line 👇
from math import ceil


def paint_calc(height, width, cover):
    area = width * height
    num_cans = area / cover
    num_cans_rounded = ceil(num_cans)
    msg = f"You'll need {num_cans_rounded} cans of paint."
    print(msg)


# Write your code above this line 👆
# Define a function called paint_calc() so the code below works.

# 🚨 Don't change the code below 👇
test_h = 5
test_w = 6
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)