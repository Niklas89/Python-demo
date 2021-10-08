# 7.1 Write a program that prompts for a file name, then opens that file and
# reads through the file, and print the contents of the file in upper case.
# Use the file words.txt to produce the output below.
# You can download the sample data at http://www.py4e.com/code3/words.txt
# Desired output is the whole text in the file

# Use words.txt as the file name
fname = input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()

for cheese in fhand:
    cheeseupper = cheese.upper()
    cheesestrip = cheeseupper.rstrip()
    print(cheesestrip)
