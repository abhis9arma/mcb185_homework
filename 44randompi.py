#44randompi by Abhi Sharma
import random

inside = 0
outside = 0
while True:	
	x = random.random()
	y = random.random()
	z = (x ** 2 + y ** 2) ** 0.5
	if z < 1:
		inside += 1
	elif z > 1:
		outside += 1 
	ratio = inside / (inside + outside)
	pi = 4 * ratio
	print(pi)





