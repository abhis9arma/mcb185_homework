import mcb185
import sys
import itertools

k = int(sys.argv[2])
kcount = {}

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	for i in range(len(seq) -k + 1): #window length
		kmer = seq[i:i+k]
		if kmer not in kcount: kcount[kmer] = 0
		kcount[kmer] += 1
	for kmer, n in kcount.items(): print(kmer, n)
	

for nts in itertools.product("AGCT", repeat = k):
	kmer = "".join(nts)
	if kmer in kcount: print(kmer, kcount[kmer])
	else:              print(kmer, 0)