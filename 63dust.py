#63dust.py by Abhi Sharma
import sys
import mcb185

file = sys.argv[1]
win = int(sys.argv[2])
ent = float(sys.argv[3])


for defline, seq in mcb185.read_fasta(file):
	print(defline)	
	output = []
	for i in range(0, len(seq) - win + 1, win):
		#can't jump by 60
		s = seq[i:i+win]
		nts = 'ACGT'
		counts = [0] * len(nts) 
		for nt in s:
			idx = nts.find(nt)
			counts[idx] += 1 
		A = counts[0]
		C = counts[1]
		G = counts[2]
		T = counts[3]
		entropy = mcb185.ntentropy(A, C, G, T)
		if entropy < ent:
			for j in range(len(s)):
				output.append("N")
		else:
			output.append(s)
	output = "".join(output)
	print(output[:300])
			
	#if the window has an entropy size less than 1.4, relace nts with N
	