import sqlite3
from pixela import add_pixel
from datetime import datetime, timedelta

db = sqlite3.connect("pushups.db")
cursor = db.cursor()
data = cursor.execute("SELECT date, sum(reps) from pushups group by date").fetchall()
print(data)

# print(pushups_list)
# date = datetime.now().strftime("%Y%m%d")

for date, reps in data:
    date = datetime.strptime(date, "%Y-%m-%d").strftime("%Y%m%d")
    print(date)
    add_pixel(date, reps)

# print(pushups_list)
# date = datetime.now().strftime("%Y%m%d")


# tracking_date = "2024-02-01"
# dash_format = "%Y-%m-%d"
# condensed_format = "%Y%m%d"
#
# for date, reps in data:
#     print(tracking_date)
#     while date != tracking_date:
#         date_dt = datetime.strptime(tracking_date, dash_format)
#         api_date = date_dt.strftime(condensed_format)
#         add_pixel(api_date, 0)
#         date_dt += timedelta(days=1)
#         tracking_date = date_dt.strftime(dash_format)
#         print(tracking_date)
#     date = datetime.strptime(date, dash_format).strftime(condensed_format)
#     add_pixel(date, reps)

