import random
import time
import sqlite3
from datetime import datetime
from beepy import beep
from progressbar import progressbar

target = int(input("Enter target number of reps."))
min_reps_per_set = 5  # int(input("Enter min reps per set."))
max_reps_per_set = 15  # int(input("Enter max reps per set."))
rest = 60

pushups_list = []

while sum(pushups_list) < target:
    remaining = target - sum(pushups_list)
    reps = random.randint(min_reps_per_set, max_reps_per_set)
    reps = min(reps, remaining)
    reps_done = int(input(f"Target reps for this set is {reps}. How many did you do?"))
    print(f"Total so far: {sum(pushups_list)}")
    pushups_list.append(reps_done)
    for i in progressbar(range(rest)):
        time.sleep(rest / 60)
    random_sound_int = random.randint(1, 7)
    beep(random_sound_int)


print(pushups_list)

db = sqlite3.connect("pushups.db")
cursor = db.cursor()
max_id = cursor.execute("SELECT MAX(id) from pushups").fetchone()[0]
db_id = max_id + 1
date = datetime.now().strftime("%Y-%m-%d")
for i in range(0, len(pushups_list)):
    cursor.execute(f"INSERT INTO pushups VALUES ({db_id}, '{date}', {i + 1}, {pushups_list[i]})")
    db_id += 1
db.commit()
cursor.close()

