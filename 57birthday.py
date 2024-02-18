#56birthday.py by Abhi Sharma

import random 
import sys

trials = int(sys.argv[1
people = int(sys.argv[2])

total = 0

for i in range(trials):
	calendar = i
	calendar = []
	for j in range(365):
		calendar.append(0)
	for k in range(people):
		day = random.randint(0, 364)
		calendar[day] += 1
	if 2 in calendar:
		total += 1
		
prob = total / trials
print(prob * 100)
