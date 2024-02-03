#Scoring Matrix by Abhi Sharma

def scoringmatrix(n):
	nts = "ACGT"  
	for nt1 in nts:
		print("  ", nt1, end=" ")
	print()	
	for nt2 in nts:
		print(nt2, end= " ")
		for nt in nts:
			if nt == nt2:
				print(" +1 ", end=" ")
			else:
				print(" -1 ", end=" ")
		print()		
   		
   	 
scoringmatrix(1)  	
         
	

