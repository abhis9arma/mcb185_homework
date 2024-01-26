

def oligotemp(A, C, G, T):
	if A + C + G + T <= 13:
		x = (A + T) * 2 + (G + C) * 4
		return x 
	else:
		x = 64.9 + 41 * (G + C - 16.4)/(A + C + G + T)
		return x
		
		
print(oligotemp(9, 4, 2, 3))
print(oligotemp(4, 4, 2, 3))
print(oligotemp(2, 2, 2, 3))