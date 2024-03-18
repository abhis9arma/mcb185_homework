import sys
import json
import mcb185

"""
print(sys.argv)
print(sys.argv[0][3])


d = [
	"hello",
	(3.14, "pi"),
	[-1, 0, 1],
	{"year": 2000, "month": 7}
]
	
	
print(d[0][4], d[1][0], d[2][2], d[3]["month"])

#records
oligo = {
	'Name': 'SO116',
    'Length': 18,
    'Sequence': 'ATTTAGGTGACACTATAG',
    'Description': 'SP6 promoter sequencing primer"
}


catalog = []
catalog.append(oligo)



def read_catalog(filepath):
	catalog = []
	with open(filepath) as fp:
		for line in fp:
			if line.startswith("#"): continue
			name, length, seq, desc = line.rstrip().split(",")
			record = {
				"Name": name,
				"Length": length,
				"Sequence": seq,
				"Description": desc
			}
			catalog.append(record)
		return catalog
		
catalog = read_catalog("primers.csv")
for primer in catalog:
	print(primer["Name"], primer["Description"])

	
#In Class Notes - JSON 


person = {
	"name": "Ian Korf",
	"age": 57,
	"weight": 163.8,
	"pets": ["Hesper", "Mouserat", "Labrat"],
	"mentees": {
	"Claire": "undergrad",
	"Dell":"undergrad",
	}
}



people = []
people.append(person) 

people[0]["made this up"] = "hello"
people[0]["mentees"]["Ismael"] = "grad"
people[0]["pets"].append("Fizzbuzz")

print(json.dumps(people, indent = 4))
#You can mix lists and dictionaries within each other



print(person["mentees"]["Claire"])


k = int(sys.argv[2])
kloc = {}
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	words = defline.split()
	chrom = words[0]
	for i in range(len(seq) - k + 1):
		kmer = seq[i:i+k]
		if kmer not in kloc:
			kloc[kmer] = {}
		if chrom not in kloc[kmer]:
			kloc[kmer][chrom] = []
		kloc[kmer][chrom].append(i)
			
			
#		kloc[kmer].append( (chrom, i) )
		
print(json.dumps(kloc, indent=4))



truc = {
    'animals': {'dog': 'woof', 'cat': 'meow', 'pig': 'oink'},
    'numbers': [1.09, 2.72, 3.14],
    'is_complete': False,
}
print(json.dumps(truc, indent=4))

"""

#In Class Notes 03/07
import gzip
import json
import sys
import mcb185

def print_pwm(pwm, ma, id, de):
	print("MA", ma)
	print("XX")
	print("ID", id)
	print("XX")
	print("DE", de)
	print("P0")
	for i, n in enumerate(pwm):
		a = n["A"] 
		c = n["C"]
		g = n["G"]
		t = n ["T"]
		print(f'{i + 1:<8}, {a:<8}, {c:<8}, {g:<8}, {t:<8}')
	print("XX")
	print("//")
	


introns = []
with gzip.open(sys.argv[1], "rt") as fp:
	for line in fp:
		f = line.split()
		if f[2] != "intron": continue
		chrom = f[0]
		beg = int(f[3]) -1
		end = int(f[4]) -1
		strand = f[6]
		if f[5] == ".": continue
		n = float(f[5])
		introns.append( (chrom, beg, end, strand, n) )
#print("introns", len(introns))

dons = []
accs = []
dlen = 6
aclen = 8
for i in range(dlen):
	dons.append({"A": 0, "C": 0, "G": 0, "T": 0})
for i in range(aclen):
	accs.append({"A": 0, "C": 0, "G": 0, "T": 0})



for defline, seq in mcb185.read_fasta(sys.argv[2]):
	words = defline.split()
	chrom = words[0]
	for c, b, e, s, n in introns:
		if chrom == c :
			iseq = seq[b:e+1]
			if s == "-": iseq = mcb185.anti_seq(iseq)
			
			don = iseq[:6]
			for i, nt in enumerate(don):
				dons[i][nt] += n
			
			acc = iseq[-8:]
			for i, nt in enumerate(acc):
				accs[i][nt] += n
				
		
print_pwm(dons, "mad", "ik01", "hello")
print_pwm(accs, "maa", "ik02", "world")



		



