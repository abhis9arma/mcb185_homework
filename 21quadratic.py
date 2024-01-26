

import math
import sys

def quadratic(a, b, c):
	if b ** 2 - 4*a*c < 0:
		sys.exit("no real solution")
	elif b ** 2 - 4*a*c == 0:
		x = (-b + math.sqrt(b**2 - 4*a*c))/(2 * a)
		return x, x
	else:
		x = (-b + math.sqrt(b**2 - 4*a*c))/(2 * a)
		y = (-b - math.sqrt(b**2 - 4*a*c))/(2 * a)
		return x, y
		
print(quadratic(1, -6, 9))
print(quadratic(1, 4, 3))
print(quadratic(1, -8, 15))
print(quadratic(3, 5, 15))