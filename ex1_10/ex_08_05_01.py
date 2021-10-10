# BASED ON THE VIDEO CORRECTION ON COURSERA
# 8.5 Open the file mbox-short.txt and read it line by line. When you find a
# line that starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word
#in the line (i.e. the entire address of the person who sent the message).
# Then print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'.
# Also look at the last line of the sample output to see how to print the count.

# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt

fname = input("Enter file name: ")
# YOU CAN Write
# if len(fname) < 1 : fname = "mbox-short.txt"
# OR I CAN ALSO WRITE:
# if line == '' : continue
# OR YOU CAN DO AS BELOW
fh = open('mbox-short.txt')

count = 0

for line in fh:
    line = line.rstrip()
    wds = line.split()
    # below you need to put len(wds) on first position, else it won't work
    if len(wds) < 3 or wds[0] != 'From' : continue
    email = wds[1]
    print(email)
    count = count + 1


print("There were", count, "lines in the file with From as the first word")
