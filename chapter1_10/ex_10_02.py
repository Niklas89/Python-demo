# 10.2 Write a program to read through the mbox-short.txt and figure out the
# distribution by hour of the day for each of the messages. You can pull the
# hour out from the 'From ' line by finding the time and then splitting
# the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts,
# sorted by hour as shown below.

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
    time = wds[5]
    newword = time[:2]
    all_words.append(newword)

for word in all_words:
     # 0 is the default value if key doesn't exist
     # idiom : retrieve/create/update counter
    counts[word] = counts.get(word, 0) + 1

lst = list()
for v, k in counts.items():
    newtup = (v,k)
    lst.append(newtup)


lst = sorted(lst, reverse=False)

for v,k in lst:
    print(v,k)

#print(all_words)
#print(counts)
