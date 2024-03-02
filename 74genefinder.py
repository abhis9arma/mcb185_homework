import mcb185

seq = "ATGATGGCGAATTAACCCAAAGGTTCAT"
#F0       M   M   A   N   *
#F1   * 
anti = mcb185.anti_seq(seq)
seq = anti
print(anti)


for frame in range(3):
	print(frame)
	stop_used = {}
	fseq = seq[frame:]
	i = 0
	for i in range(0, len(fseq) - 3 + 1, 3): #manual loop (not for) so we can kill it whehn you find the longest seq
		codon = fseq[i:i+3]
		if codon != "ATG": continue
		for j in range(i, len(fseq) - 2, 3):
			codon = fseq[j:j+3]
			if codon == "TAA" or codon == "TAG" or codon == "TGA":
				stop = j
				if stop not in stop_used:
					print("gene", i,  j)
					print("gene", len(anti) - i, len(anti) - j - 1) # rev comp, coordinates in the opposite direction
					stop_used[stop] = True
					
					
					
# Do it again for the revcomp, makes sense to make above code into a fucntion so its easier

