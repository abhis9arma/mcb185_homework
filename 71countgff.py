import gzip
import sys

count = {}
with gzip.open(sys.argv[1], "rt") as fp:
	for line in fp:
		if line.startswith("#"): continue
		f = line.split()
		feature = f[2]
		if feature not in count: count[feature] = 0
		count[feature] += 1 
for f, n in count.items(): print(f, n)

#lines 7 and 8 can also be replaced
# if feature not in count: count[feature] = 1
# else:                    count[feature] += 1

