import os

#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

names_file = os.path.join("Input", "Names", "invited_names.txt")
with open(names_file) as file:
    names = file.readlines()

print(names)

template_file = os.path.join("Input", "Letters", "starting_letter.txt")
with open(template_file) as letter:
    text = letter.readlines()

for name in names:
    name = name.strip()
    new_file_name = f"to_{name}.txt"
    new_file_path = os.path.join("Output", "ReadyToSend", new_file_name)
    with open(new_file_path, "w") as new_file:
        for item in text:
            item = item.replace("[name],", f"{name},")
            new_file.writelines(item)
            new_file.writelines("\n")
