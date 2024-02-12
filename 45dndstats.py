#dndstats by Abhi Sharma
import random


total1 = 0
total2 = 0
total3 = 0
total4 = 0
limit = 1000000


#3D6
for i in range(limit):
	for j in range(3):
		d1 = random.randint(1, 6)
		total1 += d1
	average1 = total1 / limit
print(average1)


#3D6r1
for i in range(limit):
	for j in range(3):
		d1 = random.randint(1, 6)
		if d1 == 1:
			d1 = random.randint(1, 6)
		total2 += d1
	average2 = total2 / limit
print(average2)


#3D6x2
for i in range(limit):
	for j in range(3):
		d1 = random.randint(1 ,6)
		d2 = random.randint(1, 6)
		if d1 >= d2:
			total3 += d1
		else:
			total3 += d2
	average3 = total3 / limit
print(average3)


#4D6d1
for i in range(limit):
	d1 = random.randint(1, 6)
	d2 = random.randint(1, 6)
	d3 = random.randint(1, 6)
	d4 = random.randint(1, 6)
	if d1 <= d2 and d1 <= d3 and d1 <= d4:
		total4 += d2 + d3 + d4
	elif d2 < d1 and d2 <= d3 and d2 <= d4:
		total4 += d1 + d3 + d4
	elif d3 < d1 and d3 < d2 and d3 <= d4:
		total4 += d1 + d2 + d4
	elif d4 < d1 and d4 < d2 and d4 < d3:
		total4 += d1 + d2 + d3
average4 = total4 / limit
print(average4)
		
