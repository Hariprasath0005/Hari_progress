#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp



with open(r"C:\Users\thprasat\Hari_progress\Day15\Mail Merge Project Start\Input\Names\invited_names.txt") as names:
    name = names.readlines()
    
with open(r"C:\Users\thprasat\Hari_progress\Day15\Mail Merge Project Start\Input\Letters\starting_letter.txt") as letter:
    letters = letter.read()


for i in name:
    x = i.strip()
    y = letters.replace("[name]",x) 
    print(y)
    with open(f"./Day15/Mail Merge Project Start/Output/ReadyToSend/letter_to_{x}.txt",mode="w") as final_letter:
        final_letter.write(y)
    





