

limit = 100
for x in range(1, limit):
	if x % 3 == 0:
		print("Fizz", x)
	if x % 5 == 0:
		print("Buzz", x)
	if x % 3 == 0 and x % 5 == 0:
		print("Fizzbuzz", x)
	else:
		print(x)