from prettytable import PrettyTable

table = PrettyTable()
table.add_column(fieldname="day", column=["2024-01-29", "2024-02-01"])
table.add_column(fieldname="amount", column=[120, 16])

print(table)
print(table.align)

table.align = "l"
print(table)