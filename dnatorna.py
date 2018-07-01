#! python3
# DNA to RNA

print('What is the DNA string?')
t = input()

u = []

trans = {'A':'A','C':'C','T':'U','G':'G'}
# use ''.join(u) to make a str
for i in range(len(t)):
    if t[i] == 'A':
        u.append(trans['A'])
    if t[i] == 'C':
        u.append(trans['C'])
    if t[i] == 'T':
        u.append(trans['T'])
    elif t[i] == 'G':
        u.append(trans['G'])

output = ''.join(u)

print(output)

# best answer
# s = raw_input() <- from python 2
# print(s.replace('T', 'U'))
