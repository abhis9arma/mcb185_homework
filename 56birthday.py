#56birthday.py by Abhi Sharma

import random 
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])


total = 0


for i in range(trials):
	birthdays = i
	birthdays = []
	n = 0
	l = 1
	m = 0
	for j in range(people):
		day = random.randint(1, days)
		birthdays.append(day)
	for k in birthdays:
		new = birthdays[l:]
		if (int(birthdays[m])) in new:
			n += 1
		m += 1
		l += 1
	if n >= 1:
		total += 1
prob = total / trials
print(prob * 100)
