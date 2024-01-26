

def aminoacidhp(x):
	if x == "a":
		return("The Kyte-Doolittle Hydrophobic Value is 1.80")
	if x == "c":
		return("The Kyte-Doolittle Hydrophobic Value is 2.50")
	if x == "d":
		return("The Kyte-Doolittle Hydrophobic Value is -3.50")
	if x == "e":
		return("The Kyte-Doolittle Hydrophobic Value is -3.50")
	if x == "f":
		return("The Kyte-Doolittle Hydrophobic Value is 2.80")
	if x == "g":
		return("The Kyte-Doolittle Hydrophobic Value is -0.40")
	if x == "h":
		return("The Kyte-Doolittle Hydrophobic Value is -3.20")
	if x == "i":
		return("The Kyte-Doolittle Hydrophobic Value is 4.50")
	if x == "k":
		return("The Kyte-Doolittle Hydrophobic Value is -3.90")
	if x == "l":
		return("The Kyte-Doolittle Hydrophobic Value is 3.80")
	if x == "m":
		return("The Kyte-Doolittle Hydrophobic Value is 1.90")
	if x == "n":
		return("The Kyte-Doolittle Hydrophobic Value is -3.50")
	if x == "p":
		return("The Kyte-Doolittle Hydrophobic Value is -1.60")
	if x == "q":
		return("The Kyte-Doolittle Hydrophobic Value is -3.50")
	if x == "r":
		return("The Kyte-Doolittle Hydrophobic Value is -4.50")
	if x == "s":
		return("The Kyte-Doolittle Hydrophobic Value is -0.80")
	if x == "t":
		return("The Kyte-Doolittle Hydrophobic Value is -0.70")
	if x == "v":
		return("The Kyte-Doolittle Hydrophobic Value is 4.20")
	if x == "w":
		return("The Kyte-Doolittle Hydrophobic Value is -0.90")
	if x == "y":
		return("The Kyte-Doolittle Hydrophobic Value is -1.30")
	else:
		return("That entry does not encode for an Amino Acid")
		
		
		

print(aminoacidhp("y"))
print(aminoacidhp("x"))
print(aminoacidhp("c"))




