# nchoosek by Abhi Sharma

def factorial(x):
	if x == 0: return 1
	fac = 1
	for i in range(1, x + 1):
		fac = fac * i
	return fac
	
def nchoosek(n, k):
	assert k >= 0
	if k == 0 or k == n:
		print("1")
	else:
		nk = factorial(n) / (factorial(k) * factorial(n - k))
		return nk
	
	

print(nchoosek(8, 4))
print(nchoosek(3, 0))
print(nchoosek(7, -1))