
import math

def ntentropy(a, c, g, t):

	pa = a / (a + c + g + t)
	pc = c / (a + c + g + t)
	pg = g / (a + c + g + t)
	pt = t / (a + c + g + t)
	if a > 0:
		sum1 = pa * math.log2(pa)
	elif a == 0:
		sum1 = 0
	if c > 0:
		sum2 = pc * math.log2(pc)
	elif c == 0:
		sum2 = 0
	if g > 0:
		sum3 = pg * math.log2(pg)
	elif g == 0:
		sum3 = 0
	if t > 0:
		sum4 = pt * math.log2(pt)
	elif t == 0:
		sum4 = 0
	entropy = -1 * (sum1 + sum2 + sum3 + sum4)
	return sum4
	
	
print(ntentropy(10, 10, 10, 50))
print(ntentropy(30, 60, 70, 40))
print(ntentropy(00, 60, 70, 45))

