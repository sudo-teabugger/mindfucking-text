sample = input("Input the text that you want to convert:\n").upper()
sample = sample.replace("T","7").replace("I","1").replace("S","5").replace("E","3").replace("A","4").replace("O","0")
tofile = input(f"Here is your converted text, do you want to save it to a file? (y/n):\n{sample}\n$ ")

if tofile == "y" or tofile == "Y" or tofile == "":
    with open("brainfucking_output.txt", "w") as text_file:
        text_file.write(sample)
