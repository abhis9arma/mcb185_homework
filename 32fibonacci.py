#Fibonacci by Abhi Sharma
#First 10 numbers of fibonacci sequence

a = 0
b = 1
print(a)
print(b)
for i in range(3, 10):
	next = a + b
	a = b
	b = next
	print(next)
	

	