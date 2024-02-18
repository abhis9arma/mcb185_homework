"""
#indexes
seq = "GAATTC"
print(seq[0], seq[-1])

for nt in seq: print(nt, end='')
print()

for i in range(len(seq)):
	print(i, seq[i])

#slices
s = "ABCDEFGHIJ"
print(s[0:5])
print(s[0:8:2])
print(s[0:5], s[:5])
print(s[5:len(s)], s[5:]) 

#tuples
tax = ("Homo", "Sapiens", 9606)
print(tax)

#How to slice strings/ tuples
print(tax[0])
print(tax[::-1])
# -1 in reverse order
#Always unpack the tuple

#enumerate
nts = "ACGT"
for i in range(len(nts)):
	print(i, nts[i])
	
for i, nt in enumerate(nts):
	print(i, nt)
	
#zip
names = ("adenine", "cytosine", "guanine", "thymine")
for i in range(len(names)):
	print(nts[i], names[i])
	
for nt, name in zip(nts, names):
	print(nt, name)
	
for i, (nt, name) in enumerate(zip(nts, names)):
	print(i, nt, name)
	
#Lists
nts = ["A", "T", "C"]
print(nts)
nts[2] = "G"
print(nts)

nts.append("C")
print(nts)

last = nts.pop()
print(last)

nts.sort()
print(nts)
nts.sort(reverse=True)
print(nts)

nucleotides = nts
nucleotides.append("C")
nucleotides.sort()
print(nts, nucleotides)

#list() function
items = list()
print(items)
items.append("eggs")
print(items)

stuff = []
stuff.append(3)
print(stuff)

alph = "ABCDEFGHIJKLMNOP"
print(alph)
aas = list(alph)
print(aas)

#split() and join()
text = "good day  to you"
words = text.split()
print(words)

#for TSC or CSV data
line = "1.41, 2.72, 3.14"
print(line.split(","))

s = "-".join(aas)
print(s)
s = "".join(aas)
print(s)

#searching
if "A" in alph: print("yay")
if "a" in alph: print("no")

print("index G?", alph.index("G"))
print("find G?", alph.find("G"))

if thing in list: idx = list.index(thing)
"""

#Practice problems

#minimum value of a list
def minimum(vals):
	mini = vals[0]
	for val in vals[1:]:
		if val < mini: mini = val
	return mini

x = (2, 3, 4, 7, 10, 25)
print(minimum(x))

#minmax of a list
def minmax(vals):
	mini = vals[0]
	maxi = vals[0]
	for val in vals[1:]:
		if val < mini: mini = val
		if val > maxi: maxi = val
	return mini, maxi

print(minmax(x))

#mean value
def mean(vals):
	total = 0
	for val in vals: totals += val
	return total / len(vals)
	
#entropy probability
import math

def entropy(probs):
	h = 0
	for p in probs:
		h -= p * math.log2(p)
	return h
print(entropy([0.2, 0.3, 0.5]))

# dkl
def dkl(P, Q):
	d = 0
	for p, q in zip(P, Q):
		d += p * math.log2(p/q)
	return d
p1 = [0.4, 0.3, 0.2, 0.1]
p2 = [0.1, 0.3, 0.4, 0.2]
print(dkl(p1, p2))
		
