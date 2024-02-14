import sqlite3


db = sqlite3.connect("pushups.db")
cursor = db.cursor()
data = cursor.execute("SELECT date, sum(reps) from pushups group by date").fetchall()
print(data)
