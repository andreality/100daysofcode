import os

#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

print(os.getcwd())
template_file = os.path.join("Input", "Letters", "starting_letter.txt")
names_file = os.path.join("Input", "Names", "invited_names.txt")
with open(template_file) as file:
    text = file.readlines()
    with open(names_file) as file2:
        name = file2.readline()
        print(name)
        new_file_name = f"to_{name}.txt"
        new_file_path = os.path.join("Output", "ReadyToSend", new_file_name)
        with open(new_file_name) as new_file:
            for item in text:
                item.replace("[name]", name)
                new_file.writelines(item)

# with open("Mail Merge Project Start/Input/Names/invited_names.txt") as file:
#     name = file.readline()

    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp