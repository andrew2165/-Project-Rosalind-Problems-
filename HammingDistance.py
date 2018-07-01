#! python3
# CountingPointMutations.py - a script meant to determine the Hamming Distance
# in two strings of DNA

import re

print('Where is this file?')
location = input()
data_file = open(location)
data_read = data_file.read()
find_dna = re.compile(r'[ACTG]{1,1000}')
w = find_dna.findall(data_read)

if int(len(w[0])) != int(len(w[1])):
    raise Error('The DNA strings are not equal in legnth')

s = list(w[0])
t = list(w[1])
hamm = 0

for i in range(len(s)):
    if s[i] != t[i]:
        hamm += 1

print('Hamming Distance = ' + str(hamm))

#TODO: condense into something that can run faster

# Top Answer from Project Rosalind:
# Done using the example data

#s1 = 'GAGCCTACTAACGGGAT'
#s2 = 'CATCGTAATGACGGCCT'
#print [ a!=b for (a, b) in zip(s1, s2)].count(True)
