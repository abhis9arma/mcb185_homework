#nilakantha by Abhi Sharma 

def nilakantha(n):
	sign = 1
	result = 0
	for i in range(1, n):
		x = sign * 4 / ((i + 1) * (i + 2) * (i + 3))
		result = x + result
		sign = sign * -1
	final = 3 + result
	return final
	
print(nilakantha(2))
print(nilakantha(4))
print(nilakantha(7))
print(nilakantha(100))
print(nilakantha(10000000))