import random
import time
import sqlite3
from datetime import datetime
from beepy import beep
from progressbar import progressbar
from pixela import add_pixel
import webbrowser

target = int(input("Enter target number of reps."))
min_reps_per_set = 8  # int(input("Enter min reps per set."))
max_reps_per_set = 16  # int(input("Enter max reps per set."))
rest = 60

# TODO: weight reps more heavily on front end

pushups_list = []

while sum(pushups_list) < target:
    remaining = target - sum(pushups_list)
    reps = random.randint(min_reps_per_set, max_reps_per_set)
    reps = min(reps, remaining)
    reps_done = int(input(f"Target reps for this set is {reps}. How many did you do?"))
    pushups_list.append(reps_done)
    print(f"Total remaining: {target - sum(pushups_list)}")
    for i in progressbar(range(rest)):
        time.sleep(rest / 60)
    random_sound_int = random.randint(1, 7)
    beep(random_sound_int)

print(pushups_list)
date = datetime.now().strftime("%Y%m%d")
success = False
while success is False:
    response = add_pixel(date, reps=sum(pushups_list))
    print(response)
    if response.status_code == 200:
        success = True

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

webbrowser.open("https://pixe.la/v1/users/andreality/graphs/pushups.html")
