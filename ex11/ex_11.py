import re

hand = open('actual_data.txt')

numlist = list()

for line in hand:
    line = line.rstrip()
    stuff = re.findall('[0-9]+', line)
    if len(stuff) <= 0 : continue
    #print(stuff)

    for num in range(len(stuff)) :
        newnum = int(stuff[num])
        numlist.append(newnum)
        #print('This is numlist:', numlist)
    #print('This is the sum:', sum(numlist))
print('This is the totalsum:', sum(numlist))
