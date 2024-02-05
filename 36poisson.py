#Poisson by Abhi Sharma
# (n^k e ^ -n/ k!)

import math

def factorial(x):
	if x == 0: return 1
	fac = 1
	for i in range(1, x + 1):
		fac = fac * i
	return fac
	
def poisson(n, k):
	poisson = (n ** k * math.e ** -n)/ factorial(k)
	return poisson
		
print(poisson(5, 4))
print(poisson(9, 8))
print(poisson(2, 4))