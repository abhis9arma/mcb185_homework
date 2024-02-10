#43RandomDNA by Abhi Sharma
import random

seq = 3
seqnum = 1
for i in range(1, seq + 1):
	print()
	print(f">seq-{seqnum}")
	seqnum += 1
	seqlength = random.randint(50, 60)
	for j in range(1, seqlength):
		print(random.choice('ACGT'), end='')
		

		
