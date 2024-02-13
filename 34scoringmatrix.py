#Scoring Matrix by Abhi Sharma


nts = "ACGT"
print(end=" ")  
for nt1 in nts:
	print(" ", nt1, end="")
print()	
for nt2 in nts:
	print(nt2, end= " ")
	for nt in nts:
		if nt == nt2:
			print("+1", end=" ")
		else:
			print("-1", end=" ")
	print()		
	

