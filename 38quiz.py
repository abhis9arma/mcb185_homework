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

#Task 2 Gregory-Leibniz and Nilakantha

def pi(n):
		sign = -1
		result = 0
		degree = 1
		end = 0
		for i in range(1, n):
			x = sign * (1 / (i * 2 + 1))
			y = degree * (4 / ((i * 2) * (i * 2 + 1) * (i * 2 + 2)))
			result = x + result
			end = y + end
			sign = sign * -1
			degree = degree * -1
		total = 1 + result
		pi = total * 4
		final = 3 + end
		return pi, final

print(pi(10))