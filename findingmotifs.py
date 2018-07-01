#! python3
# Finding a Motif in DNA - Combs through a string of DNA looking for a given
# motif and provides the locations of the motifs in the Dictionary

import re

print('Where is the DNA string?')
file = open(input(), 'r')
dna_string = file.read()

sub = re.compile(r'[ACTG]{1,1000}')
sub_string = sub.findall(dna_string)
dna_sub = sub_string[0]
motif_sub = sub_string[1]

motif = re.finditer(r'(?=(' + motif_sub + r'))', dna_sub)
results = [str(match.start(1) + 1) for match in motif]
# I have nfc how the two lines above work, some StackOverflow magical trickery

answer = ' '.join(results)
print('motif: ' + motif_sub)
print('string: ' + dna_sub)
print('locations: ' + answer)

# Top Project Rosalind answer

#s1,s2 = open('rosalind_subs.txt').read().split('\r\n')
#
#for i in range(len(s1)):
#    if s1[i:].startswith(s2):
#        print i+1,
