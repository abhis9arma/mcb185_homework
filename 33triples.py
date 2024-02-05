#Pythagorean Triples by Abhi Sharma

def pythagoreantriple(x):
	for a in range(1, 100):
		for b in range(a + 1, 100):
			c = (a ** 2 + b ** 2) ** 0.5
			if c <= 100 and c == int(c):
				print(a, b, c)
				
print(pythagoreantriple(1))