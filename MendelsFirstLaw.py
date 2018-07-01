#! python3
# Mendel's First Law - Using probability and Mendel's Dominance rules,
# figure out the chance that an offspring will possess the dominant phenotype.
# Given 3 numbers, k, m, and n, which represent the number of Homozygous
# Dominant, Heterozygous, and Homozygous Recessive, respectively.

import re
import operator

print('Where is the data file?')
opened_file = open(input())
read_file = opened_file.read()

values = re.compile(r'[0-9]{1,2}')
pop = values.findall(read_file)

k = int(pop[0]) # Homozygous Dominant (dd)
m = int(pop[1]) # Heterozygous (dr)
n = int(pop[2]) # Homozygous Recessive (rr)
t = k + m + n # Total Population

print(str(k)) # For debugging
print(str(m))
print(str(n))

# Create a dictionary in which to store the probability equations
probs = {"dd and dd":float(k/t * (k-1)/(t-1)),
"dd and dr":float(k/t * m/(t-1)),
"dd and rr":float(k/t * n/(t-1)),
"dr and dd":float(m/t * k/(t-1)),
"dr and dr":float((3/4) * (m/t * (m-1)/(t-1))),
"dr and rr":float((1/2)*(m/t)*(n/(t-1))),
"rr and dd":float(n/t * k/(t-1)),
"rr and dr":float((1/2)*(n/t)*(m/(t-1)))
}

print(probs)
print('Probability of dominant phenotype:\n' +
str(round(sum(probs.values()),5)))

# Top Answer from Project Rosalind:



# Not the top answer from Project Rosalind, but my favorite:

# Read in data
#    use integers to avoid problems with imprecision in integer representation by floating point numbers
#with open('rosalind_iprb.txt', 'r') as infile:
#    (k, m, n) = (int(value) for value in infile.readline().split())

# Total number of pairings:
#total = (k + m + n) ** 2 - (k + m + n)

# Expected number offspring /c recessive phenotype per pairing (RPO)
#   note that this will always be a float, even if m = 0
#expected_RPO = (n + 0.5 * m) ** 2 - (n + 0.25 * m)

#print 1 - expected_RPO / total
