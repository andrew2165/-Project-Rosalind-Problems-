#! python3
# Consensus and Profile - Computing the Consensus string given a list of
# DNA strings in FASTA format

import re
import pyperclip

print('Where is the data?')
data_file = open(input())
good_data = data_file.read().replace('\n', '')  #
find_value = re.compile(r'[ACTG]{1,1000}')
a = find_value.findall(good_data)

l = []  # l is used as storage for the DNA strings
c = []  # c is used as storage for the Consensus sequence
pre_par = []  # Variable for storing pre-parsed DNA
par = iter(pre_par)  # Turned into an iterable to create the final consensus_seq
a_tot = []  # Total 'A's
c_tot = []  # Total 'C's
t_tot = []
g_tot = []

for i in range(len(a)):  # Filling l
    l.append(a[i])

for i in range(len(l[0])):  # Primary Loop
    A, C, T, G = 0, 0, 0, 0
    for p in range(len(l)):
        if l[p][i] == 'A':
            A += 1
        if l[p][i] == 'C':
            C += 1
        if l[p][i] == 'T':
            T += 1
        if l[p][i] == 'G':
            G += 1
    if A > C and A > T and A > G:
        c.append('A')
    if C > A and C > T and C > G:
        c.append('C')
    if T > A and T > C and T > G:
        c.append('T')
    if G > A and G > C and G > T:
        c.append('G')
    pre_par.append(A)
    pre_par.append(C)
    pre_par.append(T)
    pre_par.append(G)

consensus_seq = ''.join(c)  # Turning the list of Consensus into string

len = len(l[0])

for i in range(int(len)):  # Loop prepping for the final array
    a_tot.append(str(next(par)))
    c_tot.append(str(next(par)))
    t_tot.append(str(next(par)))
    g_tot.append(str(next(par)))

a_fin = ' '.join(a_tot)  # Formatting
c_fin = ' '.join(c_tot)
t_fin = ' '.join(t_tot)
g_fin = ' '.join(g_tot)


# The rest deals with outputting the data
final = str(consensus_seq+'\n'+'A: '+a_fin+'\n'+'C: '+c_fin+'\n'+'G: '+g_fin+'\n'
+'T: '+t_fin)
print(final)
pyperclip.copy(final)
print('Output Copied to Clipboard')
