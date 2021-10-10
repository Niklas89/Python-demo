# 6.5 Write code using find() and string slicing (see section 6.10) to extract
# the number at the end of the line below. Convert the extracted value to a
# floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475";
#index = 0
#while index < len(text):
#    letter = text[index]
#    print(index, letter)
#    index = index + 1
#print(text[23:29])

# ONE WAY TO SOLVE IT:
pos = text.find('0')
host = text[pos:]
newhost = float(host)
print(host)

# ANOTHER WAY TO SOLVE IT:
ipos = text.find(':')
ihost = text[ipos+1:]
piece = ihost.lstrip()
newpiece = float(piece)
print(newpiece)

#s = 'Monty Python'
#print(s[8:])

#data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
#pos = data.find('.')
#print(data[pos:pos+3])
