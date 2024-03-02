import dogma
import sys
import mcb185

seq = sys.argv[1]
win = int(sys.argv[2])


#seq = "ACGTAGCTACGTACGTAGTAGCTGCTAGCTGACAGC" #test case
#win = 10

for defline, seq in mcb185.read_fasta(seq):
	initial = seq[:win]
	g = initial.count("G")
	c = initial.count("C")
	#calculations for initial window
	gccomp = (g + c) / win

	if g + c == 0: gcskew = 0
	else:          gcskew = (g - c) / (g + c)
	
	print(0, gccomp, gcskew)

	for i in range(len(seq) - win):
		off = seq[i]
		on = seq[i + win]
	
		if off == "G":
			g -= 1
		elif off == "C":
			c -= 1
	
		if on == "G":
			g += 1
		elif on == "C":
			c += 1
	
		gccomp = (g + c) / win
		if g + c == 0:
			gcskew = 0
		else:
			gcskew = (g - c) / (g + c)
	
		print(i + 1, gccomp, gcskew)

		