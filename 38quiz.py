# Abhi Sharma and Connor Suen


#Task 1 Gregory-Leibniz

def gregory(n):
	sign = -1
	result = 0
	for i in range(1, n):
		x = sign * (1 / (i * 2 + 1))
		result = x + result
		sign = sign * -1
	final = 1 + result
	pi = final * 4
	print(pi)
	return final
		
print(gregory(2))
print(gregory(1000))

#