import sys
import dogma
import mcb185

file = sys.argv[1]
minimum = int(sys.argv[2])
 

def translation(dna, t):
	translations = []
	for frame in range(3):
		translation = dogma.translate(dna[frame:])			
		orfs = translation.split("*")
		for orf in orfs:
			if "M" in orf:
				begin = orf.find("M")
				protein = orf[begin:]
				if len(protein) >= t:
					translations.append(protein)
	return translations
				
	
for defline, seq in mcb185.read_fasta(file):
	strand1 = translation(seq, minimum)
	strand2 = translation(dogma.revcomp(seq), minimum)
	for protein in strand2:
		strand1.append(protein)
	total = 1
	for protein in strand1:
		print(f">{defline[0:11]}-prot-{total}")
		print(protein)
		total += 1
				
		
	

