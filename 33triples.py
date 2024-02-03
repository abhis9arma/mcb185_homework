#Pythagorean Triples by Abhi Sharma

def pythagoreantriple(x):
	for a in range(1, 101):
		for b in range(a, 101):
			c = (a ** 2 + b ** 2) ** 0.5
			if c <= 100:
				print(int(a), int(b), int(c))
				
pythagoreantriple(1)