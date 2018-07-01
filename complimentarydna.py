# python3
# Complimentary DNA - takes in raw DNA string and provides the Compliment

print('What is the raw string of DNA?')
s = input()


comp = {'A':'T', 'C':'G', 'T':'A', 'G':'C'}
u = []

for i in range(len(s)):
    if s[i] == 'A':
        u.append(comp['A'])
    if s[i] == 'C':
        u.append(comp['C'])
    if s[i] == 'T':
        u.append(comp['T'])
    if s[i] == 'G':
        u.append(comp['G'])

output = ''.join(u)
print('\n' + output[::-1])

# best answer
# st = "AAAACCCGGT"
# st = st.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()[::-1]
# print st
