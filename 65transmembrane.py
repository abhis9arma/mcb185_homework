import sys
import dogma
import mcb185

file = sys.argv[1] 
				
def signalseq(dna):
	signalregion = dna[:30]
	wlen = 8
	for i in range(len(signalregion) - wlen + 1):
		signallength = signalregion[i:i+wlen]
		kd1 = dogma.kdh(signallength)
		if kd1 >= 2.5 and "P" not in signallength:
			return True
	return False		
			
def membraneseq(dna):	
	membraneregion = dna[30:]
	wlen = 11
	for i in range(len(membraneregion) - wlen + 1):
		membranelength = membraneregion[i:i+wlen]
		kd2 = dogma.kdh(membranelength)
		if kd2 >= 2.0 and "P" not in membranelength:
			return True
	return False
										
total = 0
for defline, seq in mcb185.read_fasta(file):
	if signalseq(seq) and membraneseq(seq):
			print(defline)
			total += 1
print(total)



	