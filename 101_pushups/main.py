import random
import time
import sqlite3
from datetime import datetime
from beepy import beep
from progressbar import progressbar
from pixela import add_pixel
import webbrowser
from gtts import gTTS
from playsound import playsound

target = input("Enter target number of reps, or enter R for random.")
if target.lower() == "r":
    target = random.randint(50, 100)
    print(f"Target number of reps: {target}")
else:
    target = int(target)
min_reps_per_set = 8  # int(input("Enter min reps per set."))
max_reps_per_set = 16  # int(input("Enter max reps per set."))
rest = 60

# TODO: weight reps more heavily on front end

pushups_list = []
language = 'en'

def get_reps_input(reps):
    reps_done = input(f"Target reps for this set is {reps}. How many did you do?")
    try:
        reps_done = int(reps_done)
    except ValueError:
        reps_done = get_reps_input()
    return reps_done


while sum(pushups_list) < target:
    remaining = target - sum(pushups_list)
    reps = random.randint(min_reps_per_set, max_reps_per_set)
    reps = min(reps, remaining)
    tts = gTTS(str(reps))
    tts.save("x.mp3")
    playsound("x.mp3")
    reps_done = get_reps_input(reps)
    pushups_list.append(reps_done)
    remaining = target - sum(pushups_list)
    if remaining == 0:
        break
    print(f"Total remaining: {remaining}")
    for i in progressbar(range(rest)):
        time.sleep(rest / 60)
    # random_sound_int = random.randint(1, 7)
    # beep(random_sound_int)

print(pushups_list)
date = datetime.now().strftime("%Y%m%d")
add_pixel(date, reps=sum(pushups_list))

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
