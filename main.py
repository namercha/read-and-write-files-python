#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Names/invited_names.txt") as names:
    list_of_names = names.readlines()
    # print(list_of_names)

with open("Input/Letters/starting_letter.txt") as template:
    template_text = template.readlines()
    # print(template_text)

for name in list_of_names:
    name = name.strip("\n")
    if "[name]" in template_text[0]:
        template_text[0] = template_text[0].replace("[name]", name)
    else:
        template_text[0] = "Dear " + name + ",\n"

    file_name = "Output/ReadyToSend/letter_for_{}.txt".format(name)
    with open(file_name, mode="w") as writer:
        for line in template_text:
            writer.write(line)
