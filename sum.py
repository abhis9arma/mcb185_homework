

def chksum(s):
	n = 0
	for c in s:
		n = n + ord(c)
	return n % 256	

def maxchar(s):
	mx = 0
	for c in s:
		if ord(c) > mx:
			mx = ord(c)
	return mx
	
def minchar(s):
	mix = 255
	for c in s:
		if ord(c) < mix:
			mix = ord(c)
	return mix
	

name = "natalia"
print(chksum(name))
print(maxchar(name))
print(minchar(name))