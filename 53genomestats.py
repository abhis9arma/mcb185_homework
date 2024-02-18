#53genomestats by Abhi Sharma

import gzip
import sys

gffpath = sys.argv[1]
feature = sys.argv[2]
lengths = []

total = 0
mini = 10000
maxi = 0

#List Creation
with gzip.open(gffpath, "rt") as fp:
	for line in fp:
		if line[0] == "#": continue
		words = line.split()
		if words[2] != feature: continue
		beg = int(words[3])
		end = int(words[4])
		value = end - beg + 1
		lengths.append(value)

#Count		
n = 0
for val in lengths:
	n += 1
print(f"The count is {n}")	

#Minimum/Maximum
mini = 10000
maxi = 0
for val in lengths:
	if val < mini:
		mini = val
	if val > maxi:
		maxi = val
print(f"The minimum is {mini}")
print(f"The maximum is {maxi}")		

#Mean
total = 0
for val in lengths:
	total += val
mean = total / len(lengths)
print(f"The mean is {mean}")

#StdDev
num = 0
for val in lengths:
	top = (val - mean) ** 2
	num += top
stddev = (num / (len(lengths) - 1)) ** 0.5
print(f"The standard deviation is {stddev}")

#Median

for val in lengths:
	lengths.sort()
	n = len(lengths)
	if n % 2 == 0:
		med1 = lengths[n // 2] 
		med2 = lengths[n // 2 - 1]
		med = (med1 + med2) / 2
	else:
		med = lengths[n // 2]
print(f"The median is {med}")