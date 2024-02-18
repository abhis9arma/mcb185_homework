#55colorname.py

import sys

colorfile = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])

d = 0
d1 = 10000
fp = open(colorfile)
for line in fp:
	words = line.split()
	color = words[0]
	val = (words[2].split(","))
	r = int(val[0])
	g = int(val[1])
	b = int(val[2])
	r1 = abs(r - R)
	g1 = abs(g - G)
	b1 = abs(b - B)
	d = r1 + b1 + g1
	if d < d1:
		target = color
		d1 = d
print(target)


