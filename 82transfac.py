#using the jaspsar transfac file and output as json
import gzip
import sys
import json


file = sys.argv[1]

catalog = []
with gzip.open(file, "rt") as fp:
	for line in fp:
		PWM = {}
		if line.startswith("ID"):
			ID, name = line.rstrip().split(" ")
			PWM["id"] = name
			catalog.append(PWM)
		elif line.startswith("0") or line.startswith("1"):
			number, A, C, G, T = line.rstrip().split()
			
			pwm = {
			"A": A,
			"C": C,
			"G": G,
			"T": T,
			}
			PWM["pwm"] = pwm 
			catalog.append(PWM)

print(json.dumps(catalog[:5], indent = 4))