#61skewer.py by Abhi Sharma
import dogma
import sys
import mcb185

seq = sys.argv[1]
w = int(sys.argv[2])

#seq = "ACGTACGTGGGGGACGTACGTCCCCC"
#w = 10
for defline, seq in mcb185.read_fasta(seq):
	for i in range(len(seq) - w + 1):
		s = seq[i:i+w]
		print(f'{i}\t{dogma.gc_comp(s):.3f}\t{dogma.gc_skew(s):.3f}')