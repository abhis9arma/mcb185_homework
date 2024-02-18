#57birthday.py by Abhi Sharma

import random 
import sys

trials = int(sys.argv[1])
people = int(sys.argv[2])

 
total = 0 
for i in range(trials):
	calendar = []
	for j in range(365):
		calendar.append(0)
	for j in range(people):
		date = random.randint(0, 364)
		calendar[date] += 1
		if calendar[date] >= 2:
			total += 1
			break

prob = total / trials
print(prob * 100)
	