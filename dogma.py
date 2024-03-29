#dogma

#Transcription
def transcribe(dna):
	return dna.replace("T", "U")
	
#Reverse-Complement
def revcomp(dna):
	rc = []
	for nt in dna[::-1]:
		if   nt == "A": rc.append("T")
		elif nt == "C": rc.append("G")
		elif nt == "G": rc.append("C")
		elif nt == "T": rc.append("A")
		else:			rc.append("N")
	return ''.join(rc)
	
#Translate
def translate(dna):
	aas = []
	for i in range(0, len(dna), 3):
		codon = dna[i:i+3]
		if   codon == "ATG": aas.append("M")
		elif codon == "TAA": aas.append("*")
		elif codon == "TAG": aas.append("*")
		elif codon == "TAC": aas.append("Y")
		elif codon == "TAT": aas.append("Y")
		elif codon == "TTT": aas.append("F")
		elif codon == "TTC": aas.append("F")
		elif codon == "TTA": aas.append("L")
		elif codon == "TTG": aas.append("L")
		elif codon == "CTT": aas.append("L")
		elif codon == "CTC": aas.append("L")
		elif codon == "CTA": aas.append("L")
		elif codon == "CTG": aas.append("L")
		elif codon == "ATT": aas.append("I")
		elif codon == "ATC": aas.append("I")
		elif codon == "ATA": aas.append("I")
		elif codon == "GTT": aas.append("V")
		elif codon == "GTC": aas.append("V")
		elif codon == "GTA": aas.append("V")
		elif codon == "GTG": aas.append("V")
		elif codon == "TCT": aas.append("S")
		elif codon == "TCC": aas.append("S")
		elif codon == "TCA": aas.append("S")
		elif codon == "TCG": aas.append("S")
		elif codon == "CCT": aas.append("P")
		elif codon == "CCC": aas.append("P")
		elif codon == "CCA": aas.append("P")
		elif codon == "CCG": aas.append("P")
		elif codon == "ACT": aas.append("T")
		elif codon == "ACC": aas.append("T")
		elif codon == "ACA": aas.append("T")
		elif codon == "ACG": aas.append("T")
		elif codon == "GCT": aas.append("A")
		elif codon == "GCC": aas.append("A")
		elif codon == "GCA": aas.append("A")
		elif codon == "GCG": aas.append("A")
		elif codon == "TGT": aas.append("C")
		elif codon == "TGC": aas.append("C")
		elif codon == "TGA": aas.append("*")
		elif codon == "TGG": aas.append("W")
		elif codon == "CAT": aas.append("H")
		elif codon == "CAC": aas.append("H")
		elif codon == "CAA": aas.append("Q")
		elif codon == "CAG": aas.append("Q")
		elif codon == "CGT": aas.append("R")
		elif codon == "CGC": aas.append("R")
		elif codon == "CGA": aas.append("R")
		elif codon == "CGG": aas.append("R")
		elif codon == "AAT": aas.append("N")
		elif codon == "AAC": aas.append("N")
		elif codon == "AAA": aas.append("K")
		elif codon == "AAG": aas.append("K")
		elif codon == "AGT": aas.append("S")
		elif codon == "AGC": aas.append("S")
		elif codon == "AGA": aas.append("R")
		elif codon == "AGG": aas.append("R")
		elif codon == "GAT": aas.append("D")
		elif codon == "GAC": aas.append("D")
		elif codon == "GAA": aas.append("E")
		elif codon == "GAG": aas.append("E")
		elif codon == "GGT": aas.append("G")
		elif codon == "GGC": aas.append("G")
		elif codon == "GGA": aas.append("G")
		elif codon == "GGG": aas.append("G")
		else: 			     aas.append("X")
	return ''.join(aas)
	
#GCcomp
def gc_comp(seq):
	return (seq.count("C") + seq.count("G")) / len(seq)
	
#GCskewed
def gc_skew(seq):
	c = seq.count("C")
	g = seq.count("G")
	if c + g == 0: return 0
	return (g - c) / (g + c)
	
#Kyte-Doolittle Hydropathy

def kdh(dna):
	KD = 0
	for aa in dna:
		if aa == "A":
			KD += 1.80
		if aa == "C":
			KD += 2.50
		if aa == "D":
			KD += -3.50
		if aa == "E":
			KD += -3.50
		if aa == "F":
			KD += 2.80
		if aa == "G":
			KD += -0.40
		if aa == "H":
			KD += -3.20
		if aa == "I":
			KD += 4.50
		if aa == "K":
			KD += -3.90
		if aa == "L":
			KD += 3.80
		if aa == "M":
			KD += 1.90
		if aa == "N":
			KD += -3.50
		if aa == "P":
			KD += -1.60
		if aa == "Q":
			KD += -3.50
		if aa == "R":
			KD += -4.50
		if aa == "S":
			KD += -0.80
		if aa == "T":
			KD += -0.70
		if aa == "V":
			KD += 4.20
		if aa == "W":
			KD += -0.90
		if aa == "Y":
			KD += -1.30
		else:
			KD += 0
	return KD / len(dna)
	
	
kdh = {
	'I':  4.5, 'V':  4.2, 'L':  3.8, 'F':  2.8, 'C':  2.5,
	'M':  1.9, 'A':  1.8, 'G': -0.4, 'T': -0.7, 'S': -0.8,
	'W': -0.9, 'Y': -1.3, 'P': -1.6, 'H': -3.2, 'E': -3.5,
	'Q': -3.5, 'D': -3.5, 'K': -3.9, 'N': -3.5, 'R': -4.5,
}
def hydropathy(seq):
	s = 0
	for aa in seq:
		s += kdh[aa]
	return s / len(seq)
	
	

	