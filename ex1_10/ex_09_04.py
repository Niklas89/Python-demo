# 9.4 Write a program to read through the mbox-short.txt and figure out who has
# sent the greatest number of mail messages. The program looks for 'From ' lines
#  and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address
#  to a count of the number of times they appear in the file. After the
#  dictionary is produced, the program reads through the dictionary using a
#  maximum loop to find the most prolific committer.

# Desired output: cwen@iupui.edu 5

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()
all_words = list()

for line in handle:
    line = line.rstrip()
    if not line.startswith("From") : continue
    if line.startswith("From:") : continue
    wds = line.split()
    all_words.append(wds[1])

for word in all_words:
     # 0 is the default value if key doesn't exist
     # idiom : retrieve/create/update counter
    counts[word] = counts.get(word, 0) + 1


# Now we want to find the most common word
bigcount = None
bigword = None
for word,count in counts.items() :
    if bigcount is None or count > bigcount:
        bigword = word # capture and remember the key that was largest
        bigcount = count


print(bigword, bigcount)
