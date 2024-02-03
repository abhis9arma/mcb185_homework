#Fibonacci by Abhi Sharma
#First 10 numbers of fibonacci sequence

def fibonacci(n):
	a = 0
	b = 1
	print(a)
	print(b)
	for i in range(3, n):
		next = a + b
		a = b
		b = next
		print(next) 
	
fibonacci(10)
	