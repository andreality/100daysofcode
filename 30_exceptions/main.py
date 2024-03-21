

try:
    file = open("file.txt")
    d = {"key": "value"}
    # print(d["lock"])
except FileNotFoundError:
    file = open("file.txt", "w")
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
else:  # success condition
    content = file.read()
    print(content)
finally:  # runs no matter what
    # print("Closing file...")
    # file.close()
    raise TypeError("ERROR ABORT ABORT!")
