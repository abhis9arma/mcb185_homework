import gzip
import sys
import mcb185

file = sys.argv[1]


with gzip.open(file, "rt") as fp: 
	sequence = []
	coord = []
	seq = False
	for line in fp:
		line = line.rstrip()
		if line.startswith("VERSION"):
			line = line.split()
			AC = line[1]
		elif "/organism=" in line:
			line = line.replace('"', '').split("=")
			id = line[1]
		elif line.startswith("     CDS"):
			if "join" in line: continue
			elif "complement" in line:
				start = line.find("(") + 1
				stop = line.find(")")
				beg, end = line[start:stop].split("..")
				coord.append((int(beg), int(end), "-"))
			else:
				beg, end = line.split()[1].split("..")
				coord.append((int(beg), int(end), "+"))
		elif line.startswith("ORIGIN"):
			seq = True
			continue
		if seq:
			line = line.split()
			for seq in line[1:]:
				sequence.append(seq)
	sequence = "".join(sequence).upper()	

kozaks = []
for i in range(14):
	kozaks.append({
		"A": 0,
		"C": 0,
		"G": 0,
		"T": 0})

for beg, end, strand in coord:
	if strand == "-":
		kozak = sequence[stop - 5: stop + 9]
		kozak = mcb185.anti_seq(kozak)
	else:
		kozak = sequence[start - 10: start + 4]
	for i, nt in enumerate(kozak):
		kozaks[i][nt] += 1
		
		
		
print("AC", AC)
print("XX")
print("ID", id)
print("XX")
print("DE I also made this up")
print("P0      A       C       G       T")
for i, cnts in enumerate(kozaks):
	print(f'{i+1:<8}', end="")
	for nt in "ACGT":
		print(f'{kozaks[i][nt]:<8}', end="")
	print()
print("XX")
print("//")