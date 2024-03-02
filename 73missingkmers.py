import mcb185
import sys
import itertools
import dogma

kcount = {}

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	seqrev = dogma.revcomp(seq) 
	for k in range(len(seq)):
		for j in range(len(seq) -k + 1): #window length
			
			kmer1 = seq[j:j+k]
			if kmer1 not in kcount: 
				kcount[kmer1] = 0
			else:
				kcount[kmer1] += 1
			
			kmer2 = seqrev[j:j+k]
			if kmer2 not in kcount:
				kcount[kmer2] = 0
			else:
				kcount[kmer2] += 1
		
		n = 0
		for nts in itertools.product("AGCT", repeat = k):
			kmer = "".join(nts)
			if kmer not in kcount:
				n += 1
		
		if n >= 1:
			print({k}, {n})
			break
	
