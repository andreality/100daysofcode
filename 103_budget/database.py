import sqlite3
import datetime

db = sqlite3.connect("budget.db")
cursor = db.cursor()

cursor.execute("""CREATE TABLE spending (
    date TEXT NOT NULL,
    amount REAL NOT NULL,
    category TEXT NOT NULL,
    vendor TEXT, 
    note TEXT
);""")

CATEGORIES = ["grocery", "gas and water", "hydro", "internet", "home", "hobbies", "entertainment"]
date = datetime.now().strftime("%Y-%m-%d")
amount = float(input("Enter amount"))
category = input("Enter category")
if category not in category:
    create_new_category = input(f"{category} does not exist, do you want to add it? Y/N").lower()
    if create_new_category == "y":
        CATEGORIES.append(category)
    else:
        category = input("Re-enter category")
vendor = input("Add vendor if applicable.")
note = input("Add any additional notes here.")

cursor.execute(f"INSERT INTO spending VALUES ('{date}'', {amount}, {category}, {vendor}, {note}")
