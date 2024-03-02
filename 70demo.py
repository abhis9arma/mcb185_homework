import itertools
import random

#Dictionary
#Two ways to call a dictionary
d = {}
d = dict()
#Inserting values in a dictionary
d = {"dog" : "woof ", "cat" : "meow"}
print(d)

#Printing from dictionary
print(d["cat"])

#Adding to dictionary
d["pig"] = "oink"
print(d)

#Changing value within dictionary
d["cat"] = "mew"
print(d)

#Deleting value within dictionary
del d["cat"]
print(d)

#Checking if key is within a dictionary
if "dog" in d: print(d["dog"])

#Iterating through a dictionary
for key in d: print(f"{key} says {d[key]}")

#Iterating with dict.items
for k, v in d.items(): print(k, "says", v)

#What happens if you don't unpack your tuples
for thing in d.items(): print(thing[0], thing[1]) # looks bad

#Taking other values
print(d.keys(), d.values(), list(d.values()))



#Lookup Tables
#Accessing values from within a lookup table
seq = "IGEVTQLCYK"

kdtable = {
    'I':  4.5, 'V':  4.2, 'L':  3.8, 'F':  2.8, 'C':  2.5, 'M': 1.9, 'A': 1.8,
    'G': -0.4, 'T': -0.7, 'S': -0.8, 'W': -0.9, 'Y': -1.3, 'P':-1.6, 'H': -3.2,
    'E': -3.5, 'Q': -3.5, 'D': -3.5, 'N': -3.5, 'K': -3.9, 'R': -4.5
}

def kd_dict(seq):
	kd = 0
	for aa in seq: kd += kdtable[aa]
	return kd / len(seq)

print(kd_dict(seq))

import itertools

for k in range(1, 4):
	print(k)
	kcount = {}
	for t in itertools.product("AGCT", repeat=k)
		kmer = "".join(t)
		kcount[kmer] = 0
	print(kcount)
	
	
#Calculating composition using a dictionary
count = {}
for nt in seq:
	if nt not in count: count[nt] = 0
	count[nt] += 1
	
#you can sort within code
# using the sorted function

for k in sorted(count): print(k, count[k])

for k, v in sorted(count.items(), key=lambda item: item[1]):
	print(k, v)
	
for nts in itertools.product("AGCT", repeat = 2):
	print(nts)



