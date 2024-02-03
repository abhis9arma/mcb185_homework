import math
"""

for i in range(1, 10, 3):
	print(i)
	
# range( initial, end, increment)

for i in range(5):
	print(i)
	
for char in "hello":
	print(char)
	
seq = "GAATTC"
for nt in seq:
	print(nt)
	

nts = "ACGT"
for nt1 in nts:
	for nt2 in nts:
		if nt1 == nt2: print(nt1, nt2, "+1")
		else:          print(nt1, nt2, "-1")
		
limit = 4
for i in range(0, limit):
	for j in range(i + 1, limit):
		print(i + 1, j + 1)

"""
		
#practice problems 

#Triangle Problem
def triangle(n):
	tri = 0
	for i in range(n + 1):
		tri = tri + i 
	return tri
		
print(triangle(4))

#Factorial Problem
def factorial(n):
	if n == 0: return 1
	fac = 1
	for i in range(1, n + 1):
		fac = fac * i
	return fac
	
#Euler's Number
def euler(limit):
	e = 0
	for n in range(limit):
		e = e + 1 / factorial(n)
	return e
	
#Perfect Square
def perfectsquare(n):
	root = math.sqrt(n)
	if math.isclose(root, root // 1): return True
	return False
	
#Prime Number
def primenumber(n):
	for den in range(2, n // 2):
		if n % den == 0: return False
	return True
	
print(factorial(4))