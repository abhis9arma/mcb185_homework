

limit = 100
for x in range(1, limit):
	if x % 3 == 0:
		print("Fizz")
	if x % 5 == 0:
		print("Buzz")
	if x % 3 == 0 and x % 5 == 0:
		print("FizzBuzz")
	