#Pythagorean Triples by Abhi Sharma

limit = 100

for a in range(1, limit):
	for b in range(a + 1, limit):
		c = (a ** 2 + b ** 2) ** 0.5
		if a < 100 and b < 100 and c % 1 == 0:
			print(a, b, c)
			

