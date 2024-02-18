#56birthday.py by Abhi Sharma

import random 
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])


total = 0

for i in range(trials):
	# create lists with dates of birthdays
	bds = []
	for j in range(people):
		day = random.randint(0, days - 1)
		# checks if the day is already within the list
		if day in bds:
			total += 1
			break
		else:
			bds.append(day)
prob = (total / trials) * 100
print(prob)

		
