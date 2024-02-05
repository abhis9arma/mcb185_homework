#nilakantha by Abhi Sharma 

def nilakantha(n):
	sign = 1
	result = 0
	for i in range(1, n):
		x = sign * (4 / ((i * 2) * (i * 2 + 1) * (i * 2 + 2)))
		result = x + result
		sign = sign * -1
	final = 3 + result
	return final
	
print(nilakantha(18))
print(nilakantha(180))
